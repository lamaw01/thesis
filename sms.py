import RPi.GPIO as GPIO
import serial
import time,sys

SERIAL_PORT = "/dev/ttyAMA0"
ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)

ser.write(str.encode("AT+CMGF=1\r"))
print("Text mode enabled...")
time.sleep(2)
ser.write(str.encode('AT+CMGS="+639652605024"\r'))
msg = "Baby on Board"
print("sending message...")
time.sleep(2)
ser.write(str.encode(msg+chr(26)))
time.sleep(2)
print("message sent..")