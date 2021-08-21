#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 15:28
# @Author  : cendeavor
# @File    : state_mapper.py
# @Software: PyCharm

from app.mapper.basic_mapper import BasicMapper
from conf.settings import mapper_config

config = mapper_config.get('state')
cname = config['CNAME']
cid = config['CID']
min_num = config['MIN_WEIBO_CNT']
max_num = config['MAX_WEIBO_CNT']


class StateMapper(BasicMapper):

    @staticmethod
    def find_all(db):
        """ 翻译症状

        Returns:

        """
        return db[cname].find({"is_depression": -1, "total_num": {"$gte": min_num, "$lte": max_num}, "cid": cid},
                              no_cursor_timeout=True)

    @staticmethod
    def update_one(db, item):
        db[cname].update({"_id": item["_id"]}, {"$set": item}, upsert=True)

    @staticmethod
    def stats_all(db):
        # statistics
        total = db[cname].find(
            {"is_depression": -1, "total_num": {"$gte": min_num, "$lte": max_num}, "cid": cid}
        ).count()
        stats = {
            "total": total,
            "todo": total
        }
        return stats

    @staticmethod
    def stats_participant(db, participant):
        stats = {"past_tag_num": db[cname].find({"participant": participant}).count()}
        return stats

    @staticmethod
    def renew(db):
        db[cname].update_many({}, {
            '$set': {'is_depression': -1, "participant": "", "tag_time": "", "self_reported": "",
                     "symptoms": {
                         "interest_loss": "",
                         "pleasure_loss": "",
                         "energy_loss": "",
                         "sadness": "",
                         "sympathetic_arousal": "",
                         "concentration_problem": "",
                         "panic": "",
                         "appetite_problem": "",
                         "insomnia": "",
                         "anxious": "",
                         "self_blame": "",
                         "retardation": "",
                         "suicidal_ideation": "",
                         "weight_problem": "",
                         "hypersomnia": ""
                     }}}, upsert=True)


if __name__ == '__main__':
    from database import MongoDBC

    dbc = MongoDBC()
    db = dbc.connect()
    data_gen = StateMapper.find_all(db)
    for item in data_gen:
        print(item["_id"])
        label = input("label: ")
        item['is_depression'] = label
        StateMapper.update_one(db, item)
    # StateMapper.renew(db)
    dbc.close()
