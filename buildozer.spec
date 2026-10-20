[app]

# App 显示的名称
title = 我的记账本

# 包名，必须全是小写字母
package.name = mybookkeeper
package.domain = org.test

# 源代码所在的目录（. 表示当前根目录）
source.dir = .

# 允许打包的文件后缀
source.include_exts = py,png,jpg,kv,atlas,ttc,json

# 主入口文件
source.main = main.py

# 版本号
version = 1.0

# 依赖库
requirements = python3,kivy,pyjnius

# 竖屏
orientation = portrait
fullscreen = 0

# 安卓权限
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# 编译目标
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# ★ 核心修复：自动接受安卓 SDK 许可协议（加在最下面）
android.accept_sdk_license = True
