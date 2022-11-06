import gps_funktion
from time import sleep
from machine import Pin, ADC
import umqtt_robust2 as mqtt
import _thread


def gps_start_thread():
    print("thread")
    _thread.start_new_thread(gps_measure,())
    print("gps started")


def gps_measure():
    while True:
            
            gps_data = gps_funktion.gps_to_adafruit
            print(f"\ngps_data er: {gps_data}")     
            
            mqtt.web_print(gps_data, 'Greeznerd/feeds/mapfeed/csv')
            sleep(30)
            
                
