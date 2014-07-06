# coding=utf-8
__author__ = 'tech.chao'

from flask import Blueprint
from flask import render_template

#: 初始化Main蓝图. 注意静态文件和模板文件夹路径
#: 模板路径是 root_path + template_folder
#: root_path 是 FlaskBluePrintDemo的路径
main_app = Blueprint('main', 'main', static_folder='demo/main/static',
                     template_folder='demo/main/templates', subdomain='www')


@main_app.route('/')
def main_index():
    return render_template('main_index.html', content='Hello Main App!')