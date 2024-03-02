from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired


# Форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Обязательное поле')])
    email = EmailField('Почта', validators=[DataRequired('Обязательное поле')])
    password = PasswordField('Введите пароль', validators=[DataRequired('Обязательное поле')])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired('Обязательное поле')])
    confirm = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Обязательное поле')])
    password = PasswordField('Введите пароль', validators=[DataRequired('Обязательное поле')])
    confirm = SubmitField('Войти')
