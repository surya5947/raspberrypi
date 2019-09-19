import RPi.GPIO as GPIO
import time

relay_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin,GPIO.OUT)

try:
        while True:
                #set low
                print ("Setting low - solienoid ON")
                GPIO.output (relay_pin,GPIO.LOW)
                time.sleep(100)
                #set high
                print ("Setting high - solienoid OFF")
                GPIO.output (relay_pin, GPIO.HIGH)
                time.sleep(100)
except KeyboardInterrupt:
	GPIO.cleanup()
        print ("Bye")