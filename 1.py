import requests
import json

def apuesta():
    url = "https://api.soccersapi.com/v2.2/bookmakers/?user=oscar.poncedeleonsanabria80&token=514efe4a99c6e66e68561b915fb4c0e4&t=list"

    r= requests.get(url)
    j =r.json()

    if "data" in j:
        for i in j["data"]:

            print("Casa de apuesta:", i["name"])
    
apuesta()
