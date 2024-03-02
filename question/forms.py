from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


# Форма для добавления комментария
class CommentForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired('Обязательное поле')])
    title = StringField('Заголовок', validators=[DataRequired('Обязательное поле')])
    comment = TextAreaField('Придумайте коммент', validators=[DataRequired('Обязательное поле')])
    confirm = SubmitField('Отправить')
