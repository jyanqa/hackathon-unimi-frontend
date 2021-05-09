from flask import Flask, render_template, Response, request, redirect, url_for
import requests
import json

from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def index():
    request = requests.get('http://127.0.0.1:5000/api/get_all_coinpairs')
    list_crypto_pairs = json.loads(request.text) #sorted
    #list_crypto = list_crypto_pairs.sort()
    extra_info = ['last price', 'volume']
    return render_template('index.html', colours = list_crypto_pairs, extra_info=extra_info)


app.run(host="localhost", port=8000, debug=True)