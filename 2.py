import requests
import json

def continentes():
    url ='https://api.soccersapi.com/v2.2/continents/?user=oscar.poncedeleonsanabria80&token=514efe4a99c6e66e68561b915fb4c0e4&t=list'

    r= requests.get(url)
    j =r.json()

    for i in j["data"]:
        if i["name"]:
         print ("Los continentes del Mundo:", i["name"])
    
continentes()
