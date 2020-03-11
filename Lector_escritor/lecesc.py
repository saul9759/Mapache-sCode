import threading
import time
import random

from aptdaemon.lock import acquire


def worker(barrier, lock, arreglo):
    print(threading.current_thread().name,'Esperando {} escritores '.format(barrier.n_waiting))
    worker_id = barrier.wait()
    print(threading.current_thread().name, 'Inicio escritor', worker_id)

    print ("Escribiendo")
    lock.acquire()
    try:
        for i in range(10):
            arreglo.append(random.randint(1, 500))
            time.sleep(.2)
    finally:
        lock.release()
        print(threading.current_thread().name, "Finalizo escritor ", worker_id)

def leer(lock, arreglo):
    while lock.locked() != True:
        print('Lector', threading.current_thread().name)
        print("---------------------------------------")
        for i in range(len(arreglo)):
                print(arreglo[i])
                time.sleep(.2)
# Escritores
NUM_THREADS = 2
lectores = 3

lock = threading.Lock()
arreglo = []

barrier = threading.Barrier(NUM_THREADS)

threads = [threading.Thread(target=worker, args=(barrier, lock, arreglo), ) for i in range(NUM_THREADS)]

lectos = [threading.Thread(target=leer, args=(lock, arreglo), ) for i in range(lectores)]

for t in threads:
    print(t.name, 'Iniciando Escritor')
    t.start()
    time.sleep(0.1)
for t in threads:
    t.join()

for t in lectos:
    print(t.name, 'Iniciando Lector')
    t.start()
    time.sleep(0.1)
for t in lectos:
    t.join()


