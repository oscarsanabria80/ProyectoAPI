import requests
import json
import os

def equipo():
    base="https://api.soccersapi.com/v2.2/"

    key=os.environ["key"]

    usuario=os.environ["usuario"]

    parametros={'token':key,'user':usuario,'t':"list",'country_id':"3"}
    #url ="https://api.soccersapi.com/v2.2/teams/?user=oscar.poncedeleonsanabria80&token="+key+"&t=list&country_id=3"

    r=requests.get(base+'teams/',params=parametros)
    j =r.json()
    print("EQUIPOS DE LA LIGA INGLESA")
    if r.status_code ==200:

        for i in j["data"]:
            if i["name"]:
                print (i["name"])
    
equipo()