import RPi.GPIO as GPIO
import serial
import time,sys

SERIAL_PORT = "/dev/ttyAMA0"
ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)

ser.write(str.encode("AT+CMGF=1\r"))
time.sleep(1)
ser.write(str.encode('AT+CMGS="+639652605024"\r'))
msg = "Baby on Board"
print("Sending message...")
time.sleep(1)
ser.write(str.encode(msg+chr(26)))
time.sleep(1)
print("Message sent...")