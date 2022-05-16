import requests
import json
import os


def apuesta():
    key=os.environ["key"]
    url = "https://api.soccersapi.com/v2.2/bookmakers/?user=oscar.poncedeleonsanabria80&token="+key+"&t=list"

    r= requests.get(url)
    j =r.json()

    if "data" in j:
        for i in j["data"]:

            print("Casa de apuesta:", i["name"])
    
apuesta()
