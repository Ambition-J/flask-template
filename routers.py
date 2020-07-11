# !/use/bin/python3
# _*_ coding:utf-8 _*_
# __author__ : __ajiang__
# 2020/7/11

# 路由蓝图集合
from app import application
from web.controllers import route_api

application.register_blueprint(route_api, url_prefix='/api')
