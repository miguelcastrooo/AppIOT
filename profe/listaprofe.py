class Lista:
    def __init__(self):  
        self.lista = []  
        self.isLista = True

    def add(self, objeto):
        """Agrega un objeto a la lista"""
        self.lista.append(objeto)

    def remove(self, index):
        """Elimina un objeto de la lista por índice"""
        if 0 <= index < len(self.lista):  
            del self.lista[index]
        else:
            print("Índice fuera de rango")

    def edit(self, index, objeto):
        """Edita un objeto de la lista en la posición especificada"""
        if 0 <= index < len(self.lista):  
            self.lista[index] = objeto
        else:
            print("Índice fuera de rango")
