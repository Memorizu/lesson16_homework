import json

from flask import Blueprint, jsonify, request
import app
from utils import order_to_dict


order_blueprint = Blueprint('order_blueprint', __name__)


@order_blueprint.get('/orders')
def orders_page():
    orders = app.Order.query.all()
    result = []
    for order in orders:
        order_dict = order_to_dict(order)
        order_dict['start_date'] = str(order_dict['start_date'])
        order_dict['end_date'] = str(order_dict['end_date'])
        result.append(order_dict)
    return jsonify(result)


@order_blueprint.get('/orders/<int:oid>')
def order_page(oid):
    order = app.Order.query.get(oid)
    order_dict = order_to_dict(order)
    order_dict['start_date'] = str(order_dict['start_date'])
    order_dict['end_date'] = str(order_dict['end_date'])
    return jsonify(order_dict)


@order_blueprint.post('/orders')
def add_order():
    order_data = json.loads(request.data)
    app.db.session.add(app.Order(**order_data))
    app.db.session.commit()
    return ''
