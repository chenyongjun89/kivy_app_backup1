[app]

# App 显示的名称
title = 我的记账本

# 包名，必须全是小写字母，不能有中文
package.name = mybookkeeper
package.domain = org.test

# 允许打包的文件后缀（必须包含 kv 和 ttc，否则界面和字体加载不出来）
source.include_exts = py,png,jpg,kv,atlas,ttc,json

# 主入口文件
source.main = main.py

# 版本号
version = 1.0

# 依赖库（必须包含 jnius，且不要写版本号）
requirements = python3,kivy,pyjnius,android

# 允许屏幕竖屏
orientation = portrait
fullscreen = 0

# 安卓权限：允许读写文件（必须加，否则无法读取 records.json）
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# 编译目标版本
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
