from alumno import Alumno
from grupo import Grupo
from lista import Lista

class Carrera:
    def __init__(self, nombre=None, clave=None):
        self.nombre = nombre
        self.clave = clave
        self.grupos = Lista()  

    def add_grupo(self, grupo):
        self.grupos.add(grupo)

    def edit_grupo(self, idx, grupo):
        self.grupos.edit(idx, grupo)

    def get_grupos(self):
        return self.grupos.get_all()

    def __repr__(self):
        return f'{self.nombre}, {self.clave}'

carrera1 = Carrera("Tics", "2212")
grupo1 = Grupo("7mo", "A")
grupo1.add_alumno(Alumno("Mario", "Garcia", "Rodriguez", "0001", "A0001"))
grupo1.add_alumno(Alumno("Gabriela", "Zamora", "Hernandez", "0002", "A0002"))
carrera1.add_grupo(grupo1)

print(f"Carrera: {carrera1}")
for grupo in carrera1.get_grupos():
    print(f"Grupo: {grupo.grado} {grupo.seccion}")
    for alumno in grupo.get_alumnos():
        print(alumno)
