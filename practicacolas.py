class ColaDePrioridad:
    def __init__(self):
        self.solicitudes = []
        self.contador = 0
        self.longitud = 0

    def esta_vacia(self):
        return self.longitud == 0

    def reordenar_cola(self):
        urgencia = self.solicitudes[0]["urgencia"]
        self.solicitudes.sort(key=lambda x: x["urgencia"], reverse=True)

    def agregar_solicitud(self, nombre, descripcion, urgencia):
        solicitud = {
            "ID": self.contador,
            "nombre_cliente": nombre,
            "descripcion": descripcion,
            "urgencia": urgencia
        }
        self.contador += 1
        self.longitud += 1
        self.solicitudes.append(solicitud)
        self.reordenar_cola()

    def atender_solicitud(self):
        if not self.esta_vacia():
            solicitud_atendida = self.solicitudes.pop(0)
            self.longitud -= 1
            print(f"ID: {solicitud_atendida['ID']}")
            print(f"Nombre del cliente: {solicitud_atendida['nombre_cliente']}")
            print(f"Descripción del problema: {solicitud_atendida['descripcion']}")
            print(f"Nivel de urgencia: {solicitud_atendida['urgencia']}")
            print("-" * 20)
            return
        else:
            return None

    def mostrar_solicitudes(self):
        for solicitud in self.solicitudes:
            print(f"ID: {solicitud['ID']}")
            print(f"Nombre del cliente: {solicitud['nombre_cliente']}")
            print(f"Descripción del problema: {solicitud['descripcion']}")
            print(f"Nivel de urgencia: {solicitud['urgencia']}")
            print("-" * 20)

    def actualizar_urgencia(self, id, nueva_emergencia):
        for i in self.solicitudes:
            if i["ID"] == id:
                i["urgencia"] = nueva_emergencia
                self.reordenar_cola()
                break


import random
import time


tinicial = time.time()


def generar_solicitudes(cola, numero_solicitudes):
    nombre = "a"
    descripcion = "b"
    for i in range(numero_solicitudes):
        urgencia = random.randint(1, 10)
        cola.agregar_solicitud(nombre, descripcion, urgencia)


cola = ColaDePrioridad()
generar_solicitudes(cola, 10000)

cola.mostrar_solicitudes()

tfinal = time.time()
ttotal = tfinal - tinicial
print(ttotal)
