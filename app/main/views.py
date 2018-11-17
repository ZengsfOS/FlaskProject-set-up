from ..models import *
from . import main
from app import *


# 这里主要是业务逻辑的处理
@main.route("/")
def index_views():
    users = User()
    users.uloginname = "zengsf"
    users.uloginpwd = "12345"
    users.uname = "fengshao"
    print(users)
    db.session.add(users)
    return "hello"
