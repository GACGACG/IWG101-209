import machine
import utime

sensorTemp=machine.ADC(4)
conversionFactor = 3.3 / 65365

while True:
    rawValue = sensorTemp.read_u16() * conversionFactor
    
    temperature = 27 - (rawValue - 0.706) / 0.001721
    
    print(temperature)
    
    utime.sleep(0.5)
