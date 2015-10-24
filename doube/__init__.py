# coding: utf-8

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

basedir = os.path.abspath(os.path.dirname(__name__))


app = Flask(__name__)
app.config['SECRET_KEY'] = "I hate flask!"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "doube.sqlite")
app.config['UPLOAD_FOLDER'] = "/root/hackday/DouBe/doube/static/upload/"
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


from . import views, models, forms
