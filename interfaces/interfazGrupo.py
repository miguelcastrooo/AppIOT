from grupo import Grupo
from alumno import Alumno
from mongo_conect import Mongoconection
from interfazAlumno import InterfazAlum
class InterfazGrupo:
    
   
        def __init__(self, grupos= None):
            # Inicializar lista objeto 
            mongo = self.ping()
            if mongo and grupos is None:
                print("Coneccion estbalecida")
                self.mongo = True
                self.grupos = Grupo()
                self.getOfMongo()
                try:
                    self.getOfJson()
                    self.saveInJson(True)
                    self.saveMongo()
                except:
                    pass
                self.getArchivo = False
            else:
                self.mongo = False
                if grupos is None:
                    self.getArchivo = True
                    self.grupos = Grupo()
                #Verificar si existe el archivo
                    try:
                        self.getOfJson()
                    except:
                        pass
                    
                else:
                    self.mongo = False
                    self.getArchivo = False
                    self.grupos = grupos
            
        def menu(self):
            if self.getArchivo:
                self.saveInJson()
            print("--------------Interfaz Grupo--------------")
            print("Elige una opcion \n 1.Agregar Grupo \n 2.Ver Grupos \n 3.Borrar Grupo \n 4.Actualizar Grupo \n 5.Salir ")
            case = input("Inserta el numero de la opcion que deseas usar:")
            case = int(case)
            if case == 1:
                self.addGrupo()
            elif case == 2:
                self.showGrupo()
                self.menu()
            elif case == 3:
                self.deletGrupo()
            elif case == 4:
                self.updateGrupo()
            elif case == 5:
                 print("Sesion finalizada.")
            else:
                print("Error!: Opcion no diponible \n Verifique que sea solo un numero \n Verifique que su numero este en las opciones")
                self.menu()
            
        def formGrupo(self):
            
            grado = input("Grado:")
            seccion = input("Seccion:")
            
            insert = input("Deseas agregar alumnos?:(1.Sí/2.NO):")
            if insert == "1":
                alumnado = Alumno()
                alumnos = InterfazAlum(alumnado)
                alumnos.menu()
                nalumnos = alumnos.alumnos
            else:
                nalumnos = Alumno()
                    
        
                
            nGrupo= Grupo(grado, seccion, nalumnos)
            return nGrupo
            
            
        
        def addGrupo(self):
            nGrupo = self.formGrupo()
            self.grupos.agregar_objeto(nGrupo)
            print("Se agrego de forma exitosa!!")
            insert=nGrupo.getDictG()
            if self.mongo:
                self.saveMongo(insert)
            self.menu()
            
        def showGrupo(self):
            if not self.grupos.objetos:
                print("Vacio")
            else:
                print(self.grupos)
                
        
        def deletGrupo(self):
            """Obtener indice y borrar"""
            self.showGrupo
            index = input("Indice de Grupo que deseas borrar?:")
            index = int(index) - 1
            sec = self.grupos.__len__()
            
            if sec < index:
                print("No hay grupos")
            elif index > sec:
                print("Aluno inexistente")
            else:
                self.grupos.eliminar_objeto(index)
            if self.mongo:
                self.dropMongo()
                self.saveMongo()   
            self.menu()
            
            
        def updateGrupo(self):
            self.showGrupo()
            index = input("Indice del Grupo que desea editar:")
            index=int(index)-1
            grado = input("Grado:")
            seccion = input("Seccion:")
            
            insert = input("Deseas modificar alumnos?:(1.Sí/2.NO):")
            if insert == "1":
                gpo = self.grupos[index]
                alumnos = InterfazAlum(gpo.alumnos)
                alumnos.menu()
                nalum = alumnos.alumnos
            else:
                gpo = self.grupos[index]
                nalum = gpo.alumnos
                
            nGrupo= Grupo(grado, seccion, nalum)
            self.grupos.__setitem__(index, nGrupo)
            if self.mongo:
                    self.dropMongo()
                    self.saveMongo()
            #print(nalum)
            print("Se actualizo de forma exitosa!!")
            
            self.menu()
            
            
        def saveInJson(self, clean=False):

            Nombre = "Lista_Carrera.json"
            if clean:
                x = Grupo()
                x.saveJson(Nombre)
            else:
                self.grupos.saveJson(Nombre)
            
        def getOfJson(self, Nombre="Lista_Grupos.json"):
            self.grupos.loadJsonG(Nombre)
            
        def saveMongo(self, grupo=None):
            conexion= Mongoconection("Grupos")
            if grupo is None:
                data = self.grupos.getDictG()
            else:
                data = grupo
            conexion.insertDoc(data)
            
        def dropMongo(self):
            conexion= Mongoconection("Grupos")
            conexion.deleteAllDocs()    
            
        def getOfMongo(self):
            conexion= Mongoconection("Grupos")
            cargar = conexion.findDoc()
            self.grupos.toObject(cargar)
            
        def ping(self):
            conexion= Mongoconection("Grupos")
            validar=conexion.ping()
            return validar 

if __name__ == "__main__":
    
  
    prueb = InterfazGrupo()
    prueb.menu()