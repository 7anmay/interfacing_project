import socket # for socket
import sys
import time
import xlwt
from xlwt import Workbook
import csv

#wb = Workbook()
#sheet1 = wb.add_sheet("data")
print ("fetching file data")
file = "testlogfile-copy.txt"
b_val = "100"
sb_val = str(b_val)
f = open(file,'w')
f.write(sb_val)
f.close()
'''
host = ""
port = 5000

server = socket.socket()
server.bind((host,port))

conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))
'''
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created\n")
except socket.error as err:
	print ("socket creation failed with error %s\n" %(err))
# default port for socket
port = 5000
host_ip = '127.0.0.1'
# connecting to the server
#s.connect((host_ip, port))

while True:
    try:
        s.connect((host_ip, port))
        print ("the socket has successfully connected to the web page\n")
        break
    except ConnectionRefusedError:
        print("trying connection")

msg = "Ready"
s.send(msg.encode())
err = "zero_error"
i = 0
while 1:
    time.sleep(1)
    data = s.recv(1024).decode()
    if not data:
        i = i+1
        print("waiting for response\n")
    else:
        print("uploading measuremets\n")
        print("recieved:", data )
        if (b_val != 0  ):
            #s.send(str(b_val))
            sheet1.write(0, 0, b_val)
            sheet1.write(0, 1, 0)
            sheet1.write(0, 2, 0)
            wb.save("D:\XAMPP\htdocs\includes\data.csv")
        else:
            s.send(err)
    if i==20:
        print("time out\n")
        break

s.close()