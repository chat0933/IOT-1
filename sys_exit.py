# from umqtt_robust2 as mqtt
import sys
import tm1637
from machine import Pin
from time import sleep
import imu_measure

tm_imu = tm1637.TM1637(clk=Pin(2), dio=Pin(0))
tm_volt = tm1637.TM1637(clk=Pin(4), dio=Pin(3))

def stop_program():
    tm_imu.show("0000")
    count = 0
    tm_volt.show("0000")
    sleep(3)
    sys.exit()
