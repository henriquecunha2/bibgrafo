class Aresta():

    v1 = ''
    v2 = ''
    rotulo = ''
    peso = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, rotulo='',v1='', v2='', peso:int=1):
        self.set_v1(v1)
        self.set_v2(v2)
        self.set_rotulo(rotulo)
        self.set_peso(peso)

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def set_v1(self, v=''):
        self.v1 = v

    def set_v2(self, v=''):
        self.v2 = v

    def get_peso(self):
        return self.peso

    def set_peso(self, p):
        if type(p) == int or type(p) == float:
            self.peso = p
        else:
            raise TypeError("O peso deve ser um inteiro ou real")

    def get_rotulo(self):
        return self.rotulo

    def set_rotulo(self, r=''):
        self.rotulo = r

    def eh_ponta(self, v):
        return v == self.v1 or v == self.v2

    def __eq__(self, other):
        return ((self.v1 == other.get_v1() and self.v2 == other.get_v2()) or (self.v1 == other.get_v2() and self.v2 == other.get_v1())) and self.rotulo == other.get_rotulo() and self.get_peso() == other.get_peso()

    def __str__(self):
        return "{}({}-{}), {}".format(self.get_rotulo(), self.get_v1(), self.get_v2(), self.get_peso())

class ArestaDirecionada(Aresta):
    def __eq__(self, other):
        return self.v1 == other.get_v1() and self.v2 == other.get_v2() and self.rotulo == other.get_rotulo() and self.get_peso() == other.get_peso()

    def __str__(self):
        return "{}({}->{}), {}".format(self.get_rotulo(), self.get_v1(), self.get_v2(), self.get_peso())