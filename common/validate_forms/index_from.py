# !/use/bin/python3
# _*_ coding:utf-8 _*_
# __author__ : __ajiang__
# 2020/7/11
from wtforms import Form, IntegerField, StringField
from wtforms.validators import Length, DataRequired, NumberRange


class IndexForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='查找字段不符合规范')])
    page = IntegerField(validators=[NumberRange(1, 99, message='查找页数超出最大范围')], default=1)
