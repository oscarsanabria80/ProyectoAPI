import requests
import json
import os

def equipo():
    key=os.environ["key"]
    url ="https://api.soccersapi.com/v2.2/teams/?user=oscar.poncedeleonsanabria80&token="+key+"&t=list&country_id=3"

    r= requests.get(url)
    j =r.json()
    print("EQUIPOS DE LA LIGA INGLESA")
    if r.status_code ==200:

        for i in j["data"]:
            if i["name"]:
                print (i["name"])
    
equipo()