#!/usr/local/bin/python3

import socket

host = '127.0.0.1'
port = 80

# create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host, port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

client.sendto("TESTING STRING",(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)

print data
