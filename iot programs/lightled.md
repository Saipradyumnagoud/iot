

### Example Circuit Diagram
```
     GPIO 18 (Pin 12)  ----->  Anode (Longer leg) of LED
                           |       
                           |
                           R (220 ohm resistor)
                           |
                           |
                         Cathode (Shorter leg) of LED
                           |
                           |
                          GND (Pin 6)
```



```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 18  
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)  # Wait for 1 second
        
        # Turn the LED off
        
        GPIO.output(led_pin, GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO settings on exit
    GPIO.cleanup()
    print("Program terminated.")

# Clean up GPIO settings after the loop
GPIO.cleanup()
```
