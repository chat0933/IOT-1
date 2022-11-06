from time import sleep
from machine import Pin, ADC
import umqtt_robust2 as mqtt
import tm1637
import _thread

tm = tm1637.TM1637(clk=Pin(32), dio=Pin(33))

analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)

def volt_start_thread():
    print("thread")
    _thread.start_new_thread(volt_measure, ())
    print("volt started")


def volt_measure():
    while True:
            analog_val = analog_pin.read()
            m_spaending = analog_val/4095*3.3 #4095 er BAUD max værdien for ESP analog måling, og 3.3 er spændingen på ESP analog 3.3Vpin. m_spaending = målt spænding.
            print("Analog maalt vaerdi: ", m_spaending)
            spaending = m_spaending * 5
            print("Input spaending: ", spaending)
            battery_percentage = spaending/8.4 *100  #8.4 er vores max spænding for alle batterier tilsammen i serie (2 LiPo Batterier).
            battery_percentage = int(battery_percentage)
            print("the battery percentage is:", battery_percentage, "%")
            tm.show(str(battery_percentage)+ " p")
            mqtt.web_print(str(battery_percentage), 'Greeznerd/feeds/batteri')
            sleep(30)