# coding=utf-8
__author__ = 'tech.chao'

from flask import Blueprint
from flask import render_template

sub_app = Blueprint('sub', __name__, static_folder='static',
                    template_folder='templates', subdomain='sub')


@sub_app.route('/')
def sub_index():
    return render_template('sub_index.html', content='Hello Sub App!')