# coding=utf-8
__author__ = 'tech.chao'

from flask import Flask

app = Flask(__name__)
app.config['SERVER_NAME'] = 'xyz.com'

app.url_map.default_subdomain = 'www'


from demo.main import main_app
from demo.sub import sub_app

app.register_blueprint(main_app)
app.register_blueprint(sub_app)