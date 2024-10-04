import json
from listaprofe import Lista

class Alumno(Lista):
    def __init__(self, matricula=None, nombre=None):
        super().__init__()
        if matricula is None and nombre is None:
            self.isLista = True
        else:
            self.matricula = matricula
            self.nombre = nombre
            self.isLista = False

    def __str__(self):
        if self.isLista:
            return f"Tienes {len(self.lista)} alumnos"
        else:
            return f"{self.matricula} {self.nombre}"

    def getDict(self):
        if not self.isLista:
            return {
                "matricula": self.matricula,
                "nombre": self.nombre
            }
        else:
            return [a.getDict() for a in self.lista]

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDict(), f, indent=4)

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for alumno_data in data:
                alumno = Alumno(alumno_data['matricula'], alumno_data['nombre'])
                self.add(alumno)


if __name__ == "__main__":
    a1 = Alumno("123123123", "Miguel")
    a2 = Alumno("098098098", "Angel")
    a3 = Alumno("098098098", "Aziel")

    listaAlumnos = Alumno()  
    listaAlumnos.add(a1)  
    listaAlumnos.add(a2)
    listaAlumnos.add(a3)

    #print(a1.getDict()) 
    print(listaAlumnos.getDict()) 


    #print(f"Total de alumnos: {len(listaAlumnos.lista)}") 
    #print(listaAlumnos)  

    #a1.save_to_json("alumno1.json")
    #a2.save_to_json("alumno2.json")
    listaAlumnos.save_to_json("listaAlumnos.json")


    loaded_lista_alumnos = Alumno()
    loaded_lista_alumnos.load_from_json("listaAlumnos.json")

    for alumno in loaded_lista_alumnos.lista:
        print(alumno)
