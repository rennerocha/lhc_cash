# -*- coding: utf-8 -*-
import datetime

from flask import Flask, jsonify, Response, request
app = Flask(__name__)


@app.route('/balance/', methods=['GET', ])
@app.route('/balance/<int:year>/<int:month>/')
def return_balance(year=None, month=None):

    if not year or not month:
        year = datetime.date.today().year
        month = datetime.date.today().month

    format = request.args.get('format', 'json')

    balance = {
        'expected': 600,
        'actual': -600,
        'year': year,
        'month': month,
    }

    if format == 'csv':
        data = "{0},{1},{2},{3}".format(balance['expected'], balance['actual'], balance['year'], balance['month'])
        return Response(data, mimetype='text/csv')

    return jsonify(**balance)
