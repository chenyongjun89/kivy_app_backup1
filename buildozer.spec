[app]
title = 我的记账本
package.name = mybookkeeper
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttc,json
source.main = main.py
version = 1.0

# 保持这样写，云端会自动匹配
requirements = python3,kivy,pyjnius

orientation = portrait
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# 锁定使用 master 分支，坚决不用开发版
p4a.branch = master
