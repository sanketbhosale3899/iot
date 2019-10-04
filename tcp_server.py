import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setwarnings(False)

UDP_IP='192.168.0.80'
UDP_PORT=5007
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data,addr = sock.recvfrom(1024)
    d = int(data)
    if d==1:
        GPIO.output(12,GPIO.HIGH)
    elif d==0:
        GPIO.output(12,GPIO.LOW)

    print("Receiver Message : ",data)
