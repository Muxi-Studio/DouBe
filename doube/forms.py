# coding: utf-8


from .models import User
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import Required, Length, EqualTo
from wtforms import ValidationError


class LoginForm(Form):
    """登录表单类"""
    username = StringField('用户名', validators=[Required(), Length(1, 64)])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegisterForm(Form):
    """注册表单类"""
    username = StringField('用户名', validators=[Required(), Length(1, 64)])
    password1 = PasswordField('密码', validators=[Required(), EqualTo('password2', message="密码必须匹配")])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_username(self, field):
        """确定该用户名没有被注册"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已经被注册')
