from random import randrange
from bibgrafo.grafo_errors import GrafoBuilderError, GrafoInvalidoError
from bibgrafo.grafo import GrafoIF

class GrafoBuilder:
    def __init__(self):
        self.__grafo = None

    def build(self):
        return self.__grafo

    def tipo(self, grafo: GrafoIF):
        if not isinstance(grafo, GrafoIF):
            raise GrafoInvalidoError('A classe utilizada não é um grafo.')

        self.__grafo = grafo
        return self

    def vertices(self, qtd: int=1, start: chr='A', vertices=['A']):
        for i in range(qtd):
            self.__grafo.adiciona_vertice(chr(ord(start) + i))
        return self

    def arestas(self, qtd: int=1, completo=False, laco=False):
        name_a = 'a'
        if completo:
            if len(self.__grafo.vertices) == 0:
                raise GrafoBuilderError('A lista de vértices ainda está vazia.')
            for v1 in range(len(self.__grafo.vertices)):
                for v2 in range(v1 + 1, len(self.__grafo.vertices)):
                    self.__grafo.adiciona_aresta(name_a + str(j),
                        self.__grafo.vertices[v1].rotulo, self.__grafo.vertices[v2].rotulo)
                name_a = chr(ord(name_a) + 1)

        else:
            # ideia: utilizar duas listas com os rótulos dos vértices
            name_a = 'a'
            for i in range(qtd):
                v1 = randrange(len(self.__grafo.vertices))
                if laco:
                    v2 = randrange(len(self.__grafo.vertices))
                else:
                    while True:
                        v2 = randrange(len(self.__grafo.vertices))
                        if v2 != v1: break

                self.__grafo.adiciona_aresta(name_a + str(i),
                    self.__grafo.vertices[v1].rotulo, self.__grafo.vertices[v2].rotulo)

        return self
