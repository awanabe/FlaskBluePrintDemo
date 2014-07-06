# coding=utf-8
__author__ = 'tech.chao'

from flask import Blueprint
from flask import render_template

main_app = Blueprint('main', 'main', static_folder='demo/main/static',
                     template_folder='demo/main/templates', subdomain='www')


@main_app.route('/')
def main_index():
    return render_template('main_index.html', content='Hello Main App!')