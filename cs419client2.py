import socket 
import threading
username = input("Enter username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
#connect client to server, local host
#TODO ask user for ip/port and not have it hard-coded in 
client.connect(('127.0.0.1', 5555))                             
#receive message
def receive_message():
    while True:                                                 
        #make connection, send username if applicable, else print message 
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'USERNAME':
                client.send(username.encode('ascii'))
            else:
                print(message)
        #error, wrong ip or port
        except:                                                 
            print("Error, wrong ip or port")
            client.close()
            break
#write message
def write_message():
    while True:                                                 
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('ascii'))

#reveive messages
receive_thread = threading.Thread(target=receive_message)               
receive_thread.start()
#send messages
write_thread = threading.Thread(target=write_message)                   
write_thread.start()