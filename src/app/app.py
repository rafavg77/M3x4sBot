from flask import Flask, jsonify
from api.m3x4asUtils import m3x4sUtils
from api.news import news

app = Flask(__name__)
app.register_blueprint(m3x4sUtils, url_prefix='/api')
app.register_blueprint(news, url_prefix='/api/news')

@app.errorhandler(404)
def page_not_found(e):
    response_body = {
            "message": "Not Found :("
            }

    return jsonify(response_body), 404

@app.errorhandler(405)
def page_not_found(e):
    response_body = {
            "message": "Method Not Allowed :("
            }

    return jsonify(response_body), 405