# Raspberry Pi to Arduino !2C Communication
import smbus
import time

# Addresses for Arduinos
ARDUINO_1_ADDRESS = 0x04 #Address of Arduino 1
ARDUINO_2_ADDRESS = 0x05 #Address of Arduino 2
ARDUINO_3_ADDRESS = 0x06 #Address of Arduino 3

# Create the I2C bus
bus = smbus.SMBus(1)

#
def writeNumber(value):
    bus.write_byte(ARDUINO_1_ADDRESS, int(value))
    return -1

def readNumber():
    number = bus.read_byte(ARDUINO_1_ADDRESS)
    return number

while True:
    var = input("Enter Arduino (1-6): ")
    if not var:
        continue

    # Message from RPI to Itsy for request
    writeNumber(var)
    print("RPI: Hi Itsy, I sent you ", var)

    # Sleep one second
    time.sleep(1)

    # Reply from Itsy for result
    number = readNumber()
    print("Itsy: Hey RPI, I received a digit ", number)