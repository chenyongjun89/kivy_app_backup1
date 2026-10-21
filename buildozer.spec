[app]

# App 显示的名称
title = 我的记账本

# 包名，必须全是小写字母
package.name = mybookkeeper
package.domain = org.test

# 源代码所在的目录
source.dir = .

# 允许打包的文件后缀
source.include_exts = py,png,jpg,kv,atlas,ttc,json

# 主入口文件
source.main = main.py

# 版本号
version = 1.0

# ★ 核心修复：锁定 Kivy 版本和 pyjnius，防止云端拉取最新版本导致报错
requirements = python3==3.10,kivy==2.2.1,pyjnius==1.5.0

# 竖屏
orientation = portrait
fullscreen = 0

# 安卓权限
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# 编译目标（保持单架构，防止内存溢出）
android.api = 30
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# 自动接受 SDK 协议
android.accept_sdk_license = True
