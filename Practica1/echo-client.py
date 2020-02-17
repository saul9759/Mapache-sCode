#!/usr/bin/env python3

import socket

HOST = "10.100.78.15"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    # print("Estado: Connect\nMensaje: SYN\n\n")
    TCPClientSocket.connect((HOST, PORT))
    print("Conexion establecida...")
    print("Que nivel desea:\n\t1: Principiante \n\t2: Avanzado")
    op =0
    # print("Estado: sendall\nMensaje:PSH,ACK\n\n")
    op = input()
    # TCPClientSocket.sendall(b"1")
    TCPClientSocket.sendall(op.encode('utf-8'))
    # print("Esperando una respuesta...")
    #data = TCPClientSocket.recv(buffer_size)
    # print(data.decode('utf-8'), "\nDe", TCPClientSocket.getpeername())
    x = 0
    y = 0
    while True:

        data = TCPClientSocket.recv(buffer_size)
        if data.decode('utf-8') == "PERDISTE":
            data = TCPClientSocket.recv(buffer_size)
            print(data.decode('utf-8'))
            break
        elif data.decode('utf-8') == "GANASTE":
            data = TCPClientSocket.recv(buffer_size)
            print(data.decode('utf-8'))
            break
        else:
            print(data.decode('utf-8'))
            print("Hora de elegir tiro...\n\t")
            print("Digite corde1nada x\n\t")
            x = input()
            TCPClientSocket.sendall(x.encode('utf-8'))
            print("Digite cordenada y\n")
            y = input()
            TCPClientSocket.sendall(y.encode('utf-8'))

    # print("Estado: Close\nMensaje: FIN, ACK\n\n")