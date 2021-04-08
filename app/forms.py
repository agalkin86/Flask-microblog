from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username/Пользователь', validators=[DataRequired()])
    password = PasswordField('Password/Пароль',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me/Запомнить меня')
    submit = SubmitField('Sign In/Войти')