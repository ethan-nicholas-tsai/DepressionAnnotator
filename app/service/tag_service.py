#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 10:56
# @Author  : cendeavor
# @File    : tag_service.py
# @Software: PyCharm

from app.factory import mongo
from app.utils.general import get_cur_time, cardinal_time
from app.mapper.symptom_mapper import SymptomMapper
from app.mapper.state_mapper import StateMapper
from app.mapper.tweet_mapper import TweetMapper
import time


class TagService:

    def __init__(self):
        self.db = mongo.db
        # symptom
        self.symptom_chinese = SymptomMapper.get_symptoms_translation(self.db)
        self.symptom_meta = SymptomMapper.get_symptoms_meta(self.db)
        # state
        self.participant = []
        self.stats = {}

    def register(self, participant):
        """ 登记打标人

        Args:
            participant:

        Returns:

        """
        self.participant.append(participant)
        self.stats[participant] = {
            "todo_cur": StateMapper.stats_all(self.db)["total"],
            "done_cur": -1,
            "past_tag_num": StateMapper.stats_participant(self.db, participant)["past_tag_num"],
            "time_start": time.time(),
            "time_end": 0
        }

    def stat_workload(self, participant):
        """ 统计用户的打标情况

        Returns:

        """
        user_stats = self.stats[participant]
        user_stats['done_cur'] += 1
        user_stats['time_end'] = time.time()
        return {
            "todo_cur": StateMapper.stats_all(self.db)["total"],
            "done_cur": user_stats['done_cur'],
            "done_total": user_stats['past_tag_num'] + user_stats['done_cur'],
            "work_time": cardinal_time(user_stats['time_start'], user_stats['time_end'])
        }

    def generate_data(self):
        """ 生成打标数据

        Returns:

        """
        states = StateMapper.find_all(self.db)
        for item in states:
            user_id = item['_id']
            item['user_homepage'] = "https://weibo.com/u/" + user_id + "?is_all=1"
            tweets = TweetMapper.get_user_tweets(self.db, user_id)
            if not tweets:
                self.db['tag_state'].update_one({'_id': str(user_id)}, {"$set": {"is_depression": 'NAN'}}, upsert=True)
            else:
                time_tag_tweets = []
                content_tag_tweets = []
                no_tag_tweets = []
                retweets = []
                late_num = 0
                for tweet in tweets:
                    tweet['tweet_content'] = self.auto_tag_tweet(tweet['tweet_content'])
                    tweet['post_time'] = self.auto_tag_time(tweet['post_time'])
                    # 将有关键字识别的推文放在前面
                    # if "转发微博" in tweet['tweet_content']:
                    if not tweet["is_origin"]:
                        retweets.append(tweet)
                        if "</mark>" in tweet['post_time']:  # 转发贴中也有深夜贴，也要计算！
                            late_num += 1
                    elif "</mark>" in tweet['post_time']:
                        time_tag_tweets.append(tweet)
                        late_num += 1
                    elif "</mark>" in tweet['tweet_content']:
                        content_tag_tweets.append(tweet)
                    else:
                        no_tag_tweets.append(tweet)
                # 一般晚上发丧的多一点
                item["tweets"] = content_tag_tweets + time_tag_tweets + no_tag_tweets  # + retweets
                # 统计数据
                public_num = len(time_tag_tweets + content_tag_tweets + no_tag_tweets + retweets)
                item["tweet_stats"] = {
                    "total_num": item["total_num"],
                    "public_num": public_num,
                    "private_num": item["total_num"] - public_num,
                    "late_num": late_num,
                    "retweet_num": len(retweets),
                    "late_proportion": int(late_num / public_num * 100),
                    "retweet_proportion": int(len(retweets) / public_num * 100),
                    "private_proportion": int((item["total_num"] - public_num) / item["total_num"] * 100)
                }
                # self.stats['todo'] -= 1
                yield item

    def auto_tag_tweet(self, content):
        for symptom in self.symptom_meta:
            for keyword in symptom['keywords']:
                content = content.replace(keyword,
                                          '<mark data-entity="{}">{}</mark>'.format(symptom['_id'], keyword))  # acronym
        return content

    @staticmethod
    def auto_tag_time(post_time):
        day_time = post_time.split(" ")[-1]
        if "00:00" <= day_time < "06:00":
            post_time = post_time.replace(day_time, '<mark data-entity="{}">{}</mark>'.format(10, day_time))
        return post_time

    def tag(self, participant, data):
        """ 打标函数

        Returns:

        """
        result = self.judge(data)
        update_data = {
            "_id": data['user_id'],
            "self_reported": data['self_reported'],
            "symptoms": data['symptoms'],
            "is_depression": result,
            "tag_time": get_cur_time(),
            "participant": participant,
            "manual_judges": data['manual_judges']  # 人工判断
        }
        # 更新数据库
        StateMapper.update_one(self.db, update_data)
        # 返回判别结果
        symptom_summary = ""
        if data['self_reported']:
            symptom_summary = "自述抑郁症"
        else:
            for symptom, state in data['symptoms'].items():
                if state:
                    symptom_summary += self.symptom_chinese[symptom] + ', '
        return {
            "symptom_summary": symptom_summary,
            "result": "抑郁" if result else "正常"
        }

    @staticmethod
    def judge(data):
        if data["self_reported"]:
            return True
        else:
            symptoms = data['symptoms']
            cnt = 0
            for symptom, state in symptoms.items():
                if state:
                    cnt += 1
            if (symptoms['interest_loss'] or symptoms['pleasure_loss']) and cnt >= 5:
                return True
            else:
                return False


if __name__ == '__main__':
    pass
