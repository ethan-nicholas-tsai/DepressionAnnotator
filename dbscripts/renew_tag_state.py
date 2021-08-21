#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 21:44
# @Author  : cendeavor
# @File    : renew_tag_state.py
# @Software: PyCharm

from database import MongoDBC
import time


def main():
    dbc = MongoDBC()
    db = dbc.connect()
    begin = time.time()
    db['all'].update_many({}, {'$set': {'is_depression': -1, "participant": "", "tag_time": "", "self_reported": "",
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
    times = time.time() - begin
    print(times)


if __name__ == '__main__':
    main()
