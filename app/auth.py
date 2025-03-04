from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User
from werkzeug.security import check_password_hash

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    u = User.query.filter_by(username=username).first()
    if u is None:
        return False
    g.current_user = u 
    return check_password_hash(u.password, password)

@token_auth.verify_token
def verify_token(token):
    if token:
        return User.check_token(token)
    return None
    
