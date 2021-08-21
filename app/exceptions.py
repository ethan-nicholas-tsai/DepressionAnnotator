#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 22:07
# @Author  : cendeavor
# @File    : exceptions.py
# @Software: PyCharm


class SigtermException(Exception):
    pass


def sigterm_handler(signum, frame):
    print('SIGTERM')
    raise SigtermException  # 将 SIGTERM 信号转化为 SigtermException 异常
