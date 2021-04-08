# -*- coding: utf-8 -*-
from app import blog
from flask import render_template

@blog.route('/')
@blog.route('/index')
def index():
    user = {'username': 'Андрей Галкин'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
            }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) # user=user['username'] / {{user}}