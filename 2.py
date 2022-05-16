import requests
import json
import os

def continentes():
    key=os.environ["key"]
    url = "https://api.soccersapi.com/v2.2/continents/?user=oscar.poncedeleonsanabria80&token="+key+"&t=list"

    r= requests.get(url)
    j =r.json()

    for i in j["data"]:
        if i["name"]:
         print ("Los continentes del Mundo:", i["name"])
    
continentes()
