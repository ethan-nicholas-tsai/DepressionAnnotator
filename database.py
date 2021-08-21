#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 9:48
# @Author  : cendeavor
# @File    : database.py
# @Software: PyCharm


from pymongo import MongoClient
from conf.settings import DevelopmentConfig


class MongoDBC:
    """MongoDBConnector

    """

    def __init__(self, uri=DevelopmentConfig.MONGO_URI):
        # 重写该类或者填充本地数据库配置信息
        self.uri = uri
        self.db = None
        self.cli = None

    def connect(self):
        try:
            client = MongoClient(self.uri)
            # database = client[self.database]
            # database.authenticate(self.username, self.password)
            self.db = client[self.uri.split('/')[-1]]  # 这种写法不通用
            self.cli = client
        except Exception as e:
            print("数据库连接错误！")
            return None
        return self.db

    def close(self):
        self.cli.close()
