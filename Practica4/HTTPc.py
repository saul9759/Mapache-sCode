import http.client
import urllib.parse
import socket
import sys

def enviar(conn, Metodo, A):
    conn.request(Metodo, A)
    rsp = conn.getresponse()
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)

HOST = "192.168.100.19"
PORT = "8080"
conn = http.client.HTTPConnection(HOST, PORT)
print("******************GET*******************")

enviar(conn, "GET", "wea.html") #Solicitud get correcta
tecla = sys.stdin.read(1)
print("******************HEAD******************")
enviar(conn, "HEAD", "wea.html") #Solicitud HEAD correcta
tecla = sys.stdin.read(1)
print("******************POST******************")

params = urllib.parse.urlencode({'n1': 123, 'n2': 456})
headers = {"Content-type": "text/plain"}
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
tecla = sys.stdin.read(1)

print("**************Put****************")
f = open("Archivos/bonita.html")
body = f.read()
f.close()
conn.request("PUT", "wea.html", body)
response = conn.getresponse()
print(response.status, response.reason)
tecla = sys.stdin.read(1)

print("**************DELETE****************")
enviar(conn, "DELETE", "basura.txt")
tecla = sys.stdin.read(1)

print("**************CONNECT****************")
conn.request("CONNECT", "wea.html")
response = conn.getresponse()
print(response.status, response.reason)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = (HOST, 9000)
sock.connect(server_address)
data = sock.recv(16)
print(data)
tecla = sys.stdin.read(1)
print("**************OPTIONS****************")
enviar(conn, "OPTIONS", "wea.txt")
tecla = sys.stdin.read(1)

print("**************TRACE****************")
enviar(conn, "TRACE", "Algo")
tecla = sys.stdin.read(1)

print("**************PATCH****************")
body = "#p1 {color: #ea0c0c;}" #rojo
conn.request("PATCH", "estilacho.css", body)
response = conn.getresponse()
print(response.status, response.reason)
tecla = sys.stdin.read(1)

body = "#p2 {color: #53dc0e;}" #verde
conn.request("PATCH", "estilacho.css", body)
response = conn.getresponse()
print(response.status, response.reason)
tecla = sys.stdin.read(1)

body = "#p3 {color: #d8129d;}" #rosa
conn.request("PATCH", "estilacho.css", body)
response = conn.getresponse()
print(response.status, response.reason)
tecla = sys.stdin.read(1)

print("**************Put****************")
f = open("Archivos/weacopia.html")
body = f.read()
f.close()
conn.request("PUT", "wea.html", body)
response = conn.getresponse()
print(response.status, response.reason)
tecla = sys.stdin.read(1)


conn.close()