#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 14:28
# @Author  : cendeavor
# @File    : symptom_mapper.py
# @Software: PyCharm

from app.mapper.basic_mapper import BasicMapper
from conf.settings import mapper_config

config = mapper_config.get('symptom')
cname = config['CNAME']

class SymptomMapper(BasicMapper):

    @staticmethod
    def get_symptoms_translation(db):
        """ 翻译症状

        Returns:

        """
        data = db[cname].find({})
        symptoms = {}
        for item in data:
            symptoms[item['english_name']] = item['chinese_name']
        return symptoms

    @staticmethod
    def get_symptoms_meta(db):
        data = db[cname].find({})
        symptoms = []
        for item in data:
            symptoms.append(item)
        return symptoms


if __name__ == '__main__':
    from database import MongoDBC

    dbc = MongoDBC()
    db = dbc.connect()
    print(SymptomMapper.get_symptoms_meta(db))
    print(SymptomMapper.get_symptoms_translation(db))
    dbc.close()
