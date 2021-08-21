#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 14:32
# @Author  : cendeavor
# @File    : basic_mapper.py
# @Software: PyCharm


class BasicMapper:

    @staticmethod
    def stats_collection(db, cname, key=None):
        """集合统计函数
            返回集合的一些基本统计数据，比如count之类
        Args:
            db: 目标数据库
            cname: 目标集合名
            key: 用于筛选的键值名（考虑后面改成condition字典形式）

        Returns:
            stats: 关于集合的一些统计数据

        """
        stats = {
            'total': db[cname].count(),
            'unique': {},
        }
        if key:
            stats['unique'][key] = len(db[cname].distinct(key))
        print(stats)
        return stats
