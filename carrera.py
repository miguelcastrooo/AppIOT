from alumno import Alumno
from grupo import Grupo
from lista import Lista

class Carrera(Lista):
    def __init__(self, nombre=None, clave=None):
        super().__init__()
        self.nombre = nombre
        self.clave = clave

    def add_grupo(self, grupo):
        self.add(grupo)

    def get_grupos(self):
        return self.get_all()

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "clave": self.clave,
            "grupos": [grupo.to_dict() for grupo in self.elementos]
        }

    @classmethod
    def from_dict(cls, data):
        carrera = cls(nombre=data.get("nombre"), clave=data.get("clave"))
        grupos = [Grupo.from_dict(grupo_data) for grupo_data in data.get("grupos", [])]
        carrera.elementos = grupos
        return carrera

    def elemento_from_dict(self, elemento_dict):
        return Carrera.from_dict(elemento_dict)

    def __repr__(self):
        return f"{self.nombre}, {self.clave} con {len(self.elementos)} grupos"

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

    lista_carreras.save_to_json("carreras.json")

    carreras_cargadas = Lista()
    carreras_cargadas.load_from_json("carreras.json")
    print("Carreras cargadas desde JSON:", carreras_cargadas.get_all())

    # Acceso a los alumnos
    if lista_carreras.get_all():  # Verificar que haya carreras
        print(lista_carreras.get_all()[0].get_grupos()[0].get_alumnos()[1])  # Accede al segundo alumno del primer grupo en la primera carrera.
