# -*- coding: utf-8 -*-
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/balance/', methods=['GET', ])
def balance():
    balance = {
        'expected': 600,
        'actual': -600,
    }
    return jsonify(**balance)

