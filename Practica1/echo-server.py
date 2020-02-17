#!/usr/bin/env python3
from datetime import datetime
import socket
import time
import random
HOST = "10.100.78.15"  # Standard loopback interface address (localhost)
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
            # generacion dinamica para avanzado y minas aleatorias
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
            # print("Enviando respuesta a", Client_addr)
            # print("Estado: sendall\nMensaje: PSH,ACK\n\n")
            # principiante

            tablero = []

            x = 0
            y = 0
            tam = 0
            min =0
            numt = 0

            instanteInicial = datetime.now()
            # --------------------------------Principiante----------------------------------------
            if int(data) == 1:
                tam = 9
                min = 10
                numt = 71
            else:
                tam = 16
                min = 40
                numt = 216
            # Generar bombas
            x1 =0
            y1=0
            cont =0
            while True:
                x = random.randrange(tam)
                y = random.randrange(tam)
                if str(tB[x][y]) == "0":
                    tB[x][y] = "*";
                    cont = cont+1
                if cont == min:
                    break

            while True:
                for i in range(tam):
                    for j in range(tam):
                        if str(tB[i][j]) == "*":
                            men += "0 "
                        else:
                            men += str(tB[i][j])+" "
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
                if tB[x-1][y-1] == "X":
                    flag = False
                    print("Tiro "+str(x)+","+str(y)+" repetido")
                elif tB[x-1][y-1] == "*":
                    flag = True
                    tB[x - 1][y - 1] = "X*"
                    numt = numt - 1

                else:
                    flag = False
                    tB[x - 1][y - 1] = "X"
                    numt = numt - 1
                # si perdioperdio
                if flag:
                    print("Valio, perdiste")
                    # TCPClientSocket.sendall(b"PERDISTE")

                    men = "PERDISTE"
                    Client_conn.sendall(men.encode('utf-8'))
                    men = ""
                    for i in range(tam):
                        for j in range(tam):
                            men += str(tB[i][j]) + " "
                        men += "\n"
                    Client_conn.sendall(men.encode('utf-8'))
                    men = ""

                    break
                if numt == 0:
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

