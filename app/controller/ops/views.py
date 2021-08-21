#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:07
# @Author  : cendeavor
# @File    : views.py
# @Software: PyCharm

import requests
from . import ops


@ops.route('/restart', methods=['GET', 'POST'])
def restart():
    ret = requests.get("http://120.79.102.245:5001")
    # print(ret.text)
    return ret.text
