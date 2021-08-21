from flask import Flask
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_pymongo import PyMongo
import os

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]

bootstrap = Bootstrap()
csrf = CSRFProtect()
mongo = PyMongo()


def create_app(app_name=PKG_NAME, **kwargs):
    app = Flask(app_name)  # ,
    # static_folder='app/static',
    # template_folder='app/templates')  # app = Flask(app_name, instance_path="")

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    # 从环境变量获取配置名，如果环境变量不存在，则使用缺省值'default'
    config_name = os.getenv('FLASK_CONFIGURATION', default='default')

    # 添加配置
    from conf.settings import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 应用 flask-bootstrap
    bootstrap.init_app(app)

    # 应用 flask-wtf
    csrf.init_app(app)

    # 应用 flask-pymongo
    mongo.init_app(app)

    # # 登录管理
    from . import login_manager
    login_manager.init_app(app)

    # 注册蓝本
    from app.controller.demo import demo as demo_blueprint
    app.register_blueprint(demo_blueprint, url_prefix='/demo')  # , url_prefix='/home')

    from app.controller.main import main as main_blueprint
    app.register_blueprint(main_blueprint)  # , url_prefix='/home')

    from app.controller.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.controller.ops import ops as ops_blueprint
    app.register_blueprint(ops_blueprint, url_prefix='/ops')

    return app
