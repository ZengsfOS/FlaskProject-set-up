from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置该模式为ｄｅｂｕｇ模式
app.config['DEBUG'] = True
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/zengsf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 自动提交
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# 密钥
app.config['SECRET_KEY'] = 'xieshadouxing'

# 创建数据库实例
db = SQLAlchemy(app)


# 创建一个函数，里面配置蓝图
def create_app():
    # 不要在生成db之前导入注册蓝图
    # 将创建好的蓝图导入过来，进行注册
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app