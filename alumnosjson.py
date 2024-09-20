import json

class Alumno:
    def __init__(self, nombre, apaterno, amaterno, curp, matricula):
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.curp = curp
        self.matricula = matricula

    def __str__(self):
        return f'{self.nombre} {self.apaterno} {self.amaterno} - {self.curp} - {self.matricula}'

    def editar(self, nombre=None, apaterno=None, amaterno=None, curp=None, matricula=None):
        nuevo_alumno = Alumno(
            nombre or self.nombre,
            apaterno or self.apaterno,
            amaterno or self.amaterno,
            curp or self.curp,
            matricula or self.matricula
        )
        return nuevo_alumno

lista_alumnos = []

def crear_alumno(nombre, apaterno, amaterno, curp, matricula):
    nuevo_alumno = Alumno(nombre, apaterno, amaterno, curp, matricula)
    lista_alumnos.append(nuevo_alumno)
    print(f"Alumno {nombre} creado y agregado a la lista.")

def editar_alumno(matricula, **nuevos_datos):
    for i, alumno in enumerate(lista_alumnos):
        if alumno.matricula == matricula:
            lista_alumnos[i] = alumno.editar(**nuevos_datos)
            print(f"Alumno con matrícula {matricula} editado.")
            return
    print(f"Alumno con matrícula {matricula} no encontrado.")

def eliminar_alumno(matricula):
    global lista_alumnos
    lista_alumnos = [alumno for alumno in lista_alumnos if alumno.matricula != matricula]
    print(f"Alumno con matrícula {matricula} eliminado.")

def mostrar_alumnos():
    if lista_alumnos:
        print("\nLista de Alumnos:")
        for alumno in lista_alumnos:
            print(alumno)
    else:
        print("No hay alumnos en la lista.")

def guardar_alumnos(archivo):
    alumnos_dict = [alumno.__dict__ for alumno in lista_alumnos]
    with open(archivo, 'w') as f:
        json.dump(alumnos_dict, f, indent=4)
    print(f"Lista de alumnos guardada en {archivo}.")

def cargar_alumnos(archivo):
    global lista_alumnos
    with open(archivo, 'r') as f:
        alumnos_dict = json.load(f)
        lista_alumnos = [Alumno(**datos) for datos in alumnos_dict]
    print(f"Lista de alumnos cargada desde {archivo}.")

if __name__ == "__main__":
    # Ejemplo de uso
    crear_alumno("Diego", "Cisneros", "Adame", "0001", "D001")
    crear_alumno("Jose", "Mercado", "Franco", "0002", "D002")
    crear_alumno("Miguel", "Castro", "Mesta", "0003", "M003")

    mostrar_alumnos()

    editar_alumno("D001", nombre="Ivan", curp="0000")
    
    mostrar_alumnos()

    eliminar_alumno("D002")

    mostrar_alumnos()

    # Guardar y cargar la lista de alumnos
    guardar_alumnos("alumnos.json")
    cargar_alumnos("alumnos.json")
    mostrar_alumnos()
