from flask import Blueprint
# 创建蓝图实例
main = Blueprint("main", __name__)

from . import views