# Anthony Krivonos
# client.py
# 07/13/2018

# MARK: - Imports

import socket
import select
import os
import sys
import argparse

from utility import *
from environment import *

# MARK: - Client-server interaction

def initialize():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    return clientSocket

# MARK: - Check for invalid inputs

def run(clientSocket):
    while True:
        socketList = [sys.stdin, clientSocket]
        readSockets, writeSockets, errorSockets = select.select(socketList, [], [])
        # Read sockets from server
        for socket in readSockets:
            if socket == clientSocket:
                readFromServer()
            else:
                userInput = readInput()
                error = userInput[0]
                if error is None:
                    message = userInput[1]
                    send(clientSocket, message)
                else:
                    print(error)


# MARK: - Read Message from Server

def readFromServer():
    data = clientSocket.recv(BUFFER_SIZE).decode('utf-8')
    if data is None:
        raise socket.error
    else:
        print(data)

# MARK: - Read Input from Console

def readInput():
    fromWallet = None
    toWallet = None
    transactionAmount = None
    message = None
    out = None

    parser = argparse.ArgumentParser(description='Process blockchain transaction.')
    parser.add_argument('-f', help='fromWallet')
    parser.add_argument('-t', help='toWallet')
    parser.add_argument('-a', help='transactionAmount')

    args = parser.parse_args()

    fromWallet = args.f or ""
    toWallet = args.t or ""
    transactionAmount = args.a or ""

    message = fromWallet + "," + toWallet + "," + transactionAmount

    return (out, message, fromWallet, toWallet, transactionAmount)

# MARK: - Send Message Packet to Server

def send(socket, message):
    socket.send(message.encode())

# MARK: - Terminate the Blockchain Client

def terminate():
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

# MARK: - Start Client

if __name__ == '__main__':
    print('Connecting to Blockchain Host ' + str(HOST) + ' on Port ' + str(PORT) + '...')

    try:
        clientSocket = initialize()
        print('Client started...')
        run(clientSocket)
    except socket.error:
        print('Connection failure. Exiting...')
        terminate()
    except KeyboardInterrupt:
        print('\nInterrupted. Exiting...')
        terminate()
