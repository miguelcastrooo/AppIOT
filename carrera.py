from grupo import Grupo
from alumno import Alumno

class Carrera:
    def __init__(self, nombre, clave):
        self.nombre = nombre  
        self.clave = clave  
        self.grupos = []

    def agregar_grupo(self, grupo: Grupo):
        self.grupos.append(grupo)

    def mostrar_grupos(self):
        print(f'Carrera: {self.nombre} - Clave: {self.clave}')
        for grupo in self.grupos:
            grupo.mostrar_alumnos()


if __name__ == "__main__":