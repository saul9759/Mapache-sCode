import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://192.168.100.89:8000',)

print("----------------------READDIR------------------------")
print(s.readdir())
input()
input()

print("-----------------------CREATE------------------------")
print(s.create("Archivo1.txt"))
input()
input()

print("-----------------------WRITE-------------------------")
print(s.write("Archivo1.txt", "Soy un parrafo bonito"))
input()
input()

print("-----------------------READ--------------------------")
print(s.read("Archivo1.txt"))
input()
input()

print("----------------------READDIR------------------------")
print(s.readdir())
input()
input()

print("-----------------------MKDIR------------------------")
print(s.mkdir("CarpetaFea"))
input()
input()

print("----------------------READDIR-------------------------")
print(s.readdir())
input()
input()

print("----------------------RENAME--------------------------")
print(s.rename("CarpetaFea", "CarpetaBonita"))
input()
input()

print("----------------------READDIR-------------------------")
print(s.readdir())
input()
input()

print("-----------------------RMDIR--------------------------")
print(s.rmdir("CarpetaBonita"))
input()
input()

print("----------------------READDIR-------------------------")
print(s.readdir())
input()
input()


print("------------------------CD----------------------------")
print(s.cd(".."))
input()
input()

print("----------------------READDIR-------------------------")
print(s.readdir())
input()
input()

print("-----------------------MKDIR--------------------------")
print(s.mkdir("NuevosArchivosRPC"))
input()
input()

print("----------------------READDIR-------------------------")
print(s.readdir())
input()
input()

print("------------------------CD----------------------------")
print(s.cd("/home/daxtex/PycharmProjects/Mapache-sCode/Practica5/NuevosArchivosRPC"))
input()
input()

print("-----------------------CREATE-------------------------")
print(s.create("NuevoArchivo1.txt"))
input()
input()

print("-----------------------MKDIR--------------------------")
print(s.mkdir("NuevaCarpetaBonita"))
input()
input()

print("-----------------------READDIR------------------------")
print(s.readdir())
input()
input()