#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythones.net

from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    
    #GET
    url = "http://hapi.fhir.org/baseR4/Patient/3004256/_history/1"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    #POST
    url = "https://gravitate-health.lst.tfo.upm.es/fhir/Patient"

    payload = response
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
  
    return response.text

if __name__ == "__main__":
    app.run()

