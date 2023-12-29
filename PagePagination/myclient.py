import requests
import json

URL = 'http://127.0.0.1:8000/'
def post():
    data = {
        "name":"Ashlen","roll":"5156","city":"Pieksämäki"
    }
    json_data = json.dumps(data)
    
    r = requests.post(url=URL, data=json_data)
    
    data = r.json()
    print(data)