from grupo import Grupo
from alumno import Alumno
from lista import Lista


class Grupo(Lista):
    def _init_(self, grado=None, seccion=None):
        if(grado == None and seccion == None):
            super()._init_()
        else:
            self.grado = grado
            self.seccion = seccion
            self.alumnos = Alumno()
            self.isLista = False

    def addAlumno(self,alumno):
        self.alumnos.add(alumno)

    def _str_(self):
        if self.isLista:
            return  f"Tienes {len(self.lista)} grupos"
        else:
            return f"{self.grado} {self.seccion} {self.alumnos}"

    def getDict(self):
        if not self.isLista:
            return {
                "grado": self.grado,
                "seccion": self.seccion,
                "alumnos": self.alumnos.getDict()
            }
        else:
            return [g.getDict() for g in self.lista]

if __name__ == "_main_":
    a1=Alumno("123123123","Diego")
    a2=Alumno("098098098","Ivan")
    g1=Grupo("1","A")
    g2=Grupo("2","B")
    g1.addAlumno(a1)
    g1.addAlumno(a2)
    g2.addAlumno(a1)
    lista=Grupo()
    lista.add(g1)
    lista.add(g2)


    
    print(g1.getDict())
    print(g2.getDict())
    print(lista.getDict())