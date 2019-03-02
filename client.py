import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc only for now
    port = 5000

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input("->") #take input values
    print(message)

    #message = [255,0,255]

    client_socket.send(message.encode())  # send message

    data = client_socket.recv(1024).decode() # receive response

    if(data == "recieved"):
        print('Received from server: ' + data)  # show in terminal

    #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()