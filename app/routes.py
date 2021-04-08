# -*- coding: utf-8 -*-
from app import blog
from flask import render_template

@blog.route('/')
@blog.route('/index')
def index():
    user = {'username': 'Andrey'}
    return render_template('index.html', title='Home', user=user) # user=user['username'] / {{user}}