#####server hello###

import socket

def main():
    host = '127.0.0.1'
    port = 12000

    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ss.bind((host, port))
    ss.listen(1)

    print("Server started and waiting for client connection...")
    conn, addr = ss.accept()
    print(f"Connected to client: {addr}")

    conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    while True:
        # Receive message from client
        client_msg = conn.recv(1024).decode('utf-8')
        if not client_msg:
            break
        print(f"\nClient: {client_msg}")

        # Check for exit condition
        if client_msg.lower() == "exit":
            print("\n")
            break

        # Server sends reply
        server_msg = input("Server msg: ")
        conn.sendall(server_msg.encode('utf-8'))

        if server_msg.lower() == "exit":
            print("\n")
            break

    conn.close()
    ss.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()

