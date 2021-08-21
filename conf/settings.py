#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/24 21:47
# @Author  : cendeavor
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOUR_SECRET'

    # ITEMS_PER_PAGE = 10
    # JWT_AUTH_URL_RULE = '/api/auth'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_USERNAME = 'YOUR_USERNAME'
    MONGO_PASSWORD = 'YOUR_PASSWORD'
    MONGO_HOST = 'YOUR_IP'
    MONGO_PORT = 'YOUR_PORT'
    MONGO_DATABASE = 'YOUR_DBNAME'
    MONGO_URI = "mongodb://{0}:{1}@{2}:{3}/{4}".format(
        MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT, MONGO_DATABASE
    )
    # DATABASE_URI = os.getenv('DEV_DATABASE_URI', MONGO_URI)


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    PRODUCTION = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

mapper_config = {
    'symptom': {
        'CNAME': 'symptoms'
    },
    'tweet': {
        'CNAME': 'tweet_1'
    },
    'state': {
        'CNAME': 'tag_state',
        'CID': 1,
        'MIN_WEIBO_CNT': 50,
        'MAX_WEIBO_CNT': 500,
    }
}