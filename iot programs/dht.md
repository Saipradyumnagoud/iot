

### Example Circuit Diagram
```
        DHT Sensor (DHT11/DHT22)
         ______________________
        |  1  |  2  |  3  |  4  |
        | VCC |Data |NC/NC|GND |
        ------------------------
         |       |        |   
       3.3V    GPIO4    GND 
         |       |
        10kΩ    |
         |      Pull-up resistor
        GND    |
``` 



```python
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22 
pin = 4  
try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from the sensor")
        time.sleep(2)

except KeyboardInterrupt:
    print("Program terminated")
```
