#!/usr/bin/env python3 

# echo-client.py 

import socket

HOST = "127.0.0.1"

PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # - Data is exchanged

    s.sendall(b"Hello world")
    data = s.recv(1024)

print(f"Recieved {data}")