#!/usr/bin/python3
# -*- coding: utf-8 -*-
#=============================================================
# Created: Tue 30 Nov 2021 10:47:14 PM -03
# Modified: Tue 30 Nov 2021 10:47:14 PM -03
#=============================================================
# Description: API that checks if the email is valid.
# Autor: Leonardo Berbert Gomes 

from flask import Flask
from flask import request
from flask import jsonify
from os import path
import json,re,sys,os
from email_validator import validate_email, EmailNotValidError

if path.exists('blacklist.conf') == False:
    print('\nIs not possible to start application without blacklist file \'blacklist.conf\'!!!\n')
    sys.exit(0)

config = open("blacklist.conf","r").read().splitlines()
pattern = '.*|.*'.join(config)
app = Flask(__name__)

@app.route("/api/v1/", methods = ['POST'])

def mailcheck():
    data = json.loads(request.data)
    emailAddress = data['emailAddress']
    blacklist = re.match(pattern,emailAddress,re.IGNORECASE)
    if blacklist:
            return jsonify({
                "emailAddress": str(emailAddress), 
                "status": 2,
                "bounce": { 
                "type": 1, 
                "detail": "Bad destination mailbox address", 
                "code": 511
                }
            })     
   
    if emailAddress:
        isValidate = ValidateMail(emailAddress)
        if isValidate == "1": # valid email
         return jsonify({
                        "emailAddress": str(emailAddress), 
                        "status": 1
                    })            
        else:
            return jsonify({
                "emailAddress": str(emailAddress), 
                "status": 2,
                "bounce": { 
                "type": 1, 
                "detail": "Invalid mail format", 
                "code": 990
                }
            }) 

def ValidateMail(email):
    try:
        valid = validate_email(email)
        email = valid.email

        if email:
            return('1')
        else:
            return('0')
    except EmailNotValidError as e:
        print(str(e))

if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)