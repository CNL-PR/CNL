#####client###

import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = '127.0.0.1'   # Server IP address
port = 12000         # Server port

s.connect((host, port))
s.send(b"Hello server!")  # Send bytes, not string

with open('received_file.txt', 'wb') as f:
    print('File opened for writing...')
    while True:
        print('Receiving data...')
        data = s.recv(65536)
        if not data:
            break
        f.write(data)
    print('File received successfully.')

s.close()
print('Connection closed.')

