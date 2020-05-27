from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import socket
import os
r = os.getcwd()
#-------------------------Carpeta de trabajo----------------------------
carpeta = "/ArchivosRPC"

ruta = r+carpeta

os.chdir(ruta)
try:
    os.mkdir(ruta)
except OSError:
    print("-")
else:
    print("-")

#----------------------------------------------------------------------


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(("192.168.100.89", 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    class Operaciones:
        def create(self, name):

            try:
                open(name, "x")
            except OSError:
                men = "El archivo "+name+" ya existe"
            else:
                men = "El archivo "+name+" fue creado"
            return men

        def read(self, name):

            try:
                f = open(name, "r")
            except OSError:
                men = "El archivo "+name+" no existe"
            else:
                men = f.read()
                f.close()
            return men

        def write(self, name, text):

            try:
                f = open(name, "w")
            except OSError:
                men = "Ocurrio un error"
            else:
                f.write(text)
                f.close()
                men = "Se escribio correctamente en el archivo "+name

            return men

        def rename(self, dir, name):
            try:
                os.rename(dir, name)
            except OSError:
                men = "Error: "+dir+" no existe en "+ruta
            else:
                men = "La carpeta "+dir+" fue renombrada a "+name+" exitosamente"
            return men

        def mkdir(self, dir):
            try:
                os.mkdir(dir)
            except OSError:
                men = "La carpeta "+dir+" ya existe"
            else:
                men = "La carpeta " + dir + " se creo exitosamente"
            return men

        def rmdir(self, dir):

            try:
                os.rmdir(dir)
            except OSError:
                men = "La carpeta "+dir+" no existe"
            else:
                men = "La carpeta "+dir+" se borro exitosamente"
            return men

        def readdir(self):

            men = os.listdir(ruta)
            return men

        def cd(self, nrut):
            global ruta
            try:
                os.chdir(nrut)
            except OSError:
                men= "La ruta "+nrut+" no existe"
            else:

                ruta = os.getcwd()
            men = "Directorio cambiado a "+ruta
            return men


    server.register_instance(Operaciones())
    server.serve_forever()
