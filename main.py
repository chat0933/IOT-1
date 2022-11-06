from machine import Pin, ADC, I2C
from time import sleep
import umqtt_robust2 as mqtt
from imu import MPU6050
import tm1637
import _thread
import gps_measure 
import volt_measure
# from puls_measure import puls_styring, puls_funktion, timer
import imu_measure
from sys_exit import stop_program


while True:
    try:
        if mqtt.besked == "start":
            imu_measure.imu_start_thread()
            sleep(1)
            gps_measure.gps_start_thread()
            sleep(5)
            volt_measure.volt_start_thread()
            sleep(15)
        if mqtt.besked == "stop":
            stop_program()

            
        
        
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
#         print(".", end = '') # printer et punktum til shell, uden et enter        
        # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()