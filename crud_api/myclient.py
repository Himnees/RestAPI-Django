import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'
def get_data(id=None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
    
#get_data()

def post_data():
    data={
        'id':5,
        'name':'Chowdary',
        'roll':'105',
        'city':'Bangalore'
    }
    json_data = json.dumps(data)
    
    r= requests.post(url=URL, data=json_data)
    
    data = r.json()
    
    print(data)
    
#post_data()

def update_data():
    data = {
        'id':1,
        'name':'Dodda',
        'roll':123,
        'city':'Bapatla'
    }
    json_data = json.dumps(data)
    
    r= requests.put(url=URL, data=json_data)
    
    data = r.json()
    
    print(data)
    
#update_data()

def delete_post():
    data = {'id':1}
    json_data = json.dumps(data)
    
    r= requests.delete(url=URL, data=json_data)
    
    data = r.json()
    
    print(data)
delete_post()