from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.core.text import LabelBase
from kivy.utils import platform
import json
import os
import csv
from datetime import datetime

# 注册中文字体
LabelBase.register(name="Roboto", fn_regular="msyh.ttc")

if platform == 'android':
    from android.storage import app_storage_path
    DATA_FILE = os.path.join(app_storage_path(), "records.json")
else:
    DATA_FILE = "records.json"

class RecordRow(BoxLayout):
    text = StringProperty("")
    amount_str = StringProperty("")
    amount_color = ListProperty([0, 0, 0, 1])
    index = NumericProperty(0)

class ExpenseTracker(BoxLayout):
    total_income = StringProperty("0.00")
    total_expense = StringProperty("0.00")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_list()

    def on_type_toggle(self):
        is_income = self.ids.type_switch.state == 'down'
        if is_income:
            self.ids.category_spinner.values = ('工资', '奖金', '红包', '理财收益', '退款', '其他')
        else:
            self.ids.category_spinner.values = ('餐饮', '购物', '交通', '话费', '医疗', '其他')
        self.ids.category_spinner.text = '选择分类'

    def save_record(self):
        amount_str = self.ids.amount_input.text
        category = self.ids.category_spinner.text
        platform = self.ids.platform_spinner.text
        note = self.ids.note_input.text
        
        is_income = self.ids.type_switch.state == 'down'
        record_type = "收入" if is_income else "支出"

        if not amount_str or category == '选择分类' or platform == '选择平台':
            return

        try:
            amount = float(amount_str)
        except ValueError:
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        record = {
            "date": now,
            "type": record_type,
            "amount": amount,
            "category": category,
            "platform": platform,
            "note": note
        }
        
        records = self.load_json()
        records.append(record)
        self.save_json(records)

        self.ids.amount_input.text = ""
        self.ids.note_input.text = ""
        self.ids.category_spinner.text = '选择分类'
        self.ids.platform_spinner.text = '选择平台'
        self.ids.type_switch.state = 'normal' 
        
        self.refresh_list()

    def delete_record(self, index):
        records = self.load_json()
        if 0 <= index < len(records):
            records.pop(index)
            self.save_json(records)
            self.refresh_list()

    def load_json(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_json(self, records):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

    def export_data(self):
        records = self.load_json()
        if not records: return
            
        export_file = "我的记账数据.csv"
        with open(export_file, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["时间", "类型", "平台", "分类", "金额", "备注"])
            for r in records:
                writer.writerow([r.get("date", ""), r.get("type", "支出"), r["platform"], r["category"], r["amount"], r["note"]])
        print(f"导出成功！文件已保存在：{os.path.abspath(export_file)}")

    def update_month_spinner(self):
        records = self.load_json()
        months = sorted(list(set([r.get("date", "")[:7] for r in records if r.get("date")])), reverse=True)
        values = ['全部'] + months
        
        current = self.ids.month_spinner.text
        self.ids.month_spinner.values = values
        if current not in values:
            self.ids.month_spinner.text = '全部'

    def refresh_list(self):
        self.update_month_spinner()
        
        rv_data = []
        records = self.load_json()
        
        # 获取双重过滤器
        selected_month = self.ids.month_spinner.text
        selected_category = self.ids.category_filter_spinner.text
        
        month_prefix = "" if selected_month == '全部' else selected_month

        income_sum = 0.0
        expense_sum = 0.0
        filtered_records = []

        for i, r in enumerate(records):
            # 1. 月份过滤
            if month_prefix and not r.get("date", "").startswith(month_prefix):
                continue
            # 2. 分类过滤
            if selected_category != '全部分类' and r.get("category") != selected_category:
                continue
                
            filtered_records.append((i, r))
            
            r_type = r.get("type", "支出")
            if r_type == "收入":
                income_sum += r['amount']
            else:
                expense_sum += r['amount']

        for i, r in reversed(filtered_records):
            r_type = r.get("type", "支出")
            
            if r_type == "收入":
                color = [0.2, 0.7, 0.2, 1] 
                prefix = "+"
            else:
                color = [0.9, 0.3, 0.3, 1] 
                prefix = "-"

            date_str = r.get('date', '旧数据')[5:16] 

            rv_data.append({
                'text': f"{date_str} | [{r['platform']}] {r['category']} | {r['note']}",
                'amount_str': f"{prefix}{r['amount']:.2f}",
                'amount_color': color,
                'index': i
            })

        self.ids.rv.data = rv_data
        self.total_income = f"{income_sum:.2f}"
        self.total_expense = f"{expense_sum:.2f}"

class ExpenseApp(App):
    def build(self):
        self.title = "我的记账本"
        return ExpenseTracker()

if __name__ == '__main__':
    ExpenseApp().run()