# coding: utf-8

# 用户数据表
# 逗比数据表
# 用户数据表属性
#		id  username password_hash doube dou
# 逗比数据表属性
#		id doube author_id dou(redis)


from . import db
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    """用户类"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(168))
    avatar = db.Column(db.Text)  # url
    doube = db.relationship('Doube', backref="author", lazy='dynamic')


    @property
    def password(self):
        """将password设置为属性
           读取密码原始值时报错"""
        raise AttributeError('无法读取密码原始值')

    @password.setter
    def password(self, password):
        """设置密码散列值"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """通过比对散列值验证密码"""
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        """根据用户的id加载用户
		   flask-login的验证回调函数"""
        return User.query.get(int(user_id))

    def __repr__(self):
        return '<user %r>' % self.username


class Doube(db.Model):
    """逗比类哈哈哈哈
	   用户头像, 文字论述, 图片"""
    __tablename__ = 'doubes'
    id = db.Column(db.Integer, primary_key=True)
	# title = db.Column(db.Text)
    body = db.Column(db.Text)  # body 中包含图片
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    dou = db.Column(db.Integer)  # 逗赞

    def __repr__(self):
        return '<%r is a Doube hahaha>' % self.title
