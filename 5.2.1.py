#####server file transfer##
import socket  # Import socket module
s = socket.socket()
host = '127.0.0.1'
port = 12000

s.bind((host, port))
s.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)

    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = 'myfile.txt'
    f = open(filename, 'rb')
    l = f.read(65536)
    while l:
        conn.sendall(l)
        print('Sent', repr(l))
        l = f.read(65536)

    f.close()
    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()

