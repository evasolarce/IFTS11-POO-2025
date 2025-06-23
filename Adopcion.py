import uuid

class Perro:
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, temperamento):
        self.id = str(uuid.uuid4())[:8]
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = 'disponible'
        self.temperamento = temperamento

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ['disponible', 'reservado', 'adoptado']:
            self.estado = nuevo_estado

    def mostrar_info(self):
        return f"{self.nombre} ({self.raza}) - {self.edad} años, {self.tamaño}, Salud: {self.estado_salud}, Vacunado: {self.vacunado}, Estado: {self.estado}, ID: {self.id}"


# usuario

class UsuarioAdoptante:
    def __init__(self, nombre, dni, email, preferencias):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias  # dict: {'raza': ..., 'edad': ..., 'tamaño': ...}
        self.historial_adopciones = []

    def modificar_datos(self, nombre=None, email=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email

    def ver_historial(self):
        if not self.historial_adopciones:
            return "No ha realizado adopciones."
        return "\n".join([f"{perro.nombre} ({perro.raza})" for perro in self.historial_adopciones])

#sitema

class SistemaAdopcion:
    def __init__(self):
        self.perros = []
        self.usuarios = []

    def cargar_perro(self, perro):
        self.perros.append(perro)

    def eliminar_perro(self, perro_id):
        self.perros = [p for p in self.perros if p.id != perro_id]

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, dni):
        return next((u for u in self.usuarios if u.dni == dni), None)

    def postular_adopcion(self, perro_id, usuario):
        perro = self.buscar_perro(perro_id)
        if perro and perro.estado == 'disponible':
            perro.cambiar_estado('reservado')
            return True
        return False

    def confirmar_adopcion(self, perro_id, usuario):
        perro = self.buscar_perro(perro_id)
        if perro and perro.estado == 'reservado':
            perro.cambiar_estado('adoptado')
            usuario.historial_adopciones.append(perro)
            return True
        return False

    def buscar_perro(self, perro_id):
        return next((p for p in self.perros if p.id == perro_id), None)

    def sugerir_perros(self, preferencias):
        sugerencias = self.perros
        for clave, valor in preferencias.items():
            if valor:
                sugerencias = [p for p in sugerencias if getattr(p, clave) == valor and p.estado == 'disponible']
        return sugerencias

    def mostrar_perros(self, estado=None):
        lista = [p for p in self.perros if p.estado == estado] if estado else self.perros
        return "\n".join([p.mostrar_info() for p in lista]) or "No hay perros disponibles."

    def mostrar_perros_por_usuario(self, usuario):
        return usuario.ver_historial()

#interfaz

def menu():
    sistema = SistemaAdopcion()

    while True:
        print("\n--- MENÚ SISTEMA DE ADOPCIÓN ---")
        print("1. Registrar usuario")
        print("2. Cargar perro")
        print("3. Buscar perro por preferencias")
        print("4. Postular adopción")
        print("5. Confirmar adopción")
        print("6. Ver perros disponibles")
        print("7. Ver historial de adopciones")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            email = input("Email: ")
            raza = input("Pref. raza (opcional): ")
            edad = input("Pref. edad (opcional): ")
            tamaño = input("Pref. tamaño (opcional): ")
            preferencias = {'raza': raza or None, 'edad': int(edad) if edad else None, 'tamaño': tamaño or None}
            usuario = UsuarioAdoptante(nombre, dni, email, preferencias)
            sistema.registrar_usuario(usuario)
            print("Usuario registrado.")

        elif opcion == "2":
            nombre = input("Nombre del perro: ")
            raza = input("Raza: ")
            edad = int(input("Edad: "))
            tamaño = input("Tamaño: ")
            peso = float(input("Peso (kg): "))
            estado_salud = input("Estado de salud: ")
            vacunado = input("¿Vacunado? (s/n): ") == 's'
            temperamento = input("Temperamento: ")
            perro = Perro(nombre, raza, edad, tamaño, peso, estado_salud, vacunado, temperamento)
            sistema.cargar_perro(perro)
            print(f"Perro cargado con ID: {perro.id}")

        elif opcion == "3":
            dni = input("DNI del usuario: ")
            usuario = sistema.buscar_usuario(dni)
            if usuario:
                sugerencias = sistema.sugerir_perros(usuario.preferencias)
                if sugerencias:
                    print("🐾 Perros sugeridos:")
                    for p in sugerencias:
                        print(p.mostrar_info())
                else:
                    print("No hay perros que coincidan con las preferencias.")
            else:
                print("Usuario no encontrado.")

        elif opcion == "4":
            dni = input("DNI del usuario: ")
            perro_id = input("ID del perro: ")
            usuario = sistema.buscar_usuario(dni)
            if usuario and sistema.postular_adopcion(perro_id, usuario):
                print("Postulación registrada. Estado del perro: reservado.")
            else:
                print("Falló la postulación.")

        elif opcion == "5":
            dni = input("DNI del usuario: ")
            perro_id = input("ID del perro: ")
            usuario = sistema.buscar_usuario(dni)
            if usuario and sistema.confirmar_adopcion(perro_id, usuario):
                print("Adopción confirmada.")
            else:
                print("Falló la adopción.")

        elif opcion == "6":
            print(sistema.mostrar_perros(estado='disponible'))

        elif opcion == "7":
            dni = input("DNI del usuario: ")
            usuario = sistema.buscar_usuario(dni)
            if usuario:
                print(usuario.ver_historial())
            else:
                print("Usuario no encontrado.")

        elif opcion == "8":
            print("👋 ¡Gracias por usar el sistema de adopción!")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
