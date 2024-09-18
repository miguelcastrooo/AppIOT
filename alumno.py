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
        if nombre:
            self.nombre = nombre
        if apaterno:
            self.apaterno = apaterno
        if amaterno:
            self.amaterno = amaterno
        if curp:
            self.curp = curp
        if matricula:
            self.matricula = matricula
        print(f"Se ha editado el alumno con la matricula {self.matricula}.")
        print(f"--------------------------------------------")


def eliminar_alumno(lista_alumnos, matricula):
    for alumno in lista_alumnos:
        if alumno.matricula == matricula:
            lista_alumnos.remove(alumno)
            return


if __name__ == "__main__":
    lista_alumnos = [
        Alumno("Juan", "Pérez", "García", "CURP123", "M123"),
        Alumno("Ana", "López", "Martínez", "CURP456", "M456"),
        Alumno("Luis", "Ramírez", "Torres", "CURP789", "M789"),
        Alumno("Carlos", "Díaz", "Hernández", "CURP000", "M000"),
        Alumno("María", "González", "Sánchez", "CURP001", "M001"),
        Alumno("Sofía", "Martínez", "Fernández", "CURP002", "M002")
    ]

    print("Lista de Alumnos: ")
    for i, alumno in enumerate(lista_alumnos):
        print(f"{i}. {alumno}")


    indice_editar = 0 
    print(f"\nEditando el alumno numero {indice_editar}")
    lista_alumnos[indice_editar].editar(nombre="Juan Carlossssssss", curp="CURP1234")  

    print("\nLista actualizada:")
    for i, alumno in enumerate(lista_alumnos):
        print(f"{i}. {alumno}")

    matricula_eliminar = "M002"  # Aquí se coloca la matrícula del alumno a eliminar
    print(f"\nAlumno con matrícula {matricula_eliminar} eliminado")
    eliminar_alumno(lista_alumnos, matricula_eliminar)

    print("\nLista actualizada:")
    for i, alumno in enumerate(lista_alumnos):
        print(f"{i}. {alumno}")
