#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythones.net

from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():


  #POST AUTH
    url = "https://gravitate-health.lst.tfo.upm.es/realms/GravitateHealth/protocol/openid-connect/token"
    payload='client_id=GravitateHealth&grant_type=password&username=user-test%40gh.com&password=Alumni-diabetic-attentive1'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'AUTH_SESSION_ID=06dc3d0a-3faa-48f8-80a6-96b49e0c2930.keycloak-54d87cb874-fgfqt-35421; AUTH_SESSION_ID_LEGACY=06dc3d0a-3faa-48f8-80a6-96b49e0c2930.keycloak-54d87cb874-fgfqt-35421; connect.sid=s%3AzAO6RERUqbVCqTestPUumDeN-mjugapo.rQwGxTAWl1VSZLcxFOMhkcxQZAkAFZ0ZHXD64zuJhMc'
      }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    token= response.json()

    #GET PATIENT
    url = "http://hapi.fhir.org/baseR4/Patient/3004256/_history/1"

    payload={}
    headers = {}

    response1 = requests.request("GET", url, headers=headers, data=payload)

  #POST PATIENT
    url = "https://gravitate-health.lst.tfo.upm.es/fhir/Patient"
    
    payload = response1
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + str(token.get('access_token'))
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response.text

if __name__ == "__main__":
    app.run()

