# Anthony Krivonos
# models/clientthread.py
# 07/13/2018

# MARK: - Imports

import os
import sys
import socket
import time

from threading import Thread, Lock

from utility import *
from models.blockchain import *

# MARK: - ClientThread

class ClientThread(Thread):

    # Initialize the Broadcast Thread
    def __init__(self, connection, address, bufferSize, blockchain):
        super(ClientThread, self).__init__()
        self.connection = connection
        self.address = address
        self.bufferSize = bufferSize
        self.blockchain = blockchain
        self.live = True
        self.lock = Lock()

    # Run the thread
    def run(self):
        while self.live:
            clientMessage = self.connection.recv(self.bufferSize).decode('utf-8')
            serverMessage = ''
            if len(clientMessage) > 0:
                serverMessage = self.handleRequest(clientMessage)
                self.send(serverMessage)
        print('Client at ' + str(self.address) + ' disconnected...')

    # Send a message
    def send(self, message):
        self.connection.send(message.encode())

    # Terminate the Thread Loop
    def terminate(self):
        self.live = False
        self.connection.close()

    # Handle a Request
    def handleRequest(self, request = ''):
        fields = request.split(',')

        # Continue if there are fewer than 3 provided fields
        if len(fields) < 3:
            return 'ERROR: Invalid request.'

        fromWallet = hash(fields[0])
        toWallet = hash(fields[1])
        transactionAmount = hash(fields[2])

        self.lock.acquire()
        success = self.processBlock(fromWallet, toWallet, transactionAmount)
        self.lock.release()

        if success:
            print('The blockchain now contains ' + str(self.blockchain.len()) + ' blocks.')
            msg = 'Sent ' + transactionAmount + ' from ' + fromWallet + ' to ' + transactionAmount + '\n'
            msg += 'Block successfully created\n'
        else:
            msg = 'ERROR: Block creation failed.\n'

        return msg

    # Process a New Block
    def processBlock(self, fromWallet, toWallet, transactionAmount):
        lastBlock = self.blockchain.last()
        newBlock = self.blockchain.last().generateNewBlock(fromWallet, toWallet, transactionAmount)

        # Validate block in the chain
        if not newBlock.isValid(self.blockchain.last()):
            return False

        # If valid, add the new block to a longer chain
        newBlockchain = self.blockchain.add(newBlock)
        self.blockchain.replaceIfNeeded(newBlockchain)
        return True
