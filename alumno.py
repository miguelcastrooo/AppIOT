from lista import Lista
import json

class Alumno:
    def __init__(self, nombre=None, ap_materno=None, ap_paterno=None, curp=None, matricula=None):
        self.nombre = nombre
        self.ap_materno = ap_materno
        self.ap_paterno = ap_paterno
        self.curp = curp
        self.matricula = matricula

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "ap_materno": self.ap_materno,
            "ap_paterno": self.ap_paterno,
            "curp": self.curp,
            "matricula": self.matricula
        }

    @classmethod
    def from_dict(cls, data):
        if isinstance(data, dict):
            return cls(
                nombre=data.get("nombre"),
                ap_materno=data.get("ap_materno"),
                ap_paterno=data.get("ap_paterno"),
                curp=data.get("curp"),
                matricula=data.get("matricula")
            )
        else:
            raise TypeError("El formato del elemento no es válido. Se esperaba un diccionario.")

    def __repr__(self):
        return f"{self.nombre} {self.ap_materno} {self.ap_paterno} {self.matricula}"


class Alumnos(Lista):
    def __init__(self):
        super().__init__()

    def print_json(self):
        print(json.dumps([alumno.to_dict() for alumno in self.elementos], indent=4))

    def get_alumno(self, index):
        try:
            return self.elementos[index]
        except IndexError:
            print("Índice fuera de rango.")

if __name__ == "__main__":
    lista_alumnos = Alumnos()

    # Creación de alumnos
    alumno1 = Alumno("Miguel", "Castro", "Mesta", "0001", "A0001")
    alumno2 = Alumno("Gabriela", "Zamora", "Hernandez", "0002", "A0002")
    alumno3 = Alumno("Benjamin", "Castro", "Garcia", "0003", "A0003")
    alumno4 = Alumno("Claudia", "Mesta", "Castellanos", "0004", "A0004")

    # Agregar alumnos a la lista
    lista_alumnos.add(alumno1)
    lista_alumnos.add(alumno2)
    lista_alumnos.add(alumno3)
    lista_alumnos.add(alumno4)

    # Guardar en JSON
    lista_alumnos.save_to_json("alumnos.json")

    # Cargar desde JSON
    lista_cargada = Alumnos()
    lista_cargada.load_from_json("alumnos.json")

    print("Alumnos cargados desde JSON:")
    lista_cargada.print_json()

    # Ejemplo de impresión de un alumno específico por índice
    indice = 1  # Cambia este índice para acceder a otro alumno (0 para el primero, 1 para el segundo, etc.)
    alumno_especifico = lista_cargada.get_alumno(indice)
    if alumno_especifico:
        print("\nAlumno específico:")
        print(alumno_especifico)
