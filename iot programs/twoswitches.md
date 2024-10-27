

### Example Circuit Diagram
```
      GPIO 17 (Pin 11)  ----->  Anode of LED1
                            |       
                            |
                            R (220 ohm resistor)
                            |
                            |
                          Cathode of LED1
                            |
                            |
                           GND (Pin 6)

      GPIO 27 (Pin 13)  ----->  Anode of LED2
                            |       
                            |
                            R (220 ohm resistor)
                            |
                            |
                          Cathode of LED2
                            |
                            |
                           GND (Pin 6)

      GPIO 22 (Pin 15)  ----->  One terminal of Switch1
                            |
                           GND (Pin 6)

      GPIO 23 (Pin 16)  ----->  One terminal of Switch2
                            |
                           GND (Pin 6)
```

### Python Code


```python
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for LEDs and switches
led1_pin = 17  # Pin for LED1
led2_pin = 27  # Pin for LED2
switch1_pin = 22  # Pin for Switch1
switch2_pin = 23  # Pin for Switch2

# Set up the GPIO pins for LEDs as outputs
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)

# Set up the GPIO pins for switches as inputs with pull-down resistors
GPIO.setup(switch1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        # Read the state of the switches
        switch1_state = GPIO.input(switch1_pin)
        switch2_state = GPIO.input(switch2_pin)
        
        # Control LED1 based on Switch1
        if switch1_state == GPIO.HIGH:
            GPIO.output(led1_pin, GPIO.HIGH)  # Turn LED1 ON
        else:
            GPIO.output(led1_pin, GPIO.LOW)   # Turn LED1 OFF
        
        # Control LED2 based on Switch2
        if switch2_state == GPIO.HIGH:
            GPIO.output(led2_pin, GPIO.HIGH)  # Turn LED2 ON
        else:
            GPIO.output(led2_pin, GPIO.LOW)   # Turn LED2 OFF
        
        # Small delay to prevent excessive CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings on exit
    GPIO.cleanup()
    print("Program terminated.")

# Clean up GPIO settings after the loop
GPIO.cleanup()
```
