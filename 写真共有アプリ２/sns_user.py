# ユーザとログイン管理を行うモジュール
from flask import session, redirect
from functools import wraps


# ユーザー名とパスワードの一覧
USER_LOGIN_LIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc',
    'siro': 'ddd',
    'goro': 'eee',
    'muro': 'fff'
}


# ログインしているかどうかの確認
def is_login():
    return 'login' in session


# ログインを試行する
def try_login(form):
    user = form.get('user', '')
    password = form.get('pw', '')
    # パスワードチェック
    if user not in USER_LOGIN_LIST:
        return False
    if USER_LOGIN_LIST[user] != password:
        return False
    session['login'] = user
    return True


# ユーザー名を得る
def get_id():
    return session['login'] if is_login() else '未ログイン'


# 全ユーザの情報を得る
def get_allusers():
    return [u for u in USER_LOGIN_LIST]


# ログアウトする
def try_logout():
    session.pop('login', None)


# ログイン必須を処理するデコレーターを定義
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login():
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
