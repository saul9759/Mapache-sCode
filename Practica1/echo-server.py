#!/usr/bin/env python3
from datetime import datetime
import socket
import time
HOST = "192.168.100.20"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
buffer_size = 1024
men = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("Estado: Espera\nMensaje: Escuchando\n\n")
    print("El servidor TCP está disponible y en espera de solicitudes")

    Client_conn, Client_addr = TCPServerSocket.accept()
    # print("Estado: \nMensaje:\n\n")
    with Client_conn:
        print("Conectado a", Client_addr)
        # print("Estado: Conectado\nMensaje:\n\n")
        while True:
            # print("Esperando a recibir datos...")
            data = Client_conn.recv(buffer_size)
            print("Dificultad elegida: ,", data," de ", Client_addr)
            if not data:
                break
            # principiante
            tA = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]

            tAM = [["*", "", "", "", "", "", "", "", "*"],
                  ["", "*", "", "", "", "", "", "", ""],
                  ["", "", "*", "", "", "", "", "", ""],
                  ["", "", "", "*", "", "", "", "", ""],
                  ["", "", "", "", "*", "", "", "", ""],
                  ["", "", "", "", "", "*", "", "", ""],
                  ["", "", "", "", "", "", "*", "", ""],
                  ["", "", "", "", "", "", "", "*", ""],
                  ["", "", "", "", "", "", "", "", "*"]]
            # avanzado
            tB = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]
            tBM = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "*"],
                  ["", "*", "", "", "", "", "", "", "", "", "", "", "", "", "*", "*"],
                  ["", "", "*", "", "", "", "", "", "", "", "", "", "", "*", "", "*"],
                  ["", "", "", "*", "", "", "", "", "", "", "", "", "*", "", "", "*"],
                  ["", "", "", "", "*", "", "", "", "", "", "", "*", "", "", "", "*"],
                  ["", "", "", "", "", "*", "", "", "", "", "*", "", "", "", "", "*"],
                  ["", "", "", "", "", "", "*", "", "", "*", "", "", "", "", "", "*"],
                  ["", "", "", "", "", "", "", "*", "*", "", "", "", "", "", "", "*"],
                  ["", "", "", "", "", "", "", "*", "*", "", "", "", "", "", "", "*"],
                  ["", "", "", "", "", "", "*", "", "", "*", "", "", "", "", "", ""],
                  ["", "", "", "", "", "*", "", "", "", "", "*", "", "", "", "", ""],
                  ["", "", "", "", "*", "", "", "", "", "", "", "*", "", "", "", ""],
                  ["", "", "", "*", "", "", "", "", "", "", "", "", "*", "", "", ""],
                  ["", "", "*", "", "", "", "", "", "", "", "", "", "", "*", "", ""],
                  ["", "*", "", "", "", "", "", "", "", "", "", "", "", "", "*", ""],
                  ["*", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "*"]]
            # print("Enviando respuesta a", Client_addr)
            # print("Estado: sendall\nMensaje: PSH,ACK\n\n")
            # principiante
            x = 0
            y = 0
            numtP = 71
            numtA = 216
            instanteInicial = datetime.now()
            # --------------------------------Principiante----------------------------------------
            if int(data) == 1:

                while True:
                    for i in range(len(tA)):
                        for j in range(len(tA[i])):
                            men += str(tA[i][j])+" "
                        men +="\n"
                    print(men +"\n")
                    Client_conn.sendall(men.encode('utf-8'))
                    men = ""
                    print("Esperando x")
                    data = Client_conn.recv(buffer_size)
                    x = int(data)
                    print("Esperando y")
                    data = Client_conn.recv(buffer_size)
                    y = int(data)
                    print(str(x)+","+str(y))
                    # evaluar bomba
                    flag = True
                    if tAM[x-1][y-1] == "*":
                        flag = True
                        tA[x - 1][y - 1] = "X"
                        numtP = numtP - 1

                    else:
                        flag = False
                        tA[x - 1][y - 1] = "X"
                        numtP = numtP-1
                    # si perdioperdio
                    if flag:
                        print("Valio, perdiste")
                        # TCPClientSocket.sendall(b"PERDISTE")

                        men = "PERDISTE"
                        Client_conn.sendall(men.encode('utf-8'))
                        men = ""
                        for i in range(len(tA)):
                            for j in range(len(tA[i])):
                                men += str(tA[i][j]) + str(tAM[i][j]) + " "
                            men += "\n"
                        Client_conn.sendall(men.encode('utf-8'))
                        men = ""

                        break
                    if numtP == 0:
                        # TCPClientSocket.sendall(b"GANASTE")


                        men = "GANASTE"
                        Client_conn.sendall(men.encode('utf-8'))
                        men = ""
                        for i in range(len(tA)):
                            for j in range(len(tA[i])):
                                men += str(tA[i][j]) + " "
                            men += "\n"
                        Client_conn.sendall(men.encode('utf-8'))

            # --------------------------------Avanzado----------------------------------------
            else:
                while True:
                    for i in range(len(tB)):
                        for j in range(len(tB[i])):
                            men += str(tB[i][j]) + " "
                        men += "\n"
                    print(men + "\n")
                    Client_conn.sendall(men.encode('utf-8'))
                    men = ""
                    print("Esperando x")
                    data = Client_conn.recv(buffer_size)
                    x = int(data)
                    print("Esperando y")
                    data = Client_conn.recv(buffer_size)
                    y = int(data)
                    print(str(x) + "," + str(y))
                    # evaluar bomba
                    flag = True
                    if tBM[x - 1][y - 1] == "*":
                        flag = True
                        tB[x - 1][y - 1] = "X"
                        numtA = numtA - 1

                    else:
                        flag = False
                        tB[x - 1][y - 1] = "X"
                        numtA = numtA - 1
                    # si perdioperdio
                    if flag:
                        print("Valio, perdiste")
                        # TCPClientSocket.sendall(b"PERDISTE")

                        men = "PERDISTE"
                        Client_conn.sendall(men.encode('utf-8'))
                        men = ""
                        for i in range(len(tB)):
                            for j in range(len(tB[i])):
                                men += str(tB[i][j]) + str(tBM[i][j]) + " "
                            men += "\n"
                        Client_conn.sendall(men.encode('utf-8'))
                        men = ""

                        break
                    if numtA == 0:
                        # TCPClientSocket.sendall(b"GANASTE")

                        men = "GANASTE"
                        Client_conn.sendall(men.encode('utf-8'))
                        men = ""
                        for i in range(len(tB)):
                            for j in range(len(tB[i])):
                                men += str(tB[i][j]) + " "
                            men += "\n"
                        Client_conn.sendall(men.encode('utf-8'))

            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial  # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            print("Tiempo final: "+str(segundos)+" segundos")

            # print("Estado: Close\nMensaje: FIN, ACK\n\n")

