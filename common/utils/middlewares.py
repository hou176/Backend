from flask import request,g
from .jwt_util import verify_jwt

# 需求：在每次请求前，尝试获取用户信息
# 手动构建认证机制，伪代码。
# - 构建认证机制
# - 对于特定视图，强制要求用户必须登录，才能访问
# - 对于所有视图，无论是否强制要求用户登录，都可以在视图中尝试获取用户认证后的身份信息


# 在每次请求前，尝试用户用户信息
# @app.before_request

def jwt_authentication():
    # 从请求头中提取token，从token提取payload中存储的用户信息
    # token = request.headers.get('Authorization')
    # g.user_id = None
    # g.refresh = None
    # if token and token.startswith('Bearer '):
    #     token = token[7:]
        # token的校验


    # 请求头中的获得token
    auth = request.headers.get('Authorization')
    if auth is not None and auth.startswith('Bearer'):
        # 切片操作  用来选取一部分信息
        token = auth[7:]
        # 校验token，提取payload
        payload = verify_jwt(token)
        # 如果在的话给g对象
        if payload:
            g.user_id = payload.get('user_id')
            # g.refresh = payload.get('refresh')
            g.id_refresh = payload.get('id_refresh')

# 在请求钩子中 实现每次请求常识获取用户token  校验token提取用户id  赋值个g对象
# 请求钩子中第二个
# @app.before_request
# 定义用户认证的功能函数 通过工厂函数中APP手动调用  befor_request请求钩子



