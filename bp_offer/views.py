from flask import Blueprint, jsonify
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
