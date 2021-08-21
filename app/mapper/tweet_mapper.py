#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 14:45
# @Author  : cendeavor
# @File    : tweet_mapper.py
# @Software: PyCharm

import re
from app.mapper.basic_mapper import BasicMapper
from conf.settings import mapper_config

config = mapper_config.get('tweet')
cname = config['CNAME']

class TweetMapper(BasicMapper):

    @staticmethod
    def get_user_tweets(db, user_id):
        """ 翻译症状

        Returns:

        """
        data = db[cname].find({"user_id": int(user_id)})
        tweets = []
        ids_seen = set([])
        for item in data:
            if item['tweet_id'] in ids_seen:
                continue
            else:
                ids_seen.add(item['tweet_id'])
            content = item["content"]["tweet_content"]
            content = re.sub("\u200b", "", content)
            # content = re.sub("#.*#", "", content)
            item["content"]["tweet_content"] = content.strip()
            tweets.append(item["content"])
        return tweets


if __name__ == '__main__':
    from database import MongoDBC
    from pprint import pprint

    dbc = MongoDBC()
    db = dbc.connect()
    pprint(TweetMapper.get_user_tweets(db, 1001352815))
    dbc.close()
