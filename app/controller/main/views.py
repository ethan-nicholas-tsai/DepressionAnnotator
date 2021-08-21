#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:07
# @Author  : cendeavor
# @File    : views.py
# @Software: PyCharm

from app.service.tag_service import TagService
from app.service.data_service import DataService
from app.dto import Response
from flask import request, render_template, jsonify, flash, redirect, url_for
from flask_login import current_user, login_required, logout_user
from . import main

data_service = DataService()
symptoms = data_service.get_data(cname='symptoms')
tag_service = TagService()
data_gen = None


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """ 首页

    Returns:

    """
    tag_service.register(participant=current_user.username)
    global data_gen
    if not data_gen:  # 加上这句，不会重复打标；但是会遗漏打标。。为了工作量统计方便，还是加吧，大不了每晚重启
        data_gen = tag_service.generate_data()
    return redirect(url_for('main.next_user'))


@main.route('/next', methods=['GET'])
@login_required
def next_user():
    """ 标注下一个

    Returns:

    """
    try:
        data = next(data_gen)
    except Exception as e:
        return redirect(url_for("main.next_user"))
        # return render_template('/main/finish.html', stats=tag_service.stat_workload(
        #     participant=current_user.username))  # todo: test this line
    user_link = data['user_homepage']
    tweets = data['tweets']
    statistics = tag_service.stat_workload(participant=current_user.username)
    tweet_stats = data['tweet_stats']
    return render_template('/main/tagging.html', user_id=data['_id'], user_link=user_link, tweets=tweets,
                           symptoms=symptoms,
                           stats=statistics, tweet_stats=tweet_stats,
                           auto_detect=['insomnia'])


@main.route('/tag', methods=['GET', 'POST'])
@login_required
def tag():
    """ 打标

    Returns:

    """
    data = request.get_json()
    print(data)
    # TODO: 系统自动根据规则判别（tag_service）
    res = tag_service.tag(participant=current_user.username, data=data)
    return jsonify(Response.success('打标成功', res))


@main.route('/diagnosis-rules', methods=['GET', 'POST'])
@login_required
def rules():
    """ 打标

    Returns:

    """
    return render_template('/main/rules.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@main.route('/restart')
def restart():
    return render_template('/ops/restart.html')
