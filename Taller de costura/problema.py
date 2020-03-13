import threading
import time

from aptdaemon.lock import acquire

def makemanga(lock, mangas):
    while True:
        while not lock.locked():
            mangas[0] += 1
            if mangas[0] == 10:
                lock.acquire()
                print("Cesto de Mangas lleno con " + str(mangas[0])+" mangas\n")

def makecuerpo(lock1, cuerpo):
    while True:
        while not lock1.locked():
            cuerpo[0] += 1
            if cuerpo[0] == 5:
                lock1.acquire()
                print("Cesto de Cuerpos lleno con " + str(cuerpo[0]) + " cuerpos\n")


def makeprenda(lock, lock1, mangas, cuerpo, completo):
    while True:
        while lock.locked() and lock1.locked():
            mangas[0] -= 2
            cuerpo[0] -= 1
            completo[0] += 1
            print("--------------------------------------------------")
            print("Mangas restantes:"+str(mangas[0]))
            print("Cuerpos restantes:" + str(cuerpo[0]))
            print("Chamarras terminadas: "+str(completo[0]))
            print("--------------------------------------------------")
            time.sleep(3)
            lock.release()
            lock1.release()



# trabajadores 1 2 y 3
t1 = 1
t2 = 1
t3 = 1

# cestas
mangas = [0]
cuerpo = [0]
complet = [0]

lock = threading.Lock()
lock1 = threading.Lock()

mang = [threading.Thread(target=makemanga, args=(lock, mangas), ) for i in range(t1)]

cuerp = [threading.Thread(target=makecuerpo, args=(lock1, cuerpo), ) for i in range(t2)]

prenda = [threading.Thread(target=makeprenda, args=(lock, lock1, mangas, cuerpo, complet), ) for i in range(t3)]

for t in mang:
    t.start()

for t in cuerp:
    t.start()

for t in prenda:
    t.start()

