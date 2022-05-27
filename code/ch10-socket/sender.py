import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('', 6000))

s.sendto(sys.argv[1].encode() , ("127.0.0.1" ,7000)) #119.23.235.40

s.close( )
