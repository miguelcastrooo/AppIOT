class Lista:
    def __init__(self):
        self.elems = []

    def add(self, elem):
        self.elems.append(elem)

    def edit(self, idx, elem):
        if 0 <= idx < len(self.elems):
            self.elems[idx] = elem
        else:
            raise IndexError("Index out of bounds")

    def get_all(self):
        return self.elems

    def __repr__(self):
        return str(self.elems)
