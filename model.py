import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ADS_PER_PAGE = 10

app = Flask(__name__)
# str = f"postgresql+psycopg2://postgres:simplePass@localhost:5432/adsmodel"
str = f"postgresql+psycopg2://postgres:simplePass@db:5432/adsDB"
app.config['SQLALCHEMY_DATABASE_URI'] = str
db = SQLAlchemy(app)


class Ad(db.Model):
    __tablename__ = 'ads'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    photos = db.Column(db.String, nullable=False)
    description = db.Column(db.String(1000))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


db.create_all()


def create_ad(data):
    ad = None

    try:
        if len(data['photos']) <= 3:
            res = Ad(name=data['name'], price=data['price'], photos=data['photos'], description=data['description'])
            db.session.add(res)
            db.session.commit()
            ad = res.id
            return ad, ''
        return ad, 'no ad created: invalid input data'
    except Exception as e:
        return ad, e


def get_ad(id):
    ad = None

    try:
        res = db.session.query(Ad).filter_by(id=id).first()
        if not res:
            return ad, f'no ad with id={id} found'
        photos = [photo for photo in res.photos[1:len(res.photos) - 1].split(',')]
        ad = {'name': res.name, 'price': res.price, 'photos': photos, 'description': res.description}
        return ad, ''

    except Exception as e:
        return ad, e


def get_ads(sort_by, order_by, page):
    ads = []

    try:
        res = db.session.query(Ad).order_by(getattr(getattr(Ad, sort_by), order_by)())\
            .paginate(page, ADS_PER_PAGE, False).items
        if not res:
            return ads, 'no ads found'
        for _ in res:
            photos = [photo for photo in _.photos[1:len(_.photos) - 1].split(',')]
            ads.append({'name': _.name, 'price': _.price, 'photos': photos[0], 'id': _.id})
        return ads, ''

    except Exception as e:
        return ads, e
