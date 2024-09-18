from alumno import Alumno

class Grupo:
    def __init__(self, seccion, grado):
        self.seccion = seccion  
        self.grado = grado  
        self.alumnos = []

    def agregar_alumno(self, alumno: Alumno):
        self.alumnos.append(alumno)

    def mostrar_alumnos(self):
        if not self.alumnos:
            print(f'No hay alumnos en el grupo {self.seccion} - {self.grado}')
        else:
            print(f'Alumnos del grupo {self.seccion}-{self.grado}:')
            for alumno in self.alumnos:
                print(alumno)

if __name__ == "__main__":
    alumno1 = Alumno("Juan", "Pérez", "García", "CURP123", "M123")
    alumno2 = Alumno("Ana", "López", "Martínez", "CURP456", "M456")
    alumno3 = Alumno("Luis", "Ramírez", "Torres", "CURP789", "M789")
    
    alumno4 = Alumno("Carlos", "Díaz", "Hernández", "CURP321", "M321")
    alumno5 = Alumno("María", "González", "Sánchez", "CURP654", "M654")
    alumno6 = Alumno("Sofía", "Martínez", "Fernández", "CURP987", "M987")

    grupo1 = Grupo("A", 1)
    grupo1.agregar_alumno(alumno1)
    grupo1.agregar_alumno(alumno2)
    grupo1.agregar_alumno(alumno3)

    grupo2 = Grupo("B", 2)  
    grupo2.agregar_alumno(alumno4)
    grupo2.agregar_alumno(alumno5)
    grupo2.agregar_alumno(alumno6)

    print("Datos del Grupo 1:")
    grupo1.mostrar_alumnos()

    print("\nDatos del Grupo 2:")
    grupo2.mostrar_alumnos()
