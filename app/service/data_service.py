#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 21:18
# @Author  : cendeavor
# @File    : data_service.py
# @Software: PyCharm

from app.factory import mongo


class DataService:

    def __init__(self):
        self.db = mongo.db
        self.page_data = None

    def get_data(self, cname):
        """ 生成打标数据

        Returns:

        """
        data = []
        for item in self.db[cname].find():
            data.append(item)
        return data

    def save_page_data(self, data):
        """ 保存当前页的临时数据

        Args:
            data:

        Returns:

        """
        self.page_data = data

    def recover_page_data(self):
        """ 恢复当前页的数据

        Returns:

        """
        return self.page_data


if __name__ == '__main__':
    pass
