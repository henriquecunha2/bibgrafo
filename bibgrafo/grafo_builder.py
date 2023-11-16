from random import randrange, shuffle, randint
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

    def vertices(self, qtd: int=1, start: chr='A', vertices=[]):
        if not start.isupper() or not start.isalpha():
            raise GrafoBuilderError('O rótulo dos vértices deve ser uma letra maiúscula')
        if vertices:
            for v in vertices:
                self.__grafo.adiciona_vertice(v)
        else:
            MAX = ord('Z') - ord('A')
            START_MAX = ord('Z') - ord(start) + 1
            for i in range(qtd):
                if i >= START_MAX:
                    rotulo_v = []
                    n = i
                    while n >= START_MAX:
                        m = n % START_MAX
                        rotulo_v.insert(0, chr(ord('A') + m))
                        n //= START_MAX
                    rotulo_v.insert(0, chr(ord('A') + n - 1))
                    self.__grafo.adiciona_vertice(''.join(rotulo_v))
                else: self.__grafo.adiciona_vertice(chr(ord(start) + i))
        return self

    def arestas(self, arestas=list(), qtd: int=1, completo=False, laco=False, qtd_laco=1,
        conexo=True, qtd_desconexo=2, paralelas=False, qtd_paralelas=1, peso_max=1, peso_min=0):

        def peso(peso_max: int):
            if peso_max <= peso_min: raise GrafoBuilderError('O intervalo para o peso das arestas é inválido')
            elif peso_max == 1 and peso_min == 0: return 1
            else: return randrange(peso_min, peso_max)

        if len(arestas) > 0:
            for a in arestas:
                try: self.__grafo.adiciona_aresta(a)
                except NotImplementedError: raise GrafoBuilderError('Este grafo não suporta este tipo de Aresta')
            return self

        name_a = 'a'
        vertices = [v.rotulo for v in self.__grafo.vertices]
        if completo:
            if len(vertices) == 0:
                raise GrafoBuilderError('A lista de vértices ainda está vazia.')
            for v1 in range(len(vertices)):
                for v2 in range(v1 + 1, len(vertices)):
                    par_v = [vertices[v1], vertices[v2]]
                    shuffle(par_v)
                    self.__grafo.adiciona_aresta(name_a + str(v2),
                        par_v[0], par_v[1], peso(peso_max))
                name_a = chr(ord(name_a) + 1)

        else:
            pares_adjacentes = list()
            for v1 in range(len(vertices)):
                for v2 in range(v1 + 1, len(vertices)):
                    pares_adjacentes.append([vertices[v1], vertices[v2]])
            if not conexo:
                if qtd_desconexo > len(vertices):
                    raise GrafoBuilderError('Não é possível gerar um grafo desconexo com configurações passadas')

                vertices_desconexos = []
                for i in range(qtd_desconexo):
                    v = vertices.pop(randrange(len(vertices)))
                    vertices_desconexos.append(v)
                grafo_desconexo = GrafoBuilder().tipo(self.__grafo.__class__()).vertices(vertices=vertices_desconexos) \
                    .arestas(completo=True, peso_max=peso_max).build()

                for n, aresta in enumerate(grafo_desconexo.arestas.values()):
                    self.__grafo.adiciona_aresta(str(n) + 'c',
                        aresta.v1.rotulo, aresta.v2.rotulo, peso(peso_max))
                    n += 1

            if laco:
                for i in range(qtd_laco):
                    v = randrange(len(vertices))
                    self.__grafo.adiciona_aresta(str(i) + 'l',
                        vertices[v], vertices[v], peso(peso_max))

            if qtd > (len(vertices) * (len(vertices) - 1)) / 2:
                raise GrafoBuilderError('Não é possível gerar um grafo com esta quantidade de arestas')
            for i in range(qtd):
                par_v: list
                if len(vertices) > 2:
                    par_v = pares_adjacentes.pop(randint(0, len(pares_adjacentes) - 1))
                else:
                    par_v = pares_adjacentes.pop()
                shuffle(par_v)
                self.__grafo.adiciona_aresta(name_a + str(i),
                    par_v[0], par_v[1], peso(peso_max))

            if paralelas:
                arestas = [a for a in self.__grafo.arestas.values()]
                for i in range(qtd_paralelas):
                    a = randrange(len(arestas))
                    self.__grafo.adiciona_aresta(str(i) + 'p',
                        arestas[a].v1.rotulo, arestas[a].v2.rotulo, peso(peso_max))
        return self
