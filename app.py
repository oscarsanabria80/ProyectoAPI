import requests
import os
from flask import Flask,render_template,abort
app=Flask(__name__)

#URL BASE
base="https://api.soccersapi.com/v2.2/"
#Variables de Entorno
key=os.environ["key"]
usuario=os.environ["usuario"]


@app.route('/')
def inicio():
    
	return render_template("inicio.html")


app.run(debug=True)
