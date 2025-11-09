###udp server###
import socket

SERVER_IP = '127.0.0.1'
PORT = 8885
BUFSIZE = 503

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((SERVER_IP, PORT))
    print(f"Server started on {SERVER_IP}:{PORT}")
    print("Waiting for file info...")

    # Receive file name
    fname, addr = s.recvfrom(1024)
    fname = fname.decode()
    print(f"Receiving file: {fname}")

    # Receive file size
    size_data, addr = s.recvfrom(1024)
    file_size = int(size_data.decode())
    print(f"File size: {file_size} bytes")

    # Open file to write
    with open("received_" + fname, "wb") as f:
        bytes_received = 0
        while bytes_received < file_size:
            data, addr = s.recvfrom(BUFSIZE)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)
            print(f"Received {bytes_received}/{file_size} bytes", end='\r')

    print(f"\nFile received successfully as 'received_{fname}'")
    s.close()

if __name__ == "__main__":
    main()

