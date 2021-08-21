#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 9:52
# @Author  : cendeavor
# @File    : models.py
# @Software: PyCharm

from flask_login import UserMixin

class User(UserMixin):
    """用户类"""
    def __init__(self, user):
        self.username = user.get("username")
        self.password = user.get("password")
        # self.password_hash = user.get("password")
        self.id = user.get("username")  # 为了简化，id == username

    def verify_password(self, password):
        """密码验证"""
        if self.password != password:
            return False
        return True
        # if self.password_hash is None:
        #     return False
        # return check_password_hash(self.password_hash, password)