# -*- coding: utf-8 -*-
from flask import Flask, jsonify, Response, request
app = Flask(__name__)


@app.route('/balance/', methods=['GET', ])
@app.route('/balance/<int:year>/<int:month>/')
def balance(year=None, month=None):

    format = request.args.get('format', 'json')

    balance = {
        'expected': 600,
        'actual': -600,
    }
    if year:
        balance['year'] = year
    if month:
        balance['month'] = month

    if format == 'csv':
        data = "{0},{1},{2},{3}".format(balance['expected'], balance['actual'], balance['year'], balance['month'])
        return Response(data, mimetype='text/csv')

    return jsonify(**balance)
