import adafruit_dht
import board
import RPi.GPIO as GPIO

def temper():
    sensor_pin = 23
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor_pin, GPIO.IN)
        dhtDevice = adafruit_dht.DHT11(board.D23)
        
        temp = dhtDevice.temperature
        humid = dhtDevice.humidity
        return temp, humid
    except RuntimeError as error:
        print(f"Error reading from DHT11: {error}")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None
    finally:
        try:
            dhtDevice.exit()
            GPIO.cleanup(sensor_pin)
        except Exception as e:
            print(f"Error cleaning up GPIO: {e}")
