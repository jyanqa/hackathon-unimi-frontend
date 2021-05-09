from flask import Flask, render_template, Response, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    request = requests.get('http://0.0.0.0:8000/api/get_all_coinpairs')
    list_crypto_pairs = json.loads(request.text)
    extra_info = ['volume', 'Candlestick Charts']
    return render_template('index.html', colours = list_crypto_pairs,extra_info=extra_info)
if __name__ == "__main__":
    app.run(host="localhost", port=80, debug=True)
