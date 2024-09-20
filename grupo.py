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

