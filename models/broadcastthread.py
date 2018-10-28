# Anthony Krivonos
# models/broadcastthread.py
# 07/13/2018

# MARK: - Imports

import os
import sys
import socket
import time

from threading import Thread

from utility import *
from models.blockchain import *

# MARK: - BroadcastThread

class BroadcastThread(Thread):

    # Initialize the Broadcast Thread
    def __init__(self, clients, blockchain, broadcastInterval = 20):
        super(BroadcastThread, self).__init__()
        self.live = True
        self.clients = clients
        self.blockchain = blockchain
        self.broadcastInterval = broadcastInterval

    # Run the thread
    def run(self):
        while self.live:
            time.sleep(self.broadcastInterval)
            self.broadcast()

    # Broadcast the thread to each client
    def broadcast(self):
        for client in self.clients:
            try:
                client.send(prettifyJSON(self.blockchain.toString(), 4))
            except socket.error:
                client.live = False
                continue

    # Terminate the Thread Loop
    def terminate(self):
        self.live = False
