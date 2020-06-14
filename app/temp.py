#temp.py
import Adafruit_DHT
import time


def readTemp():
    '''reads the temperature and humidity from the DHT11 sensor '''
    #read data, GPIO pin 17
    sensor = Adafruit_DHT.DHT11
    pin = 17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
        
        
while True:
    readTemp()
    time.sleep(3600) #read the temp/humidity once every hour 


