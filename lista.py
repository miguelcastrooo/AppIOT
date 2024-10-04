import json

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

    def to_dict(self):
        return [elemento.to_dict() for elemento in self.elementos]

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            elementos_dict = json.load(file)
        
        print("Datos cargados del JSON:", elementos_dict)
        print("Tipo de datos cargados:", type(elementos_dict))

        # Verificar si `elementos_dict` es una lista de diccionarios
        if isinstance(elementos_dict, list) and all(isinstance(d, dict) for d in elementos_dict):
            self.elementos = [self.elemento_from_dict(d) for d in elementos_dict]
        else:
            raise ValueError("Formato de archivo JSON incorrecto para cargar los elementos.")

    def elemento_from_dict(self, elemento_dict):
        raise NotImplementedError("Debe implementarse en la subclase")

    def __repr__(self):
        return str(self.elementos)
