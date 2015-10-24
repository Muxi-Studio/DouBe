# coding: utf-8

import os
from . import app, db
from flask import render_template, redirect, url_for, flash, \
		request, session
from .forms import LoginForm, RegisterForm, DouZan, \
		NewDoube
from .models import User, Doube
from flask.ext.login import login_user, logout_user, login_required, \
		current_user
from werkzeug import secure_filename


# 允许上传至服务器的文件集合
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	"""检查文件扩展名是否符合标准"""
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


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
            return redirect(url_for('doube'))
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


@app.route('/index', methods=["GET", "POST"])
def doube():
	"""
	趣味生活，就是要比
		比逗榜: 依据[逗]的个数进行排序
		鲜逗: 依据时间进行排序
		逗赞: 点赞
	"""
	douzan = DouZan()  # 逗赞按钮
	form = NewDoube()  # 创建逗文
	new_dou = []  # 鲜逗
	best_dou = []  # 比逗榜

	new_dou = Doube.query.order_by('-id').all()
	best_dou = Doube.query.order_by(Doube.dou)[:6:-1]  # 默认显示5个

	# 逗赞功能
	# /doube?doube=id
	# 并没有使用ajax
	# /doube?upload=True
	if request.method == 'POST':
		if request.args.get('doube'):
			id = request.args.get('doube')
			doube = Doube.query.filter_by(id=id).first()
			doube.dou += 1  # dou 增加1
			return redirect(url_for('doube'))
		if request.args.get('upload'):
			file = request.files['file']
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				session['fileurl'] = 'http://121.43.230.104:6666/static/upload/%s' % filename
				return redirect(url_for('doube'))

	# 发布逗文
	if form.validate_on_submit():
		doube = Doube(
			body = form.doube.data,
			author_id  = current_user.id,
            dou = 0
		)
		db.session.add(doube)
		db.session.commit()
		return redirect(url_for('doube'))

	return render_template(
			# 'doube.html',
			'home.html',
			new_dou=new_dou, best_dou=best_dou,
			douzan=douzan, form=form
	)
