import socket
import xlwt
from xlwt import Workbook

wb = Workbook()
def server_program():

    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    sheet1 = wb.add_sheet("JDMeter")

    style = xlwt.easyxf('font: bold 1, color red;')

    sheet1.write(0, 0, 'R', style)
    sheet1.write(0, 1, 'G')
    sheet1.write(0, 2, 'B')
    sheet1.write(0, 3, 'Result')
    rgb = []
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        rgb = data.split(' ')
        print("from connected user: ",rgb)
        ###########################################
        sum = 0
        for i in rgb:
            sum = sum + int(i)
        print(sum)
        ############################################
        # Writting on specified sheet
        sheet1.write(1, 1, rgb[0])
        sheet1.write(2, 1, rgb[1])
        sheet1.write(3, 1, rgb[2])
        sheet1.write(4,1, sum)

        wb.save('Readings.csv')
        ############################################
        data = 'recieved'
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()