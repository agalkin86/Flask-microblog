from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
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


class EditProfileForm(FlaskForm):
    username = StringField('Username/Пользователь', validators=[DataRequired()])
    about_me = TextAreaField('About me/Обо мне', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit/Сохранить')

    def __init__(self,original_username,*args,**kwargs):
        super(EditProfileForm, self).__init__(*args,**kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.original_username).first()
            if user is not None:
                raise ValidationError('Please use a different username/Пожалуйста, используйте другое имя пользователя')