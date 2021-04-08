# -*- coding: utf-8 -*-
from app import blog

@blog.route('/')
@blog.route('/index')
def index():
    user = {'username':'Andrey'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>
    '''