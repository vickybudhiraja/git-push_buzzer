from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1 for sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")