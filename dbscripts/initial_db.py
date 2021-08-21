#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 20:26
# @Author  : cendeavor
# @File    : initial_db.py
# @Software: PyCharm

from database import MongoDBC
from conf.settings import DevelopmentConfig
import warnings

warnings.filterwarnings('ignore')


def main():
    dbc = MongoDBC(DevelopmentConfig.MONGO_URI)
    db = dbc.connect()
    collection = db['symptoms']
    collection.update({"_id": 1}, {"$set": {
        "english_name": "self_reported",
        "chinese_name": "自述患抑郁",
        "type": 3,  # 最高级别
        "description": "发出医院开出的诊断为抑郁症病历",
        "keywords": ["抑郁", "舍曲林", "度洛西汀", "文拉法辛", "吃药", "医生"]
    }}, upsert=True)
    collection.update({"_id": 2}, {"$set": {
        "english_name": "interest_loss",
        "chinese_name": "兴致下降",
        "type": 2,  # 核心
        "description": "对几乎所有活动兴趣消退",
        "keywords": ["兴趣", "没意思", "无精打采", "厌世", "动力"]  # "没兴趣"
    }}, upsert=True)
    collection.update({"_id": 3}, {"$set": {
        "english_name": "pleasure_loss",
        "chinese_name": "快感消失",
        "type": 2,  # 核心
        "description": "长时间开心不起来，没有愉悦感",
        "keywords": ["不开心", "不高兴", "不快乐", "郁闷", "压抑", "难熬", "消沉", "低落", '丧']
    }}, upsert=True)
    collection.update({"_id": 4}, {"$set": {
        "english_name": "energy_loss",
        "chinese_name": "疲乏",
        "type": 1,  # DSM-5
        "description": "乏力，经常性疲惫，没有精神",
        "keywords": ["累", "没力气", "发软", "躺", "困", "昏", "晕"]
    }}, upsert=True)
    collection.update({"_id": 5}, {"$set": {
        "english_name": "sadness",
        "chinese_name": "悲伤",
        "type": 1,  # DSM-5
        "description": "经常无故感到伤感",
        "keywords": ["哭", "伤心", "难受", "痛苦", "惆怅", "难过"]
    }}, upsert=True)
    collection.update({"_id": 6}, {"$set": {
        "english_name": "sympathetic_arousal",
        "chinese_name": "交感神经唤醒",
        "type": 0,  # None-DSM-5
        "description": "心悸、颤抖、视力模糊、冒冷汗",
        "keywords": ["心悸", "颤抖", "模糊", "冒汗", "冷汗", "胸闷", "心慌"]
    }}, upsert=True)
    collection.update({"_id": 7}, {"$set": {
        "english_name": "concentration_problem",
        "chinese_name": "注意力下降",
        "type": 1,  # DSM-5
        "description": "可能出现精神恍惚",
        "keywords": ["注意力", "不集中"]
    }}, upsert=True)
    collection.update({"_id": 8}, {"$set": {
        "english_name": "panic",
        "chinese_name": "恐慌",
        "type": 0,  # None-DSM-5
        "description": "经常无故感到害怕",
        "keywords": ["好怕", "恐惧", "恐慌", "害怕"]  # 怕
    }}, upsert=True)
    collection.update({"_id": 9}, {"$set": {
        "english_name": "appetite_problem",
        "chinese_name": "食欲问题",
        "type": 1,  # DSM-5
        "description": "经常没胃口、呕吐或不明原因暴饮暴食",
        "keywords": ["吐", "没胃口", "饱", "暴食"]
    }}, upsert=True)
    collection.update({"_id": 10}, {"$set": {
        "english_name": "insomnia",
        "chinese_name": "失眠",
        "type": 1,  # DSM-5
        "description": "自述经常失眠、凌晨0-6点发帖时间较多",
        "keywords": ["安眠药", "失眠", "睡不着"]
    }}, upsert=True)
    collection.update({"_id": 11}, {"$set": {
        "english_name": "anxious",
        "chinese_name": "焦虑",
        "type": 0,  # None-DSM-5
        "description": "经常感到焦躁不安，包含了紧张、过度担心",
        "keywords": ["焦虑", "紧张", "担心", "紧绷", "喘不过气", "忐忑"]
    }}, upsert=True)
    collection.update({"_id": 12}, {"$set": {
        "english_name": "self_blame",
        "chinese_name": "自责",
        "type": 1,  # DSM-5
        "description": "感到愧疚或没有价值",
        "keywords": ["对不起", "没用", "一无是处", "不中用", "自我否定", "一事无成", "孤独"]  # "错",
    }}, upsert=True)
    collection.update({"_id": 13}, {"$set": {
        "english_name": "retardation",
        "chinese_name": "反应迟钝",
        "type": 1,  # DSM-5
        "description": "反应不敏捷，对疼痛不敏感",
        "keywords": ["麻木", "笨"]  # "慢",
    }}, upsert=True)
    collection.update({"_id": 14}, {"$set": {
        "english_name": "suicidal_ideation",
        "chinese_name": "自杀倾向",
        "type": 1,  # DSM-5
        "description": "重复地想到死亡，重复地想到自杀但是没有详细计划，自杀尝试或者明确的自杀计划",
        "keywords": ["自杀", "结束", "死", "自残"]
    }}, upsert=True)
    collection.update({"_id": 15}, {"$set": {
        "english_name": "weight_problem",
        "chinese_name": "体重骤变",
        "type": 1,  # DSM-5
        "description": "",
        "keywords": ["变重", "变轻"]  # "肥", "瘦"
    }}, upsert=True)
    collection.update({"_id": 16}, {"$set": {
        "english_name": "agitation",
        "chinese_name": "狂躁",
        "type": 1,  # DSM-5
        "description": "生理性躁动，言语偏激、易怒",
        "keywords": ["烦", "抓狂", "冲动", "易怒"]
    }}, upsert=True)
    collection.update({"_id": 17}, {"$set": {
        "english_name": "hypersomnia",
        "chinese_name": "嗜睡",
        "type": 1,  # DSM-5
        "description": "",
        "keywords": ["懒", "起床", "嗜睡", "睡不醒"]
    }}, upsert=True)
    dbc.close()


if __name__ == '__main__':
    main()
