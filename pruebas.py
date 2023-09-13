import random
from practicacolas import ColaDePrioridad
import time

tinicial = time.time()


def generar_solicitudes(cola, numero_solicitudes):
    nombre = "a"
    descripcion = "b"
    for i in range(numero_solicitudes):
        urgencia = random.randint(1, 10)
        cola.agregar_solicitud(nombre, descripcion, urgencia)


cola = ColaDePrioridad()
generar_solicitudes(cola, 5)


print("\n ******************************************+ \n")

cola.mostrar_solicitudes()

tfinal = time.time()
ttotal = tfinal-tinicial
print(ttotal)
