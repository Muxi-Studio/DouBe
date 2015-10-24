# coding: utf-8

from . import app, db
from flask import render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from .models import User
from flask.ext.login import login_user, logout_user, login_required


# @app.route('/test')
# def test():
# return "<h1>this is a test!</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('user'))
        flash('该用户不存在')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已登出!')
    return redirect(url_for('index'))


@app.route('/register')
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		u = User(
			username = form.username.data,
			password = form.password1.data
		)
		db.session.add(u)
		db.session.commit()
	return render_template('register.html', form=form)


@app.route('/index')
def doube():
	return render_template('doube.html')
