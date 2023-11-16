from random import randrange, shuffle
from bibgrafo.grafo_errors import GrafoBuilderError, GrafoInvalidoError
from bibgrafo.grafo import GrafoIF

class GrafoBuilder:
    def __init__(self):
        self.__grafo = None

    def build(self):
        # TODO: O build deve gravar o grafo construído em um arquivo JSON
        # (construir um bibgrafo.grafo_reader)
        return self.__grafo

    def tipo(self, grafo: GrafoIF):
        if not isinstance(grafo, GrafoIF):
            raise GrafoInvalidoError('A classe utilizada não é um grafo.')

        self.__grafo = grafo
        return self

    def vertices(self, qtd: int=1, start: chr='A', vertices=[]):
        if vertices:
            for v in vertices:
                self.__grafo.adiciona_vertice(v)
        else:
            for i in range(qtd):
                self.__grafo.adiciona_vertice(chr(ord(start) + i))
        # TODO: e se qtd > 26? (alfabeto) gerar 27 == 'AA'
        return self

    def arestas(self, arestas=list(), qtd: int=1, completo=False, laco=False, qtd_laco=1,
        conexo=True, qtd_desconexo=2, paralelas=False, qtd_paralelas=1, peso_max=1, peso_min=0):

        def peso(peso_max: int):
            if peso_max <= peso_min: raise GrafoBuilderError('O intervalo para o peso das arestas é inválido')
            elif peso_max == 1 and peso_min: return 1
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
            adjacentes = set()
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

            if qtd > (len(vertices) * (len(vertices) - 1)) / 2: # créditos ao ChatGPT
                raise GrafoBuilderError('Não é possível gerar um grafo com esta quantidade de arestas')
            for i in range(qtd):
                # TODO: gerar uma lista de todos os pares possíveis, ao invés de usar um while
                if len(vertices) > 2:
                    while True:
                        v1 = randrange(len(vertices))
                        v2 = randrange(len(vertices))
                        par_adj = '%s-%s' % (vertices[v1], vertices[v2])
                        if par_adj not in adjacentes and v2 != v1: break
                else:
                    v1, v2 = 0, 1
                par_v = [vertices[v1], vertices[v2]]
                shuffle(par_v)
                self.__grafo.adiciona_aresta(name_a + str(i),
                    par_v[0], par_v[1], peso(peso_max))
                adjacentes.add('%s-%s' % (vertices[v1], vertices[v2]))

            if paralelas:
                arestas = [a for a in self.__grafo.arestas.values()]
                for i in range(qtd_paralelas):
                    a = randrange(len(arestas))
                    self.__grafo.adiciona_aresta(str(i) + 'p',
                        arestas[a].v1.rotulo, arestas[a].v2.rotulo, peso(peso_max))
        return self
