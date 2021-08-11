from aresta import Aresta
class ArestaDirecionada(Aresta):
    def __eq__(self, other):
        return self.v1 == other.getV1() and self.v2 == other.getV2() and self.rotulo == other.getRotulo() and self.getPeso() == other.getPeso()

    def __str__(self):
        return "{}({}->{}), {}".format(self.getRotulo(), self.getV1(), self.getV2(), self.getPeso())