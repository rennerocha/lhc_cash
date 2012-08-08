# -*- coding: utf-8 -*-
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/balance/', methods=['GET', ])
@app.route('/balance/<int:year>/<int:month>/')
def balance(year=None, month=None):
    balance = {
        'expected': 600,
        'actual': -600,
    }
    if year:
        balance['year'] = year
    if month:
        balance['month'] = month

    return jsonify(**balance)

