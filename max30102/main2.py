
import time
import GY906 
sensor = GY906.GY906()


def measure():
   
    temperature = sensor.get_obj_temp()
    print("Temp:",temperature);
    time.sleep(3)
                        
    
if __name__== "__main__":
    while True:
        measure()
        time.sleep(1)
