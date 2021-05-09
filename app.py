from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    request = requests.get('http://127.0.0.1:5000/api/get_all_coinpairs')
    list_crypto_pairs = json.loads(request.text)
    return render_template('index.html', colours = list_crypto_pairs)
