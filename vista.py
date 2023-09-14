from practicacolas import ColaDePrioridad


class VistaColaDePrioridad:
    def __init__(self):
        self.cola = ColaDePrioridad()

    def mostrar_menu(self):
        print("Sistema de atención al cliente")
        while True:
            print("\n==== Menú ====")
            print("1. Agregar Solicitud")
            print("2. Atender Solicitud")
            print("3. Mostrar Solicitudes")
            print("4. Actualizar Urgencia")
            print("5. Salir")

            opcion = input("Ingrese su opción: ")
            print("\n")

            if opcion == "1":
                nombre = input("Ingrese el nombre del cliente: ")
                descripcion = input("Ingrese la descripción del problema: ")

                while True:
                    try:
                        urgencia = int(input("Ingrese el nivel de urgencia (1-5): "))
                        if 1 <= urgencia <= 10:
                            break
                        else:
                            print("La urgencia debe estar en el rango de 1 a 5. Por favor ingresela de nuevo.")
                    except ValueError:
                        print("Por favor ingrese un número válido de urgencia.")

                self.cola.agregar_solicitud(nombre, descripcion, urgencia)

            elif opcion == "2":
                if not self.cola.esta_vacia():
                    self.cola.atender_solicitud()
                else:
                    print("No hay solicitudes en este momento")

            elif opcion == "3":
                if not self.cola.esta_vacia():
                    self.cola.mostrar_solicitudes()
                else:
                    print("No hay solicitudes en este momento")

            elif opcion == "4":
                while True:
                    try:
                        id = int(input("Ingrese el ID de la solicitud: "))
                        nueva_urgencia = int(input("Ingrese la nueva urgencia (1-5): "))
                        if 1 <= nueva_urgencia <= 5:
                            self.cola.actualizar_urgencia(id, nueva_urgencia)
                            break
                    except ValueError:
                        print("Por favor ingrese un numero valido de urgencia")

            elif opcion == "5":
                break

            else:
                print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    vista = VistaColaDePrioridad()
    vista.mostrar_menu()
