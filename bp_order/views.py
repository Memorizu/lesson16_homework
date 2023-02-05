import json
from datetime import datetime
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
    order_data['start_date'] = datetime.strptime(order_data['start_date'], '%Y-%m-%d').date()
    order_data['end_date'] = datetime.strptime(order_data['end_date'], '%Y-%m-%d').date()
    app.db.session.add(app.Order(**order_data))
    app.db.session.commit()
    return ''


@order_blueprint.put('/orders/<order_id>')
def upd_order(order_id):
    order_data = json.loads(request.data)
    order = app.Order.query.get(order_id)
    order.name = order_data['name']
    order.description = order_data['description']
    order.start_date = datetime.strptime(order_data['start_date'], '%Y-%m-%d').date()
    order.end_date = datetime.strptime(order_data['end_date'], '%Y-%m-%d').date()
    order.address = order_data['address']
    order.price = order_data['price']
    order.customer_id = order_data['customer_id']
    order.executor_id = order_data['executor_id']
    app.db.session.add(order)
    app.db.session.commit()
    return ''


@order_blueprint.delete('/orders/<order_id>')
def delete_order(order_id):
    order = app.Order.query.get(order_id)
    app.db.session.delete(order)
    app.db.session.commit()
    return ''
