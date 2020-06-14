import RPi.GPIO as GPIO
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("Water Detected")
    else:
        print("No Water")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 5)
GPIO.add_event_callback(channel, callback)

#infinite loop
while True:
    time.sleep(3600) #check once an hour 
