from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username/Пользователь', validators=[DataRequired()])
    password = PasswordField('Password/Пароль',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me/Запомнить меня')
    submit = SubmitField('Sign In/Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Username/Пользователь', validators=[DataRequired()])
    email = StringField('Email/Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Password/Пароль', validators=[DataRequired()])
    password2 = PasswordField('Repeat password/Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register/Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username./Пожалуйста, используйте другое имя пользователя.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address./Пожалуйста, используйте другой адрес электронной почты.')