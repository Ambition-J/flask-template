# !/use/bin/python3
# _*_ coding:utf-8 _*_
# __author__ : __ajiang__
# 2020/7/11

import os

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


class Application(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        if 'os_config' in os.environ:
            self.config.from_pyfile('config/{}_setting.py'.format(os.environ['os_config']))
            db.init_app(self)


db = SQLAlchemy()
application = Application(__name__)
manager = Manager(application)
