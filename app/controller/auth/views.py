#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:07
# @Author  : cendeavor
# @File    : views.py
# @Software: PyCharm

from app.forms import LoginForm
from app.service.auth_service import AuthService
from app.models import User
from app.dto import Response
from flask import request, render_template, jsonify, flash, redirect, url_for, flash
from flask_login import login_user, current_user
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = AuthService.query_user(username)
        # 验证表单中提交的用户名和密码（需要写到 AuthService里面）
        if user is not None:
            curr_user = User(user)
            if curr_user.verify_password(password=password):
                # 通过Flask-Login的login_user方法登录用户
                login_user(curr_user)

                # 如果请求中有next参数，则重定向到其指定的地址，
                # 没有next参数，则重定向到"index"视图
                return redirect(request.args.get('next') or url_for('main.index'))

        # emsg = "用户名或密码有误"
        flash('用户名或密码错误!', category='info')
    # GET 请求
    return render_template('/auth/login.html', form=form)
