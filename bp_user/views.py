import json

import app
from flask import Blueprint, jsonify, request
from utils import *

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.get('/users')
def users_page():
    users = app.User.query.all()

    result = []
    for user in users:
        result.append(user_to_dict(user))
    return json.dumps(result)


@user_blueprint.get('/users/<int:uid>')
def user_page(uid):
    user = user_to_dict(app.User.query.get(uid))
    return json.dumps(user)


@user_blueprint.post('/users')
def add_user():
    user_data = json.loads(request.data)
    app.db.session.add(app.User(**user_data))
    app.db.session.commit()
    return ''


@user_blueprint.put('/users/<int:uid>')
def upd_user(uid):
    user_data = json.loads(request.data)
    user = app.User.query.get(uid)

    user.first_name = user_data["first_name"],
    user.last_name = user_data["last_name"],
    user.age = user_data["age"],
    user.email = user_data["email"],
    user.role = user_data["role"],
    user.phone = user_data["phone"]
    app.db.session.add(user)
    app.db.session.commit()
    return ''


@user_blueprint.delete('/users/<int:uid>')
def delete_user(uid):
    user = app.User.query.get(uid)
    app.db.session.delete(user)
    app.db.session.commit()
    return ''
