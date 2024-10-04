class Lista:
    def _init_(self):
        self.lista = []
        self.isLista = True

    def add(self, objeto):
        self.lista.append(objeto)

    def remove(self, index):
        self.lista.remove(index)

    def edit(self, index, objeto):
        self.lista[index] = objeto