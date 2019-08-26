# Raspberry Pi to Arduino !2C Communication
import smbus
import time

# Addresses for Arduinos
ARDUINO_1_ADDRESS = 0x04 #Address of Arduino 1
ARDUINO_2_ADDRESS = 0x05 #Address of Arduino 2
ARDUINO_3_ADDRESS = 0x06 #Address of Arduino 3

# Create the I2C bus
bus = smbus.SMBus(1)

arduinoSelect = int(input("Select Arduino (1-3): "))
powerSelect = input ("On or Off (on/off): ")

if arduinoSelect == 1:
    SlaveAddress = ARDUINO_1_ADDRESS
elif arduinoSelect == 2:
    SlaveAddress = ARDUINO_2_ADDRESS
elif arduinoSelect == 3:
    SlaveAddress = ARDUINO_3_ADDRESS
else:
    # Quit if error
    print("Error when selecting Arduino")
    quit()

# Quit if no imput for power
if powerSelect != "on" or powerSelect != "off":
    print("No input for power")
    #quit()

# This function converts a string to an array of bytes.
def ConvertStringsToBytes(src):
    #b = bytearray()
    #b.extend(map(ord, src))
    
    converted = []
    for b in src:
        converted.append(map(ord, b))
        
    print(converted)
    return converted

BytesToSend = ConvertStringsToBytes(powerSelect)
I2Cbus.write_i2c_block_data(SlaveAddress, 0x00, BytesToSend)
print("Sent " + SlaveAddress + " the " + powerSelect + " command.")
