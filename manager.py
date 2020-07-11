# !/use/bin/python3
# _*_ coding:utf-8 _*_
# __author__ : __ajiang__
# 2020/7/11

from flask_script import Server

from app import application, manager
# 加载路由蓝图文件
import routers

manager.add_command('runserver', Server(host='0.0.0.0', port=application.config['SERVER_PORT'],
                                        use_debugger=application.config['DEBUG'], use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
