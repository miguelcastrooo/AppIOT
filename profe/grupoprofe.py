import json
from alumnoprofe import Alumno
from listaprofe import Lista

class Grupo(Lista):
    def __init__(self, grado=None, seccion=None):
        super().__init__()  
        if grado is None and seccion is None:
            self.isLista = True
        else:
            self.grado = grado
            self.seccion = seccion
            self.alumnos = Alumno()  
            self.isLista = False

    def addAlumno(self, alumno):
        self.alumnos.add(alumno)  

    def __str__(self):
        if self.isLista:
            return f"Tienes {len(self.lista)} grupos"
        else:
            return f"{self.grado} {self.seccion} con alumnos: {self.alumnos}"

    def getDict(self):
        if not self.isLista:
            return {
                "grado": self.grado,
                "seccion": self.seccion,
                "alumnos": self.alumnos.getDict()  
            }
        else:
            return [g.getDict() for g in self.lista]

    def getTotalAlumnos(self):
        return len(self.alumnos.lista)

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDict(), f, indent=4) 

if __name__ == "__main__":
    a1 = Alumno("123123123", "Miguel")
    a2 = Alumno("098098098", "Angel")
    a3 = Alumno("098098098", "Aziel")

    
    g1 = Grupo("1", "A")
    g2 = Grupo("2", "B")
    
    g1.addAlumno(a1)
    g1.addAlumno(a2)
    g2.addAlumno(a3)
    
    listaGrupos = Grupo()  
    listaGrupos.add(g1)    
    listaGrupos.add(g2)    

    print(g1.getDict())
    print(g2.getDict())
    print(listaGrupos.getDict())

    total_alumnos = sum(g.getTotalAlumnos() for g in listaGrupos.lista)
    total_grupos = len(listaGrupos.lista)

    print(f"Total de alumnos: {total_alumnos}")
    print(f"Total de grupos: {total_grupos}")
    print(listaGrupos)

    #g1.save_to_json("grupo1.json")
    #g2.save_to_json("grupo2.json")
    listaGrupos.save_to_json("listaGrupos.json")
