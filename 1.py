import requests
import json
import os


def apuesta():
    base="https://api.soccersapi.com/v2.2/"

    key=os.environ["key"]

    usuario=os.environ["usuario"]

    parametros={'token':key,'user':usuario,'t':"list"}

    r=requests.get(base+'bookmakers/',params=parametros)
    j =r.json()

    if "data" in j:
        print("Casa de apuesta:")
        for i in j["data"]:
            print(i["name"])
    
apuesta()
