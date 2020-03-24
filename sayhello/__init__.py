from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment


# Flask通过 FLASK_APP 环境变量定义的模块中寻找程序实例
# Flask通过这个值确认程序路径，当使用包组织代码时，为了确保其他扩展或测试程序框架获得正确的路径值
# 最好以硬编码的形式写出 包名称 作为程序名称，即sayhello
app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

from sayhello import views, errors, commands
