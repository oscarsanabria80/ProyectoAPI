import requests
import json
import os


def continentes():
    base="https://api.soccersapi.com/v2.2/"

    key=os.environ["key"]

    usuario=os.environ["usuario"]

    parametros={'token':key,'user':usuario,'t':"list"}

    r=requests.get(base+'continents/',params=parametros)

    j =r.json()
    if r.status_code ==200:
        for i in j["data"]:
            if i["name"]:
                print ("Los continentes del Mundo:", i["name"])
    
continentes()
