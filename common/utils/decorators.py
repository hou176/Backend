from flask import g, current_app
from functools import wraps
from sqlalchemy.orm import load_only
from sqlalchemy.exc import SQLAlchemyError


from models import db



def set_db_to_read(func):
    """
    设置使用读数据库
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        db.session().set_to_read()
        return func(*args, **kwargs)
    return wrapper


# def set_db_to_write(func):
#     """
#     设置使用写数据库
#     """
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         db.session().set_to_write()
#         return func(*args, **kwargs)
#     return wrapper

# 实现用户登录认证的装饰器
def login(f):
    # 装饰器器会修改装饰过得函数名字  所以额在这之前先把装饰器给他改名了

    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.user_id and g.is_refresh is False:
            return f(*args, **kwargs)
        else:
            return{'message':'authorized failed'},403
    return wrapper

