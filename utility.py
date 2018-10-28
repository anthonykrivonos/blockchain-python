# Anthony Krivonos
# utility.py
# 07/13/2018

# MARK: - Imports

import hashlib
import time
import calendar
import json

# MARK: - Utility

# Hash strings using SHA256
def hash(str):
    return hashlib.sha256(str.encode('utf-8')).hexdigest()

# Get the system's timestamp as a string
def getCurrentTime():
    return str(calendar.timegm(time.gmtime()))

# Return pretty JSON string from a JSON object
def prettifyJSON(jsonObject, indent):
    return json.dumps(jsonObject, indent=indent, sort_keys=False)
