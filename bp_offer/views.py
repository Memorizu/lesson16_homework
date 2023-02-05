import json

from flask import Blueprint, jsonify, request
from utils import offers_to_dict
import app

offer_blueprint = Blueprint('offer_blueprint', __name__)


@offer_blueprint.get('/offers')
def offers_page():
    offers = app.Offer.query.all()

    result = [offers_to_dict(offer) for offer in offers]
    return jsonify(result)


@offer_blueprint.get('/offers/<int:id>')
def offer_page(id):
    offer = app.Offer.query.get(id)
    result = offers_to_dict(offer)
    return jsonify(result)


@offer_blueprint.post('/offers')
def add_offer():
    offer_data = json.loads(request.data)
    app.db.session.add(app.Offer(**offer_data))
    app.db.session.commit()
    return ''


@offer_blueprint.put('/offers/<int:offer_id>')
def upd_offer(offer_id):
    offer_data = json.loads(request.data)
    offer = app.Offer.query.get(offer_id)
    offer.order_id = offer_data['order_id']
    offer.executor_id = offer_data['executor_id']
    app.db.session.add(offer)
    app.db.session.commit()
    return ''


@offer_blueprint.delete('/offers/<int:offer_id>')
def delete_offer(offer_id):
    offer = app.Offer.query.get(offer_id)
    app.db.session.delete(offer)
    app.db.session.commit()
    return ''
