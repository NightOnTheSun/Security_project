import socket
import threading                                                

#local host
host = '127.0.0.1'  
#unreserved port                                                   
port = 5555                                                             

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                               
server.listen()

#lists of clients accessing server and current usernames
clientList = []
usernameList = []

def send_message(message):                                                
    for client in clientList:
        client.send(message)

#client handler: receive and send client messages and check if they left. If left, then remove from lists
def client_handler(client):                                         
    while True:
        try:                                                            
            message = client.recv(1024)
            send_message(message)
        except:                                                         
            clientIndex = clientList.index(client)
            clientList.remove(client)
            client.close()
            username = usernameList[clientIndex]
            send_message('{} left'.format(username).encode('ascii'))
            usernameList.remove(username)
            break

#receive clients, enter into clientList and usernameList
def receive():                                                          
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))   

        client.send('USERNAME'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernameList.append(username)
        clientList.append(client)
        print("Username is {}".format(username))
        
        #TODO give each user unique id, probably set id to a counter
        
        send_message("{} joined".format(username).encode('ascii'))
        client.send('Connected to server'.encode('ascii'))
        thread = threading.Thread(target=client_handler, args=(client,))
        thread.start()

receive()