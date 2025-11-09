###udp client###

import socket
import os

SERVER_IP = '127.0.0.1'
PORT = 8885
BUFSIZE = 503

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    fname = input("Enter filename with extension: ")

    if not os.path.exists(fname):
        print("File not found!")
        return

    # Send filename
    s.sendto(fname.encode(), (SERVER_IP, PORT))

    # Send file size
    size = os.path.getsize(fname)
    s.sendto(str(size).encode(), (SERVER_IP, PORT))
    print(f"File size: {size} bytes")

    # Send file content
    with open(fname, "rb") as f:
        data = f.read(BUFSIZE)
        while data:
            s.sendto(data, (SERVER_IP, PORT))
            data = f.read(BUFSIZE)

    print("File sent successfully.")
    s.close()

if __name__ == "__main__":
    main()
