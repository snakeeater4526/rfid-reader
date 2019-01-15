#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import mysql.connector

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

try:
    db = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='rfid')
    while True:
        id, text = reader.read()
        print(id) # badge_id
        print(text) # badge_content
        
        cursor = db.cursor()
        
        cursor.execute("SELECT max(request_id) from request_log")
        request_id = cursor.fetch()
        if(request_id == null):
            request_id = 1
        else:
            request_id += 1

        print(request_id)
		#sql = 'insert into request_log(request_id, device_id, ip_from, badge_id, badge_content, datetime) values(%s, %s, %s,  %s, %s, now())'
		
finally:
    print("cleaning up")
    GPIO.cleanup()
