import RPi.GPIO as GPIO
import SimpleMFRC522
import mysql.connector

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

try:
    while True:
        id, text = reader.read()
        print(id) # badge_id
        print(text) # badge_content
        # Se connecter à la base de données

finally:
    print("cleaning up")
    GPIO.cleanup()
