#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 22:46
# @Author  : cendeavor
# @Site    : 
# @File    : auth_service.py
# @Software: PyCharm

from app import login_manager
from app.models import User


# 从请求参数中获取Token，如果Token所对应的用户存在则构建一个新的用户类对象
# 并使用用户名作为ID，如果不存在，必须返回None
# @login_manager.request_loader
# def load_user_from_request(request):
#     username = request.args.get('token')

# 如果用户名存在则构建一个新的用户类对象，并使用用户名作为ID
# 如果不存在，必须返回None
@login_manager.user_loader
def load_user(username):
    user = AuthService.query_user(username)
    if user is not None:
        curr_user = User(user)
        curr_user.id = username
        return curr_user


class AuthService:
    # 用户记录表
    users = [
        {'username': 'cendeavor', 'password': 'cendeavor'},
        {'username': 'Michael', 'password': '123456'},
        {'username': 'zx', 'password': '123456'},
        {'username': 'gxt' , 'password': '123456'},
        {"username": 'cty', 'password': '18326631695'},
        {'username': 'YHL', 'password': '123456'}
    ]

    @staticmethod
    def query_user(username):
        """ 通过用户名，获取用户记录，如果不存在，则返回None

        Args:
            username:

        Returns:

        """
        for user in AuthService.users:
            if user['username'] == username:
                return user
