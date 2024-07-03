# dht11_test.py
import adafruit_dht
import time
import RPi.GPIO as GPIO
import board

sensor_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

def temper():
    sensor_pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor_pin, GPIO.IN)
    dhtDevice = adafruit_dht.DHT11(board.D18) # Problem!!
    temp = dhtDevice.temperature
    humid = dhtDevice.humidity
    return temp,humid

def read_dht11():
    dhtDevice = adafruit_dht.DHT11(board.D18)
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        return temperature, humidity
    except RuntimeError as error:
        print(f"Error reading from DHT11: {error}")
        return None, None
    finally:
        dhtDevice.exit()