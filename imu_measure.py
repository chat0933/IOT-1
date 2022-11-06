'''
Using the MPU6050 inertial unit (accelerometer + gyrometer) with a Raspberry Pi Pico.
For more info:
bekyelectronics.com/raspberry-pi-pico-and-mpu-6050-micropython/
'''

from imu import MPU6050  # https://github.com/micropython-IMU/micropython-mpu9x50
import time
from time import sleep 
from machine import Pin, I2C
import tm1637
import _thread


    
def imu_start_thread():
    print("thread")
    _thread.start_new_thread(acc_measure,())
    print("IMU started")
        

def acc_measure():
    maalt = 0
    count = 0
    tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))
    i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
    imu = MPU6050(i2c)
    tm.show("0000")

    while True:
        sleep(1)
        gyroscope = imu.gyro
        acceleration = imu.accel
        if abs(acceleration.x) > 0.8:
            if (acceleration.x > 0):
                print("The x axis points upwards")
                maalt = 0
                print("maalt er",maalt)
                sleep(1)
            elif(acceleration.x < 0 and maalt == 0):
                maalt = maalt +1    
                print("The x axis points downwards")
                count = count +1
                print(count, 'x')
                print("maalt er",maalt)
                tm.show(str(count)+ "TK")
                sleep(1)
        

        if abs(acceleration.y) > 0.8:
            if (acceleration.y > 0 and maalt == 0):
                print("The y axis points upwards")
                count = count +1
                maalt = maalt +1
                print(count, 'y')
                tm.show(str(count)+ "TK")
                print("maalt er",maalt)
                sleep(1)
            elif(acceleration.y < 0 and maalt == 0):
                maalt = maalt +1    
                print("The y axis points downwards")
                count = count +1
                print(count, 'y')
                print("maalt er",maalt)
                tm.show(str(count)+ "TK")
                sleep(1)


        if abs(acceleration.z) > 0.8:
            if (acceleration.z > 0 and maalt == 0):
                print("The z axis points upwards")
                count = count +1
                maalt = maalt +1
                print("maalt er", maalt)
                print(count, 'z')
                tm.show(str(count)+ "TK")
                sleep(1)
            elif(acceleration.z < 0 and maalt == 0):   
                print("The z axis points downwards")
                maalt = maalt +1 
                count = count +1
                print("maalt er", maalt)
                print(count, 'z')
                print("maalt er",maalt)
                tm.show(str(count)+ "TK")
                sleep(1)
      
