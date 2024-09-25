from lista import Lista  

class Alumno:
    def __init__(self, nombre=None, ap_materno=None, ap_paterno=None, curp=None, matricula=None):
        self.nombre = nombre
        self.ap_materno = ap_materno
        self.ap_paterno = ap_paterno
        self.curp = curp
        self.matricula = matricula

    def __repr__(self):
        return f"{self.nombre} {self.ap_materno} {self.ap_paterno} {self.matricula}"

alumno1 = Alumno("Miguel", "Castro", "Mesta", "0001", "A0001")
alumno2 = Alumno("Gabriela", "Zamora", "Hernandez", "0002", "A0002")

lista_alumnos = Lista()  
lista_alumnos.add(alumno1)
lista_alumnos.add(alumno2)

print(lista_alumnos)
