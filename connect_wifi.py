import time
import network
from defs import wifi_ssid, wifi_password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection ... ')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('connection to the network failed!')
else:
    print('WIFI connected!')
    status = wlan.ifconfig()
    print(status[0])