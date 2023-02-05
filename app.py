from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bp_user.views import user_blueprint
from bp_order.views import order_blueprint
from bp_offer.views import offer_blueprint
from datetime import datetime
import data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
app.register_blueprint(user_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(offer_blueprint)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))


with app.app_context():
    db.create_all()

    for order_dict in data.orders:
        order_dict['start_date'] = datetime.strptime(order_dict['start_date'], '%m/%d/%Y').date()
        order_dict['end_date'] = datetime.strptime(order_dict['end_date'], '%m/%d/%Y').date()
        new_order = Order(**order_dict)
        db.session.add(new_order)
        db.session.commit()

    for user_raw in data.users:
        new_user = User(**user_raw)
        db.session.add(new_user)
        db.session.commit()

    for offer_data in data.offers:
        db.session.add(Offer(**offer_data))
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
