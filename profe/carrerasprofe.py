import json
from listaprofe import Lista
from alumnoprofe import Alumno
from grupoprofe import Grupo

class Carrera(Lista):
    def __init__(self, nombre=None, clave=None):
        super().__init__()
        if nombre is None and clave is None:
            self.isLista = True
        else:
            self.nombre = nombre
            self.clave = clave
            self.grupos = Grupo()  
            self.isLista = False

    def __str__(self):
        if self.isLista:
            return f"Tienes {len(self.lista)} carreras"
        else:
            return f"{self.clave} - {self.nombre} con grupos: {self.grupos}"

    def addGrupo(self, grupo):
        self.grupos.add(grupo)  

    def getDict(self):
        if not self.isLista:
            return {
                "nombre": self.nombre,
                "clave": self.clave,
                "grupos": self.grupos.getDict()  
            }
        else:
            return [c.getDict() for c in self.lista]

    def getTotalAlumnos(self):
        return sum(g.getTotalAlumnos() for g in self.grupos.lista)

    def getTotalGrupos(self):
        return len(self.grupos.lista)
    
    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDict(), f, indent=4)

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for carrera_data in data:
                carrera = Carrera(carrera_data['nombre'], carrera_data['clave'])
                
                for grupo_data in carrera_data['grupos']:
                    grupo = Grupo(grupo_data['grado'], grupo_data['seccion'])
                    
                    for alumno_data in grupo_data['alumnos']:
                        alumno = Alumno(alumno_data['matricula'], alumno_data['nombre'])
                        grupo.addAlumno(alumno)
                    
                    carrera.addGrupo(grupo)

                self.add(carrera)

if __name__ == "__main__":
    a1 = Alumno("123123123", "Miguel")
    a2 = Alumno("098098098", "Angel")
    a3 = Alumno("098098098", "Aziel")

    g1 = Grupo("1", "A")
    g2 = Grupo("2", "B")
    g1.addAlumno(a1)
    g1.addAlumno(a2)
    g2.addAlumno(a3)

    c1 = Carrera("Ingeniería en Sistemas", "IS")
    c2 = Carrera("Licenciatura en Diseño", "LD")

    c1.addGrupo(g1)
    c2.addGrupo(g2)

    listaCarreras = Carrera()  
    listaCarreras.add(c1)  
    listaCarreras.add(c2)

    #print(c1.getDict()) 
    #print(c2.getDict()) 
    print(listaCarreras.getDict())  

    #c1.save_to_json("carrera1.json")
    #c2.save_to_json("carrera2.json")
    listaCarreras.save_to_json("listaCarrerass.json")

    loaded_carreras = Carrera()
    loaded_carreras.load_from_json("listaCarrerass.json")  # Asegúrate de que el nombre del archivo coincida
    
    for carrera in loaded_carreras.lista:
        print(carrera)