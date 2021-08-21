# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2020/12/3 14:07
# # @Author  : cendeavor
# # @File    : views.py
# # @Software: PyCharm
#
# from app.forms import NameForm
# from app.service.tag_service import TagService
# from app.service.data_service import DataService
# from app.dto import Response
# from flask import request, render_template, jsonify, flash, redirect, url_for
from . import demo
#
# data_service = DataService()
# # symptoms_meta = data_service.get_data(cname='symptoms')
# tag_service = TagService()
# data_gen = None
#
#
# @main.route('/test', methods=['GET', 'POST'])
# def test():
#     return render_template('/main/test.html')
#
#
# @main.route('/', methods=['GET', 'POST'])
# def index():
#     """ 首页
#
#     Returns:
#
#     """
#     form = NameForm()
#     if form.validate_on_submit():
#         participant = form.name.data
#         form.name.data = ''
#         tag_service.register(participant)
#         global data_gen
#         data_gen = tag_service.generate_data()
#         return redirect(url_for('main.next_user'))
#     return render_template('/main/index.html', form=form)
#
#
# @main.route('/next', methods=['GET'])
# def next_user():
#     """ 标注下一个
#
#     Returns:
#
#     """
#     try:
#         data = next(data_gen)
#         # data_service.save_page_data(data)  # 保存当前页的状态，用作刷新
#     except Exception as e:
#         return render_template('/main/restart.html', stats=tag_service.stat_workload())  # todo: test this line
#     user_link = data['user_homepage']
#     tweets = data['tweets']
#     symptoms = data_service.get_data(cname='symptoms')
#     statistics = data['statistics']
#     return render_template('/main/tagging.html', user_link=user_link, tweets=tweets, symptoms=symptoms,
#                            stats=statistics,
#                            auto_detect=['insomnia'])
#
#
# @main.route('/tag', methods=['GET', 'POST'])
# def tag():
#     """ 打标
#
#     Returns:
#
#     """
#     data = request.get_json()
#     print(data)
#     # TODO: 系统自动根据规则判别（tag_service）
#     res = tag_service.tag(data)
#     return jsonify(Response.success('打标成功', res))
#
#     # if data:
#     #     flash(u'打标成功', 'success')  # 只有当页面重新渲染后才能够
#     # else:
#     #     flash(u'数据录入失败', 'error')
#     # res = data_service.recover_page_data()
#     # user_link = res['user_homepage']
#     # tweets = res['tweets']
#     # symptoms = data_service.get_data(cname='symptoms')
#     # return render_template('/main/tagging.html', user_link=user_link, tweets=tweets, symptoms=symptoms,
#     #                        auto_detect=['insomnia'])
#
# # 添加任务
# # @main.route("/home/add/task", methods=["GET", "POST"])
# # def add_task():
# #     res = Response.error(code=500, msg="System Internal Error!")
# #     params = request.json
# #     if params and params.get("url"):
# #         res = Response.success(msg="创建任务成功")
# #     return jsonify(res)
