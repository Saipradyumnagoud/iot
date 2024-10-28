import RPi.GPIO as GPIO
import time 
led_pin=16
pir_pin=18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(pir_pin,GPIO.IN)
GPIO.output(led_pin,GPIO.LOW)
try:
    while True:
        if GPIO.input(pir_pin):
            print('motion detected')
            GPIO.output(led_pin,GPIO.HIGH)
        else:
            print('not detected')
            GPIO.output(led_pin,GPIO.LOW)
        time.sleep(0.1)
except keyboardInterrupt:
    GPIO.cleanup()