#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:06
# @Author  : cendeavor
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

demo = Blueprint('demo', __name__)

from . import views
