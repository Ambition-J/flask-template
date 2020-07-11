# !/use/bin/python3
# _*_ coding:utf-8 _*_
# __author__ : __ajiang__
# 2020/7/11

SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = 'IPARTAKER'

# 过滤url
IGNORE_URLS = [
    "^/api",
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico",
]