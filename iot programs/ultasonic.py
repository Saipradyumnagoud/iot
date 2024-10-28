import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the sensor
TRIG_PIN = 23  # Trigger pin connected to GPIO 23 (Pin 16)
ECHO_PIN = 24  # Echo pin connected to GPIO 24 (Pin 18)

# Set the Trigger pin as output and Echo pin as input
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    # Make sure the Trigger pin is low for 2µs
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.2)
    
    # Send a 10µs pulse to trigger the sensor
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG_PIN, False)
    
    # Record the time of the pulse
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    
    # Calculate the duration of the pulse
    pulse_duration = pulse_end - pulse_start
    
    # Calculate distance in cm (speed of sound is 34300 cm/s)
    distance = pulse_duration * 17150  # Divided by 2 (there and back)
    distance = round(distance, 2)
    
    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()  # Clean up GPIO settings
