import pymysql
pymysql.install_as_MySQLdb()
# 这一步主要是导入app下中的__init__里面的数据库配置及db
from app import db


# 创建实例类
class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    uloginname = db.Column(db.String(30))
    uloginpwd = db.Column(db.String(30))
    uname = db.Column(db.String(30))

    def __repr__(self):
        return '<User %r>' % self.uname

# 将实例类映射到数据库
db.create_all()
