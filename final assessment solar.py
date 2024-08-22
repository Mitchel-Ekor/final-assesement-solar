

from machine import Pin, I2C, ADC 

import utime 
import lcd_api 
import pico_I2C_lcd import I2C 


I2C = I2C(0, scl=Pin(1), sda=Pin(0),freq=4000000)


lcd = I2CcLcd(i2c, 0x27, 2, 16)


analogue_to_digital_convertor = ADC(Pin(26))


vref = 3.3 
analogue_to_digital_convertor_resolution = 65535 


timestamps = (1)
voltage = (1)



def calculate_voltage():
    raw_data = analogue_to_digital_convertor.read _u16()
    voltage = (raw_data / analogue_to_digital_convertor_resolution)* vref 
    return voltage

def append_data_to_file(timestamp_str,voltage):
    try:
        with open("votage_data.csv", "a") as data_file 
             data_file.write("{}. {:.2f}\n".format(timestamp_str, voltage))
    except Exception as e:
        print("Error writing to file:("e)

def_main():
    while True:
        voltage = calculate_volatge()
        
        lcd.clear()
        
        lcd.puster("Voltage:(:2f)V".format(voltage)) 
        
        
        
        timestamp = utime.loclatime()
        timestamp_atr = "(:04d)-(:02d)-(:02d) (:02d):(:02d):(02d)".format(timestamp[0],timestamp[1],timestamp[2],
                                                                          timestamp[3],timestamp[4],timestamp[5])
        
        print("Timestamp: (), Voltage: (:.2f)V".format(timestamp_str, voltage))
        
        
        
        data_file = open("voltage_data_csv", "w")
        data_file.write("Timestamp, Voltage\n")
        
        
        data_file.write("{}, {:2f)\n".format(timestamp_str,voltage))
        data_file.flush() 
        
        append_data_ro_file(timestamp_str, voltage)
        
        
        utime.sleep(1)
        
        led = Pin(5, Pin.OUT)
        
        
        led.value(1)
        
        utime.sleep(1)
        
        led.value(0)
        
        utime.sleep(1)
                
try:
    main()
except KeyboardInterrupt:
    print("Program Interrupted")
