# Anthony Krivonos
# server.py
# 07/13/2018

# MARK: - Imports

import os
import sys
import socket

from utility import *
from environment import *
from models.block import *
from models.blockchain import *
from models.broadcastthread import *
from models.clientthread import *

# MARK: - Initialize the Blockchain Server

def initialize():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(MAXIMUM_CONNECTIONS)
    return serverSocket

# MARK: - Run the Blockchain Server

def run(serverSocket):
    broadcastThread = BroadcastThread(clients, blockchain)
    broadcastThread.start()

    while True:
        connection, address = serverSocket.accept()
        print('Client at ' + str(address) + ' connected')
        client = ClientThread(connection, address, BUFFER_SIZE, blockchain)
        client.start()
        clients.append(client)

# MARK: - Terminate the Blockchain Server

def terminate():
    try:
        for client in clients:
            client.terminate()
        sys.exit(0)
    except SystemExit:
        os._exit(0)

# MARK: - Start Server

if __name__ == '__main__':
    print('Initializing Blockchain Server on Host ' + str(HOST) + ' and Port ' + str(PORT) + '...')

    # MARK: - Initialize genesis block and chain

    try:
        clients = []
        serverSocket = initialize()
        blockchain = Blockchain()
        blockchain.add(Block(0, getCurrentTime(), '', '', '', 'GENESIS'))
        print('Server ready...')
        run(serverSocket)
    except socket.error:
        print('Connection failure. Exiting...')
        terminate()
    except KeyboardInterrupt:
        print('\nInterrupted. Exiting...')
        terminate()
