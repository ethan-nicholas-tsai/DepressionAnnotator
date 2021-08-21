#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 21:34
# @Author  : cendeavor
# @File    : test_data_service.py
# @Software: PyCharm


from pprint import pprint
from app.service.data_service import DataService


def main():
    data_service = DataService()
    symptom_chinese = data_service.get_symptoms_translation()
    pprint(symptom_chinese)
    print("*" * 15)
    symptom_meta = data_service.get_symptoms_meta()

    for symptom in symptom_meta:
        pprint(symptom)


if __name__ == '__main__':
    main()
