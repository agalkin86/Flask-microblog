# -*- coding: utf-8 -*-
from app import blog
from flask import render_template

@blog.route('/')
@blog.route('/index')
def index():
    user = {'username': 'Galkin Andrey'}
    return render_template('index.html', titel='Home', user=user) # user=user['username'] / {{user}}