class Lista:
    def __init__(self):
        self.elementos = []

    def add(self, elemento):
        self.elementos.append(elemento)

    def edit(self, indice, elemento):
        if 0 <= indice < len(self.elementos):
            self.elementos[indice] = elemento
        else:
            raise IndexError("Índice fuera de rango")

    def get_all(self):
        return self.elementos

    def __repr__(self):
        return str(self.elementos)
