# -*- coding: utf-8 -*-
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/balance/', methods=['GET', ])
def balance():
    balance = {
        'expected': 600,
        'actual': '23',
    }
    return jsonify(**balance)


if __name__ == '__main__':
    app.run(debug=True)
