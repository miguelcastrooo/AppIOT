from alumno import Alumno
from lista import Lista

class Grupo:
    def __init__(self, grado=None, seccion=None):
        self.grado = grado
        self.seccion = seccion
        self.alumnos = Lista()  

    def add_alumno(self, alumno):
        self.alumnos.add(alumno)

    def edit_alumno(self, idx, alumno):
        self.alumnos.edit(idx, alumno)

    def get_alumnos(self):
        return self.alumnos.get_all()

    def __repr__(self):
        return f"Grupo: {self.grado} {self.seccion}"

grupo1 = Grupo("7mo", "A")
grupo1.add_alumno(Alumno("Mario", "Garcia", "Rodriguez", "0001", "A0001"))
grupo1.add_alumno(Alumno("Gabriela", "Zamora", "Hernandez", "0002", "A0002"))

print(grupo1)
for alumno in grupo1.get_alumnos():
    print(alumno)
