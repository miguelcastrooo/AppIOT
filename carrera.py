from alumno import Alumno
from grupo import Grupo
from lista import Lista

class Carrera(Lista):
    def __init__(self, nombre=None, clave=None):
        super().__init__()  # Inicializa la clase base
        self.nombre = nombre
        self.clave = clave

    def add_grupo(self, grupo):
        self.add(grupo)

    def edit_grupo(self, idx, grupo):
        self.edit(idx, grupo)

    def get_grupos(self):
        return self.get_all()

    def __repr__(self):
        return f'{self.nombre}, {self.clave}'

if __name__ == "__main__":
    lista_carreras = Lista()

    carrera1 = Carrera("Tics", "2212")
    grupo1 = Grupo("7mo", "A")
    grupo1.add_alumno(Alumno("Miguel", "Castro", "Mesta", "0001", "A0001"))
    grupo1.add_alumno(Alumno("Gabriela", "Zamora", "Hernandez", "0002", "A0002"))
    carrera1.add_grupo(grupo1)

    grupo2 = Grupo("7mo", "B")
    grupo2.add_alumno(Alumno("Sofia", "López", "Martínez", "0003", "A0003"))
    carrera1.add_grupo(grupo2)

    lista_carreras.add(carrera1)

    carrera2 = Carrera("Matemáticas", "2213")
    grupo3 = Grupo("7mo", "C")
    grupo3.add_alumno(Alumno("Carlos", "Pérez", "Gómez", "0004", "A0004"))
    carrera2.add_grupo(grupo3)

    lista_carreras.add(carrera2)

    for carrera in lista_carreras.get_all():
        print(carrera)
        for grupo in carrera.get_grupos():
            print(f"  {grupo}")
            for alumno in grupo.get_alumnos():
                print(f"    {alumno}")
