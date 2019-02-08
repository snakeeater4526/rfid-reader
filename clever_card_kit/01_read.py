#!/usr/bin/env python

import os
import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import socket

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

while True:
        try:
                id, text = reader.read()
                print(id)
                print(text)
                print(type(text))
                file = open("badge_id_and_name.txt","w")
                file.write('{0}'.format(id))
                file.write("\n")
                file.write('{0}'.format(text))
                file.close()

                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                print(s.getsockname()[0])
                ip_from = s.getsockname()[0]  
                s.close()
                os.system('curl -X GET "http://10.1.1.147?device_id=3&ip_from='+ip_from+'&badge_id='+str(id)+'&badge_content='+text.replace(" ", '%20')+'"')

                if(id == 579524404115 or id == 739692225313 or id == 711892313040 or id == 841781257100 or id == 828069795733 or id == 556251098634 or id == 84282908938 or id == 427905426247):
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(4, GPIO.OUT)
                        GPIO.output(4, GPIO.HIGH)
                        time.sleep(2)
                        GPIO.output(4, GPIO.LOW)
                else:
                        time.sleep(2)

        except:
                os.system('curl -X GET "http://10.1.1.147?device_id=3&ip_from='+ip_from+'&badge_id='+str(id)+'&badge_content=null"')
                #GPIO.setmode(GPIO.BCM)
                #GPIO.setup(4, GPIO.OUT)
                #GPIO.output(4, GPIO.HIGH)
                time.sleep(2)
                #GPIO.output(4, GPIO.LOW)

        finally:
                print("cleaning up")
