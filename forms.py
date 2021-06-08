from wtforms import StringField, TextAreaField, SelectField, FileField, SubmitField, IntegerField, BooleanField, PasswordField
from wtforms.validators import Required, DataRequired
from flask_wtf import FlaskForm, Form
from flask_ckeditor import CKEditorField

from app import app



class NewEatForm(FlaskForm):
    name = StringField('Название нового блюда')
    body = CKEditorField('Описание блюда', validators=[DataRequired()])
    price = IntegerField('Стоимость блюда')
    tipe = SelectField('Выбери категорию блюда', choices = [('p', 'Пицца'), ('r', 'Роллы')])
    image = FileField('Выбрать фото')

class NewUserForm(FlaskForm):
    name = StringField('Имя')
    email = StringField('email')
    phone = IntegerField('телефон')
    password = PasswordField('Пароль')
    checkbox = BooleanField('Оставаться в системе')

class FormAutent(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')

class News(FlaskForm):
    body = CKEditorField('Статья', validators=[DataRequired()])
    submit = SubmitField('Oтправить')

    

class Authorization(FlaskForm):
    body = IntegerField('код подтверждения')
