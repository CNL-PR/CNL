####client###

import socket

def main():
    host = '127.0.0.1'  # Server IP
    port = 12000

    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((host, port))
    print("Connected to server. \n")

    while True:
        # Client sends message
        client_msg = input("Client msg: ")
        cs.sendall(client_msg.encode('utf-8'))

        if client_msg.lower() == "exit":
            print("\n")
            break

        # Receive server reply
        data = cs.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Server: {data}")

        if data.lower() == "exit":
            print("\n")
            break

    cs.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()	
