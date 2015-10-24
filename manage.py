# coding: utf-8

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from doube import app, db
from doube.models import User, Doube
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
import sys


# 编码设置
reload(sys)
sys.setdefaultencoding('utf-8')


manager = Manager(app)
migrate = Migrate(app, db)
admin = Admin(app, name="Doube")
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Doube, db.session))


def make_shell_context():
    """命令行自动加载应用环境"""
    return dict(
        app = app,
        db = db,
        User = User,
		Doube = Doube
    )


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    app.debug = True
    manager.run()
