# coding: utf-8

from . import app
from flask import render_template


@app.route('/test')
def test():
	return "<h1>this is a test!</h1>"


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/logout')
def logout():
	return render_template('logout.html')


@app.route('/index')
def doube():
	return render_template('doube.html')
