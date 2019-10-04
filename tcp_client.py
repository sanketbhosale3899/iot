import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

UDP_IP='192.168.1.10'
UDP_PORT=5007

while True:
    number=int(input("Enter num :"))
    sock.sendto(str(number).encode('UTF-8'),(UDP_IP,UDP_PORT))
    if number>1:
        break
