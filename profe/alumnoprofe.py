from lista import Lista

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
            return f"Tienes {len(self.elementos)} alumnos"
        else:
            return f"{self.matricula} {self.nombre}"
        
    def getDict(self):
        if not self.isLista:
            return {
                "matricula": self.matricula,
                "nombre": self.nombre
            }
        else:
            return [a.getDict() for a in self.elementos]

if __name__ == "__main__":
    a1 = Alumno("123123123", "Diego")
    a2 = Alumno("098098098", "Ivan")
    a3= Alumno("0101010101", "Miguel")

    print(a1)  
    print(a2)
    print(a3)

    lista = Alumno()  
    lista.add(a1)  
    lista.add(a2)  

    print(lista) 
    print(a3.getDict())
     
