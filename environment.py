# Anthony Krivonos
# server.py
# 07/13/2018

# MARK: - Imports

import os
from os.path import join, dirname
from dotenv import Dotenv

# MARK: - Set .env Path

dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env")) # Of course, replace by your correct path
os.environ.update(dotenv)

# MARK: - Environment Variables

HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
BUFFER_SIZE = int(os.environ.get("BUFFER_SIZE"))
MAXIMUM_CONNECTIONS = int(os.environ.get("MAXIMUM_CONNECTIONS"))
