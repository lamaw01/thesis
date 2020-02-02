import RPi.GPIO as GPIO
import serial
import time,sys

# recipient = '+639652605024'

f = open("contact.txt", "r")

if f.mode == 'r':
    recipient = f.read()

f.close()

SERIAL_PORT = "/dev/ttyAMA0"
ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)

# ser.write(str.encode("ATD+639652605024;\r"))
ser.write(str.encode('ATD'+recipient +';\r'))
print("Dialing..." + recipient)
time.sleep(24)
ser.write(str.encode("ATH\r"))
print("Hanging up...")