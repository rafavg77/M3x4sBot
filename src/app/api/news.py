from flask import Blueprint,jsonify
from datetime import date
from api.utils.getNews import GetNews

news = Blueprint('news', __name__)

@news.route('/')
def index():
    return("Welcome to News")

@news.route('/getAll')
def getAll():
    new = GetNews()
    #response = new.getAll()
    response = new.getAll()
    return(jsonify(response))