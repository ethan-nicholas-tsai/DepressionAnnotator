#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 19:35
# @Author  : cendeavor
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, DataRequired, EqualTo


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('注册')


class LoginForm(FlaskForm):
    """登录表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')
