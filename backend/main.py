from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from flask_caching import Cache

import os

from api_crypto import API_cryptocurrency

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__file__)
cache.init_app(app)
CORS(app)
api = API_cryptocurrency(os.environ.get("API_KEY"))

@app.route("/")
def index():
    return "it is back"

@app.route("/get_top_cryptocurrencies")
@app.route("/api/get_top_cryptocurrencies")
@cross_origin()
@cache.cached(timeout=60)
def get_top_cryptocurrencies():
    res = api.api_get_top_cryptocurrencies(100)
    return res 

@app.route("/get_info_cryptocurrency/<id>")
@app.route("/api/get_info_cryptocurrency/<id>")
@cross_origin()
@cache.cached(timeout=60)
def get_info_cryptocurrency(id):
    res = api.api_get_info_cryptocurrency(id)
    return res 

# routes
@app.route('/assets/<path:path>')
def serve_assets(path):
    return send_from_directory('static/assets', path)

@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('static/images', path)


if __name__ == "__main__":
    api = API_cryptocurrency(os.environ.get("API_KEY"))
    app.run(debug=True)