# Anthony Krivonos
# models/block.py
# 07/13/2018

# MARK: - Imports

import os
import sys

from utility import *
from models.block import *

# MARK: - Blockchain

class Blockchain:

    # Initialize Blockchain with a chain, or a list of concurrent blocks
    def __init__(self):
        self.chain = []

    # Compare two
    def replaceIfNeeded(self, otherBlockchain):
        if otherBlockchain.len() > self.len():
            self.chain = otherBlockchain.chain

    # Get length of blockchain
    def len(self):
        return len(self.chain)

    # Add block to the end of the blockchain
    def add(self, block):
        self.chain.append(block)
        return self

    # Get first block or None
    def first(self):
        return self.chain[0] if self.len() > 0 else None

    # Get last block or None
    def last(self):
        return self.chain[self.len() - 1] if self.len() > 0 else None

    # Convert blockchain into outputtable string
    def toString(self):
        blocks = []
        for block in self.chain:
            blocks.append(block.toString())
        return blocks
