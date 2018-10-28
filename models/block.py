# Anthony Krivonos
# models/block.py
# 07/13/2018

# MARK: - Imports

import os
import sys

from utility import *

# MARK: - Block

class Block:

    # Initialize Block
    def __init__(self, index, timestamp, fromWallet, toWallet, transactionAmount, prevHash):
        self.index = index
        self.timestamp = timestamp
        self.fromWallet = fromWallet
        self.toWallet = toWallet
        self.transactionAmount = transactionAmount
        self.prevHash = prevHash
        self.hash = self.calculateHash()

    # Get block hash by concatenating properties
    def calculateHash(self):
        return hash(str(self.index) + str(self.timestamp) + str(self.fromWallet) + str(self.toWallet) + str(self.transactionAmount) + str(self.prevHash))

    # Create a new block from previous self block
    def generateNewBlock(self, fromWallet, toWallet, transactionAmount):
        return Block(self.index + 1, getCurrentTime(), fromWallet, toWallet, transactionAmount, self.hash)

    # Check block's validity
    def isValid(self, oldBlock):
        return oldBlock.index + 1 == self.index and oldBlock.hash == self.prevHash and self.calculateHash() == self.hash

    # Convert the block into JSON string format
    def toString(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'fromWallet': self.fromWallet,
            'toWallet': self.toWallet,
            'transactionAmount': self.transactionAmount,
            'prevHash': self.prevHash,
            'hash': self.hash
        }
