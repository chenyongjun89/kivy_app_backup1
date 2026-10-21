[app]
title = 我的记账本
package.name = mybookkeeper
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttc,json
source.main = main.py
version = 1.0

# 核心：绝对不写版本号，让系统自己匹配
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# 核心：强制使用稳定分支，拒绝 Python 3.14
p4a.branch = master
