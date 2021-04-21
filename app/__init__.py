from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler,RotatingFileHandler
import os

blog = Flask(__name__)
blog.config.from_object(Config)
db = SQLAlchemy(blog)
migrate = Migrate(blog,db)
login = LoginManager(blog)
login.login_view = 'login'

if not blog.debug:
    if blog.config['MAIL_SERVER']:
        auth = None
        if blog.config['MAIL_USERNAME'] or blog.config['MAIL_PASSWORD']:
            auth = (blog.config['MAIL_USERNAME'], blog.config['MAIL_PASSWORD'])
        secure = None
        if blog.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(blog.config['MAIL_SERVER'], blog.config['MAIL_PORT']),
            fromaddr='no-reply@' + blog.config['MAIL_SERVER'],
            toaddrs=blog.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        blog.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    blog.logger.addHandler(file_handler)
    blog.logger.setLevel(logging.INFO)
    blog.logger.info('Microblog startup')

from app import routes, models, errors