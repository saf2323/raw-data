import psutil
import pyfirmata
import datetime
import os
import time

print(datetime.datetime.now())
print('PID:',os.getpid())
print('PPID:',os.getppid())
pyf = pyfirmata.Arduino('COM4')
l = pyf.get_pin('d:13:o')
while True:
    cpuusage = psutil.cpu_percent()
    print(f'cpu usage:{cpuusage}%')
    # if cpuusage < 30:
    #     print('Normal')

    #     l.write(1)
    #     time.sleep(1)
    #     l.write(0)

    if cpuusage > 50:
        print('Warning! close programs running in background.')

        l.write(1)
        time.sleep(1)
        l.write(1)

    # time.sleep(2)
