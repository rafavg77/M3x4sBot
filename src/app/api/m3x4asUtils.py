from flask import Blueprint,jsonify
from datetime import date

m3x4sUtils = Blueprint('m3x4sUtils', __name__)

defcon_date = date(2023,8,10)

@m3x4sUtils.route('/')
def index():
    return("Welcome to M3x4as API")

@m3x4sUtils.route('/days2Defcon',methods=['POST'])
def days2Defcon():
    today = date.today()
    remaining_days = (defcon_date-today).days
    data = {
        "today" : today,
        "remaining_days" : remaining_days,
        "error" :  False
    }
    return(jsonify(data))

@m3x4sUtils.route('/events',methods=['POST'])
def events():
    data = [
        {
        "event_name" : "DragonJar",
        "eventa_date" : "TBD",
        "event_country" :  "Comlombia"
        },
        {
        "event_name" : "DEFCON",
        "eventa_date" : "10 Agosto 2023",
        "event_country" :  "Estados Unidos"
        },
        {
        "event_name" : "Ekoparty",
        "eventa_date" : "TBD",
        "event_country" :  "Argentina"
        },
        {
        "event_name" : "CISI UANL",
        "eventa_date" : "TBD",
        "event_country" :  "México"
        },
        {
        "event_name" : "Bugcon",
        "eventa_date" : "TBD",
        "event_country" :  "México"
        },
    ]
    return(jsonify(data))