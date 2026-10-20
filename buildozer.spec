[app]

# App 显示的名称
title = 我的记账本

# 包名，必须全是小写字母
package.name = mybookkeeper
package.domain = org.test

# ★ 核心修复：源代码所在的目录（. 表示当前根目录）
source.dir = .

# 允许打包的文件后缀（包含 kv 和字体，千万别漏）
source.include_exts = py,png,jpg,kv,atlas,ttc,json

# 主入口文件
source.main = main.py

# 版本号
version = 1.0

# 依赖库（必须用 pyjnius）
requirements = python3,kivy,pyjnius

# 竖屏
orientation = portrait
fullscreen = 0

# 安卓权限：允许读写文件（确保你的 records.json 能存下来）
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# 编译目标
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
