# !/use/bin/python3
# _*_ coding:utf-8 _*_
# __author__ : __ajiang__
# 2020/7/11

from web.controllers import route_api


@route_api.route('/index')
def index():
    return 'hello word'
