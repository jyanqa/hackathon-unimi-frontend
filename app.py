from flask import Flask, render_template, Response, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    request = requests.get('http://127.0.0.1:5000/api/get_all_coinpairs')
    list_crypto_pairs = json.loads(request.text) #sorted
    #list_crypto = list_crypto_pairs.sort()
    extra_info = ['last price', 'volume']
    return render_template('index.html', cp = list_crypto_pairs, extra_info=extra_info)
ButtonPressed = 0
@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        return render_template("button.html", ButtonPressed = ButtonPressed)
        # I think you want to increment, that case ButtonPressed will be plus 1.
    return render_template("button.html", ButtonPressed = ButtonPressed)
app.run(host="localhost", port=8000, debug=True)