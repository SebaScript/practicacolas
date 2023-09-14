class ColaDePrioridad:
    def __init__(self):
        self.solicitudes: list[dict] = []
        self.contador: int = 0
        self.longitud: int = 0

    def esta_vacia(self) -> bool:
        return self.longitud == 0

    def reordenar_cola(self):
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
        for solicitud in self.solicitudes:
            if solicitud["ID"] == id:
                solicitud["urgencia"] = nueva_emergencia
                self.reordenar_cola()
                break

    def cargar_solicitudes_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(', ')
                print(datos)
                numero_solicitud, nombre_cliente, descripcion, urgencia = datos
                print(nombre_cliente)
                urgencia = int(urgencia.rstrip('"'))
                self.agregar_solicitud(nombre_cliente, descripcion, urgencia)

    def atender_solicitudes_automaticamente(self):
        while not self.esta_vacia():
            self.atender_solicitud()


cola = ColaDePrioridad()

nombre_archivo = "solicitudes.txt"
cola.cargar_solicitudes_desde_archivo(nombre_archivo)

cola.mostrar_solicitudes()
cola.atender_solicitudes_automaticamente()
