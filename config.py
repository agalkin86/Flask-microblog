import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
    # настройка безовасности для форм
    SECRET_KEY = os.environ.get('SECRET_KEY_FLASK') or 'you-will-never-guess'

    # настройки подключения к БД
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_FLASK') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # настройки для отправки ошибок на email
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['galkinandrey86@gmail.com']

    # настройки элементов на странице
    POSTS_PER_PAGE = 20