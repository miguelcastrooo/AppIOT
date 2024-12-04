from grupo import Grupo
from alumno import Alumno
import json
from listaObjetos import ListaObjetos

class Carrera(ListaObjetos):
    def __init__(self, nombre=None, clave=None, grupos=None):

            super().__init__()
            if nombre is None:
                self.list = True
            else:
                self.list = False
            self.nombre = nombre
            self.clave = clave
            self.grupos = grupos
        
    def __str__(self):
        if self.list:
            return self.mostList()
        else:
            return f"Carrera: {self.nombre}, Clave: {self.clave}, Grupos:\n{self.grupos}"
        
        
    def getDictC(self):
        if self.list:
            return [g.getDictC() for g in self.objetos]
        else:
            return {
                "nombre": self.nombre,
                "clave" : self.clave,
                "grupos" : self.grupos.getDictG()
            }
        

        
    def saveJson(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.getDictC(), f, indent=4)
            
                
    def loadJsonC(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.toObject(data)
            
    def toObject(self, data):
            for carrera_data in data:
                grupos = Grupo()
                grupos.toObject(carrera_data['grupos'])                
                carrera = Carrera(carrera_data['nombre'], carrera_data['clave'], grupos)
                self.agregar_objeto(carrera)
        

if __name__ == "__main__":
    """
    alumno1 = Alumno("Javier", "Armando", "Garcia", "CURP001", "001")
    alumno2 = Alumno("Roberto", "Cedillo", "Marquez", "CURP002", "002")
    alumno3 = Alumno("Octavi", "Paz", "Olive", "CURP003", "003")
    
    alumnolista = Alumno()
    alumnolista2 = Alumno()
    
    alumnolista.agregar_objeto(alumno1)
    alumnolista.agregar_objeto(alumno2)
    alumnolista2.agregar_objeto(alumno3)
    
    grup1 = Grupo("5", "c", alumnolista)
    grupox = Grupo("8", "c", alumnolista)
    grupo2 = Grupo("1", "a", alumnolista2)
    
    grupolista = Grupo()
    
    grupolista.agregar_objeto(grup1)
    grupolista.agregar_objeto(grupo2)
    
    carrera1 = Carrera("Ciencias", "001", grupolista)
    carrera2 = Carrera("Fisica", "002", grupolista)
    
    carreralista = Carrera()
    
    carreralista.agregar_objeto(carrera1)
    carreralista.agregar_objeto(carrera2)
    
    #print(carrera2)
    #print('////////////////////////////')
    #print(carreralista.getDictC())
    
    carreralista.saveJson("carreraCarga.json")"""
    
    loadcarrera = Carrera()
    
    loadcarrera.loadJsonC("carreraCarga.json")
    
    print(loadcarrera)
    
    
    