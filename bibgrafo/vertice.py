class Vertice:

    rotulo: str
    attr: dict

    def __init__(self, r: str, attr=None):
        self.rotulo = r
        if attr is None:
            self.attr = dict()
        else:
            self.attr = attr

    def get_rotulo(self):
        return self.rotulo

    def set_rotulo(self, r: str):
        if type(r) is not str:
            raise TypeError("O tipo do rótulo deve ser string")
        self.rotulo = r

    def get_attr(self):
        return self.attr

    def set_attr(self, attr: dict):
        if type(attr) is not dict:
            raise TypeError("O tipo do rótulo deve ser string")
        self.attr = attr

    def adiciona_attr(self, chave, valor):
        self.attr[chave] = valor

    def remove_attr(self, chave):
        self.attr.pop(chave)

    def get_um_attr(self, chave):
        return self.attr[chave]

    def __eq__(self, other):
        return self.get_rotulo() == other.get_rotulo() and \
            self.get_attr() == other.get_attr()

    def __str__(self):
        return self.get_rotulo()
