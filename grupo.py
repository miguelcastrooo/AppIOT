from alumno import Alumno
from lista import Lista

class Grupo(Lista):
    def __init__(self, grado=None, seccion=None):
        super().__init__()  
        self.grado = grado
        self.seccion = seccion

    def add_alumno(self, alumno):
        self.add(alumno) 

    def get_alumnos(self):
        return self.get_all() 

    def __repr__(self):
        return f"Grupo: {self.grado} {self.seccion}"

if __name__ == "__main__":

    lista_grupos = Lista()

    grupo1 = Grupo("7mo", "A")
    grupo1.add_alumno(Alumno("Miguel", "Castro", "Mesta", "0001", "A0001"))
    grupo1.add_alumno(Alumno("Gabriela", "Zamora", "Hernandez", "0002", "A0002"))
    lista_grupos.add(grupo1)

    grupo2 = Grupo("7mo", "B")
    grupo2.add_alumno(Alumno("Sofia", "López", "Martínez", "0003", "A0003"))
    lista_grupos.add(grupo2)

    grupo3 = Grupo("7mo", "C")
    grupo3.add_alumno(Alumno("Carlos", "Pérez", "Gómez", "0004", "A0004"))
    lista_grupos.add(grupo3)

    for grupo in lista_grupos.get_all():
        print(grupo)
        for alumno in grupo.get_alumnos():
            print(f"  {alumno}")
