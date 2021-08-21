# from conf.config import Config, config
from flask_login import LoginManager
import logging, os

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
# 设置当未登录用户请求一个只有登录用户才能访问的视图时，闪现的错误消息的内容，
# 默认的错误消息是：Please log in to access this page.。
login_manager.login_message = 'Unauthorized User'
# 设置闪现的错误消息的类别
login_manager.login_message_category = "info"

# USE: 对logging进行个性化配置
basedir = "/home/cyc/Code/Privacy_Guardian"
# from logging.config import fileConfig
#
# # fileConfig('conf/log-app.conf')
# fileConfig(os.path.join(basedir, 'conf/log-app.conf'))


def get_logger(name):
    return logging.getLogger(name)


def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))


# def get_config():
#     return config[os.getenv('FLASK_CONFIG') or 'default']
