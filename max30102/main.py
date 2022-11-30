from heartrate_monitor import HeartRateMonitor
import time
import numpy as np

def readSensor():

   bpm = 0
   spo2 = 0
   temperature = 0
   print('sensor starting...')
   hrm= HeartRateMonitor()
   hrm.start_sensor()
   try:
        time.sleep(30)
   except KeyboardInterrupt:
         print('keyboard interrupt detected, exiting...')

   hrm.stop_sensor()

   print(hrm.bpm2)
   print(hrm.spo2)
   print(hrm.temperature)
   print('sensor stoped!')
   bpm = np.mean(hrm.bpm2)
   spo2 = np.mean(hrm.spo2)
   temperature = np.mean(hrm.temperature)
   return bpm,spo2,temperature

b,s,t = readSensor()
print(b,s,t)
