import time
from datetime import datetime

for i in range(10):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")
    time.sleep(10)

print("Finished printing time 10 times.")
