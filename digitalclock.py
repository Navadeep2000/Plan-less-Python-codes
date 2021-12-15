#Digital Clock
import datetime
import time
while(True):
    x=datetime.datetime.now()
    print(x.strftime('%H:%M:%S %p'),end='')
    print('\r',end='')
    time.sleep(1)