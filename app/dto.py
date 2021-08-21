#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 14:54
# @Author  : cendeavor
# @File    : dto.py
# @Software: PyCharm


class ResultDO:

    def __init__(self, code, msg, data):
        self.code = code  # 状态码
        self.msg = msg  # 提示信息
        self.data = data  # 返回的数据

    def to_dict(self):
        return {"code": self.code, "msg": self.msg, "data": self.data}


class Response:

    @staticmethod
    def success(msg="处理请求成功!", data=None):
        """
        成功的响应
        :param msg: 消息
        :param data: 返回的数据
        :return: ResultDO
        """
        if not data:
            data = {}
        return ResultDO(200, msg, data).to_dict()

    @staticmethod
    def error(code=400, msg="处理请求失败!", data=None):
        """
        错误的响应
        :param code: 状态码
        :param msg: 消息
        :return:
        """
        if not data:
            data = {}
        return ResultDO(code, msg, data).to_dict()
