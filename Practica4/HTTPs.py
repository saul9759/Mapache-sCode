import http.server
import socket
from os import remove
from http.server import BaseHTTPRequestHandler, HTTPServer


#class GetHandler(BaseHTTPRequestHandler):
class GetHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open("Archivos/" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            men = f.read()
            self.wfile.write(men.encode('utf-8'))
            f.close()
        except IOError:
            self.send_error(404)

    def do_HEAD(self):
        try:
            f = open("Archivos/" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            men = f.read()
            self.wfile.write(men.encode('utf-8'))
            f.close()
        except IOError:
            self.send_error(404)

    def do_POST(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            men = "Recibidos"
            self.wfile.write(men.encode('utf-8'))
        except IOError:
            self.send_error(404)

    def do_PUT(self):
        try:
            self.send_response(200)
            length = int(self.headers['Content-Length'])
            content = self.rfile.read(length)
            f = open("Archivos/" + self.path, 'wb')
            f.write(content)
            f.close()

            self.send_header('Content-type', 'text-html')
            self.end_headers()
            men = "Recibidos"
            self.wfile.write(men.encode('utf-8'))
        except IOError:
            self.send_error(404)

    def do_DELETE(self):
        try:
            self.send_response(200)
            remove("Archivos/" + self.path)

            self.send_header('Content-type', 'text-html')
            self.end_headers()
            men = "Archivo eliminado"
            self.wfile.write(men.encode('utf-8'))
        except IOError:
            self.send_error(404)
    def do_CONNECT(self):
        try:
            self.send_response(200)
            men = "Exito"
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            self.wfile.write(men.encode('utf-8'))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (HOST, 9000)
            sock.bind(server_address)
            sock.listen(1)
            print("Esperando conexion")
            connection, client_address = sock.accept()
            data = "HOLA"
            connection.sendall(data.encode('utf-8'))
            print("Conexion de ejemplo realizada, cerrando conexion")
            connection.close()
        except IOError:
            self.send_error(404)
    def do_OPTIONS(self):
        try:
            self.send_response(200)
            men = "Opciones: \n GET, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE y PATCH"
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            self.wfile.write(men.encode('utf-8'))

        except IOError:
            self.send_error(404)
    def do_TRACE(self):
        try:
            self.send_response(200)
            men = ""+self.path
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            self.wfile.write(men.encode('utf-8'))
        except IOError:
            self.send_error(404)

    def do_PATCH(self):
        try:
            self.send_response(200)
            length = int(self.headers['Content-Length'])
            content = self.rfile.read(length)
            f = open("Archivos/" + self.path, "a")
            f.write(content.decode('utf-8'))
            f.close()
            self.send_header('Content-type', 'text-html')
            self.end_headers()
            men = "Archivo actualizado"
            self.wfile.write(men.encode('utf-8'))

        except IOError:
            self.send_error(404)
if __name__ == '__main__':
    from http.server import HTTPServer

    HOST = '192.168.100.19'
    PORT = 8080
    server = HTTPServer((HOST, PORT), GetHandler)
    print('Starting server')
    server.serve_forever()
