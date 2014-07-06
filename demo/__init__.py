# coding=utf-8
__author__ = 'tech.chao'

from flask import Flask

app = Flask(__name__)
#: 配置项目域名, 作为Flask的ServerName
app.config['SERVER_NAME'] = 'xyz.com'
#: 指定该域名中默认的子域名
app.url_map.default_subdomain = 'www'


from demo.main import main_app
from demo.sub import sub_app

#: 注册蓝图(BluePrint)
app.register_blueprint(main_app)
app.register_blueprint(sub_app)