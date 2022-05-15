import requests
import json

def equipo():
    url ='https://api.soccersapi.com/v2.2/teams/?user=oscar.poncedeleonsanabria80&token=514efe4a99c6e66e68561b915fb4c0e4&t=list&country_id=3'

    r= requests.get(url)
    j =r.json()
    print("EQUIPOS DE LA LIGA INGLESA")
    for i in j["data"]:
        if i["name"]:
         print (i["name"])
    
equipo()