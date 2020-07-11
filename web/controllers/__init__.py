# !/use/bin/python3
# _*_ coding:utf-8 _*_
# __author__ : __ajiang__
# 2020/7/11

from flask import Blueprint

# 声明api路由蓝图
route_api = Blueprint('api_page', __name__)
# 引入api下的所有模块
from web.controllers.index.index import *


@route_api.route('/')
def index():
    return 'welcome to index'
