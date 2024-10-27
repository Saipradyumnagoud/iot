import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR_PIN = 17  
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR Sensor Test (CTRL+C to exit)")

time.sleep(2)  

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
        else:
            print("No motion")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()  