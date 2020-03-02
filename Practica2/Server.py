# !/usr/bin/env python3

import socket
import sys
import threading
import random
from datetime import datetime
buffer_size = 1024
tB = []
perdio = False

def servirPorSiempre(socketTcp, listaconexiones):
    try:
        while True:
            client_conn, client_addr = socketTcp.accept()
            print("Conectado a", client_addr)
            listaconexiones.append(client_conn)
            thread_read = threading.Thread(target=recibir_datos, args=[client_conn, client_addr])
            thread_read.start()
            gestion_conexiones(listaConexiones)
    except Exception as e:
        print(e)

def gestion_conexiones(listaconexiones):
    for conn in listaconexiones:
        if conn.fileno() == -1:
            listaconexiones.remove(conn)
    print("hilos activos:", threading.active_count())
    print("enum", threading.enumerate())
    print("conexiones: ", len(listaconexiones))
    print(listaconexiones)


def recibir_datos(client_conn, client_addr):
    try:
        cur_thread = threading.current_thread()
        print("Recibiendo datos del cliente {} en el {}".format(client_addr, cur_thread.name))
        # -------------------------------------------------------------------------------------------------------------
        while True:
            men = ""
            # print("Esperando a recibir datos...")
            data = client_conn.recv(buffer_size)
            print("Dificultad elegida: ,", data," de ", client_addr)
            if not data:
                break
            
            x = 0
            y = 0
            tam = 0
            min =0
            numt = 0

            instanteInicial = datetime.now()
            # --------------------------------Principiante----------------------------------------
            # Determina dificultad
            if int(data) == 1:
                tam = 9
                min = 10
                numt = 71
                primlin = "  1 2 3 4 5 6 7 8 9\n"
            else:
                tam = 16
                min = 40
                numt = 216
                primlin = "  1 2 3 4 5 6 7 8 9 10111213141516\n"
            # Genera tablero
            for i in range(tam):
                tB.append([])
                for j in range(tam):
                    tB[i].append("0")
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
            # General el mensaje para el cliente con el tablero

            while True:
                men += primlin
                for i in range(tam):
                    men += str(i+1)+" "
                    for j in range(tam):
                        if str(tB[i][j]) == "*":
                            men += "0 "
                        else:
                            men += str(tB[i][j])+" "
                    men +="\n"
                print(men +"\n")
                client_conn.sendall(men.encode('utf-8'))
                men = ""
                print("Esperando x")
                data = client_conn.recv(buffer_size)
                x = int(data)
                print("Esperando y")
                data = client_conn.recv(buffer_size)
                y = int(data)
                print(str(x)+","+str(y))
                # evaluar bomba
                global perdio
                flag = True
                if  perdio == False:
                    if tB[x-1][y-1] == "X" :
                        flag = False
                        print("Tiro "+str(x)+","+str(y)+" repetido")
                    elif tB[x-1][y-1] == "*":
                        flag = True
                        perdio = True
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

                    men = "PERDISTE\n"
                    client_conn.sendall(men.encode('utf-8'))
                    men = ""
                    men += primlin
                    for i in range(tam):
                        men += str(i + 1) + " "
                        for j in range(tam):
                            men += str(tB[i][j]) + " "
                        men += "\n"
                    client_conn.sendall(men.encode('utf-8'))
                    men = ""

                    break
                if numt == 0:
                    # TCPClientSocket.sendall(b"GANASTE")


                    men = "GANASTE\n"
                    client_conn.sendall(men.encode('utf-8'))
                    men = ""
                    men += primlin
                    for i in range(len(tB)):
                        men += str(i + 1) + " "
                        for j in range(len(tB[i])):
                            men += str(tB[i][j]) + " "
                        men += "\n"
                    client_conn.sendall(men.encode('utf-8'))

            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial  # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            print("Tiempo final: "+str(segundos)+" segundos")

        # -------------------------------------------------------------------------------------------------------------


    except Exception as e:
        print(e)
    finally:
        client_conn.close()



listaConexiones = []
host, port, numConn = sys.argv[1:4]

if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "<host> <port> <num_connections>")
    sys.exit(1)

serveraddr = (host, int(port))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:

    # TCPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPServerSocket.bind(serveraddr)
    TCPServerSocket.listen(int(numConn))
    print("El servidor TCP está disponible y en espera de solicitudes")

    servirPorSiempre(TCPServerSocket, listaConexiones)
