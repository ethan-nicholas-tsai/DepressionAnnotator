#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 19:25
# @Author  : cendeavor
# @File    : general.py
# @Software: PyCharm

from dateutil import rrule
from datetime import datetime
import time


def get_cur_time():
    # 获取日期，格式化yyyy-mm-dd hh:mm:ss
    # 第一种方式
    strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # print(strtime)
    return strtime
    # 输出：2019-01-08 16:44:08
    # 输出：<class 'str'>


def cardinal_time(time_start, time_end):
    seconds = time_end - time_start
    s = int(seconds % 60)
    m = int((seconds / 60) % 60)
    h = int(seconds / 60 / 60)
    return "{} h {} m {} s".format(h, m, s)
