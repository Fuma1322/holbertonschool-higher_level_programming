import sys
import time

while True:
    sys.stdout.write("1 ")
    sys.stdout.flush()
    time.sleep(0.5)  # Adjust the sleep time as desired
    sys.stdout.write("0 ")
    sys.stdout.flush()
    time.sleep(0.5)  # Adjust the sleep time as desired
