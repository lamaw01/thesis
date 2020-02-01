import RPi.GPIO as GPIO
import serial
import time,sys

SERIAL_PORT = "/dev/ttyAMA0"
ser = serial.Serial(SERIAL_PORT,baudrate = 9600,timeout=5)

ser.write(str.encode("ATD+639652605024;\r"))
print("Dialing...")
time.sleep(30)
ser.write(str.encode("ATH\r"))
print("Hanging up...")