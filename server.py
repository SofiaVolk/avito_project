from flask import Flask, jsonify, request
from model import app
import model as db
import logs


@app.route('/ad', methods=['POST'])
def create_ad():
    data = request.json
    if not data:
        logs.api_logger.error('400 -\t' + 'no json content')
        return jsonify({'message': 'no json content'}), 400

    try:
        id, msg = db.create_ad(data)
        if not id:
            logs.api_logger.error('404 -\t' + str(msg))
            return jsonify({'message': 'no ad created (invalid input data)'}), 404
        return jsonify({'id': id}), 200

    except Exception as e:
        logs.api_logger.error('500 -\t' + str(e))
        return '', 500


@app.route('/ad/<int:adId>', methods=['GET'])
def get_ad(adId):
    fields = request.args.get('fields', default=False)

    try:
        ad, msg = db.get_ad(adId)
        if not ad:
            logs.api_logger.error('404 -\t' + str(msg))
            return jsonify({'message': 'no ad with such id found'}), 404
        if fields:
            return jsonify({'name': ad['name'], 'price': ad['price'], 'photos': ad['photos'],
                            'description': ad['description']}), 200
        return jsonify({'name': ad['name'], 'price': ad['price'], 'photos': ad['photos'][0]}), 200

    except Exception as e:
        logs.api_logger.error('500 -\t' + str(e))
        return '', 500


@app.route('/ads', methods=['GET'])
@app.route('/ads/<int:page>', methods=['GET'])
def get_ads(page=1):
    sort_by = request.args.get('sort_by', default='date')
    order_by = request.args.get('order_by', default='desc')

    try:
        ads, msg = db.get_ads(sort_by, order_by, page)
        if not ads:
            logs.api_logger.error('404 -\t' + str(msg))
            return jsonify({'message': 'no ads in database found'}), 404
        return jsonify(ads), 200

    except Exception as e:
        logs.api_logger.error('500 -\t' + str(e))
        return 500


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8070")
    # app.run(host="0.0.0.0", port="8070")
