from grupo import Grupo
from alumno import Alumno
from carrera import Carrera
from interfazGrupo import InterfazGrupo
from mongo_conect import Mongoconection
class InterfazCarre:
    
   
        def __init__(self, carreras= None):
            # Inicializar lista objeto 
            mongo = self.ping()
            if mongo and carreras is None:
                print("Coneccion estbalecida")
                self.mongo = True
                self.carreras = Carrera()
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
                if carreras is None:
                    self.getArchivo = True
                    self.carreras = Carrera()
                #Verificar si existe el archivo
                    try:
                        self.getOfJson()
                    except:
                        pass
                    
                else:
                    self.getArchivo = False
                    self.carreras = carreras
                
            
            
        def menu(self):
            if self.getArchivo:
                self.saveInJson()#Actualizador
            print("---------------------Interfaz Carrera--------------------")
            print("Elige una opcion \n 1.Agregar Carrera \n 2.Ver Carrera \n 3.Borrar Carrera \n 4.Actualizar Carrera \n 5.Salir ")
            case = input("Inserta el numero de la opcion que deseas usar:")
            case = int(case)
            if case == 1:
                self.addCarrera()
            elif case == 2:
                self.showCarrera()
                self.menu()
            elif case == 3:
                self.deletCarrera()
            elif case == 4:
                self.updateCarrera()
            elif case == 5:
                 print("Sesion finalizada.")
            else:
                print("Error!: Opcion no diponible \n Verifique que sea solo un numero \n Verifique que su numero este en las opciones")
                self.menu()
            
        def formCarrera(self):
            
            carrera = input("Carrea:")
            clave = input("Clave:")
            insert = input("Deseas agregar grupos?:(1.Sí/2.NO):")
            if insert == "1":
                grupo = Grupo()
                grupos = InterfazGrupo(grupo)
                grupos.menu()
                ngrupos = grupos.grupos
            else:
                ngrupos = Grupo()
            
            
            
            nCarrera= Carrera(carrera, clave, ngrupos)
            return nCarrera
        
        def addCarrera(self):
            nCarrera = self.formCarrera()
            self.carreras.agregar_objeto(nCarrera)
            insert = nCarrera.getDictC()
            if self.mongo:
                self.saveMongo(insert)
            print("Se agrego de forma exitosa!!")
            self.menu()
            
        def showCarrera(self):
            if not self.carreras.objetos:
                print("Vacio")
            else:
                print(self.carreras)
                
            
        
        def deletCarrera(self):
            """Obtener indice y borrar"""
            self.showCarrera()
            index = input("Indice de la Carrera que deseas borrar?:")
            index = int(index) - 1
            sec = self.carreras.__len__()
            
            if sec < index:
                print("No hay grupos")
            elif index > sec:
                print("Aluno inexistente")
            else:
                self.carreras.eliminar_objeto(index)
            if self.mongo:
                self.dropMongo()
                self.saveMongo()  
            self.menu()
            
            
        def updateCarrera(self):
            self.showCarrera()
            index = input("Indice de la carrera que desea editar:")
            index=int(index)-1
            grado = input("Nombre:")
            seccion = input("Clave:")
            
            insert = input("Deseas modificar grupos?:(1.Sí/2.NO):")
            if insert == "1":
                gpo = self.carreras[index]
                alumnos = InterfazGrupo(gpo.grupos)
                alumnos.menu()
                nalum = alumnos.grupos
            else:
                gpo = self.carreras[index]
                nalum = gpo.grupos
                
            nGrupo= Grupo(grado, seccion, nalum)
            self.carreras.__setitem__(index, nGrupo)
            if self.mongo:
                    self.dropMongo()
                    self.saveMongo()
            #print(nalum)
            print("Se actualizo de forma exitosa!!")
            
            self.menu()
            
        def saveInJson(self, clean=False):

            Nombre = "Lista_Carrera.json"
            if clean:
                x = Carrera()
                x.saveJson(Nombre)
            else:
                self.carreras.saveJson(Nombre)
            
            
            
            
        def getOfJson(self):
            Nombre = "Lista_Carrera.json"
            
            self.carreras.loadJsonC(Nombre)
            
        def saveMongo(self, grupo=None):
            conexion= Mongoconection("Carreras")
            if grupo is None:
                data = self.carreras.getDictC()
            else:
                data = grupo
            conexion.insertDoc(data)
            
        def dropMongo(self):
            conexion= Mongoconection("Carreras")
            conexion.deleteAllDocs()    
            
        def getOfMongo(self):
            conexion= Mongoconection("Carreras")
            cargar = conexion.findDoc()
            self.carreras.toObject(cargar)
            
        def ping(self):
            conexion= Mongoconection("Carreras")
            validar=conexion.ping()
            return validar 

            
            
if __name__ == "__main__":
    
    prueb = InterfazCarre()
    prueb.menu()