from alumno import Alumno
from grupo import Grupo
from lista import Lista

class Carrera(Lista):
    def __init__(self, nombre=None, clave=None):
        super().__init__()
        self.nombre = nombre
        self.clave = clave

    def add_grupo(self, grupo):
        if grupo not in self.elementos:
            self.add(grupo)
        else:
            print("El grupo ya está en la carrera.")

    def remove_grupo(self, grupo):
        try:
            self.elementos.remove(grupo)
        except ValueError:
            print("El grupo no está en la carrera.")

    def edit_grupo(self, indice, grupo):
        if 0 <= indice < len(self.elementos):
            self.elementos[indice] = grupo
        else:
            raise IndexError("Índice fuera de rango")

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

    lista_grupos.save_to_json("grupos.json")

    grupos_cargados = Lista()
    grupos_cargados.load_from_json("grupos.json")
    print("Grupos cargados desde JSON:", grupos_cargados.get_all())
