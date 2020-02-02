import RPi.GPIO as GPIO
import serial
import time,sys

# recipient = "+639652605024"

f = open("contact.txt", "r")

if f.mode == 'r':
    recipient = f.read()

f.close()

SERIAL_PORT = "/dev/ttyAMA0"
ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)

ser.write(str.encode("AT+CMGF=1\r"))
time.sleep(1)
ser.write(str.encode('AT+CMGS="'+ recipient +'"\r'))
msg = "Baby on Board"
print("Sending message..." + recipient)
time.sleep(1)
ser.write(str.encode(msg+chr(26)))
time.sleep(1)
print("Message sent...")