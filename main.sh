#!/bin/bash

# Define the port your server uses
PORT=8888

# Check if something is using the port and kill it
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
    echo "Port $PORT is in use, killing the process..."
    lsof -ti :$PORT | xargs kill -9
    echo "Process killed."
    # Give it a moment to fully release
    sleep 1
fi

python3 src/main.py
cd public && python3 -m http.server 8888