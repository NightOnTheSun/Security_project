import socket
import select
import sys
import threading
import re
import pymongo
""" 
 1. User created: username + ip -> store in database 
 2. user starts chat: add desired members by username -> send message get number associated with 
    with the chat. e.g., 0001
 3. send message to chat: 0001 message! -> server lookup chat number 0001 for list of participants 
    -> send that message to all participants with the same format. 
4. error handling: if chat is closed remove user from the 0001 list of participants. 
5. Encryption: not sure yet! 
 """

def create_socket():
    """
    Creates a socket
    :return: cs: created socket
    """
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return server
    except socket.error as err:
        print('socket open error: {}'.format(err))
        sys.exit()


def initialize_server_socket(server: socket, ip: str, port: int):
    """
    This function initializes the socket with commandline args. Will work given an IP or
    a host name as the ip param.
    :param server: the newly created socket
    :param ip: ip address of the server or host name
    :param port: port to bind this socket to
    :return: Initialized server socket
    """
    if re.search('[a-zA-Z]', ip):
        host_ip = socket.gethostbyname(ip)
        server_binding = (host_ip, port)
        server.connect(server_binding)
    else:
        server.bind((ip, port))


"""
Message format: We would like there to be some identifying info about which 
chat the message is to be associated with. A lookup of the chat id will say which 
people to send message to. 
format: 4 diget number followed by a space then message 
0001 apples taste good! 
"""


def client_thread(conn: socket, addr: str, chats: dict) -> None:
    """
    This function listens for messages from a perticular user and routs the message
    to the appropriate chat by using the 4 digit number preceding the message.
    Send message with username... we should store the mapping somewhere...
    :param conn: the socket for chat room
    :param addr: address of user who sent message
    :param chats: a dictionary of arrays of users to send messages to based on chat number
    :return: None
    """
    conn.send("Welcome to the chat!")


if __name__ == "__main__":
    """ Below write commandline interface stuff and error handling """
    # TODO: Write some print statements so that this this running will look nicer in terminal

    server = create_socket()
    initialize_server_socket(server, 'ilab4.cs.rutgers.edu', 8080)
    """ We'd like a hashtable of pairs of connections to manage the connections """
