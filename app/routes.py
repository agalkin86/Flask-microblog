# -*- coding: utf-8 -*-
from app import blog

@blog.route('/')
@blog.route('/index')
def index():
    return "Привет, мир!"
