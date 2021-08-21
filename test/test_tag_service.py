#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 21:26
# @Author  : cendeavor
# @File    : test_tag_service.py
# @Software: PyCharm

from pprint import pprint
from app.service.tag_service import TagService


def main():
    tag_service = TagService()
    tag_service.register('cendeavor')
    data_gen = tag_service.generate_data()

    cnt = 0
    for data in data_gen:
        cnt += 1
        if not cnt % 3:
            break
        pprint(data)


if __name__ == '__main__':
    main()
