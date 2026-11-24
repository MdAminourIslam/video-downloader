#!/bin/bash
cd "$(dirname "$0")"
pip3 install -r requirements.txt
echo "Starting server... Open http://localhost:8000 in your browser."
python3 server.py
