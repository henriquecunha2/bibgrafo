from functools import singledispatchmethod
from random import randrange, shuffle, randint
from bibgrafo.grafo_errors import GrafoBuilderError, GrafoInvalidoError
from bibgrafo.grafo import GrafoIF

class GrafoBuilder:
    '''
        Esta classe é um gerador semiautomático de grafos.
        Ela recebe uma instância de qualquer subclasse de GrafoIF (ou seja, qualquer grafo válido)
        e adiciona vértices e arestas de acordo com os parâmetros passados, podendo gerar grafos
        aleatórios ou pode receber vértices e arestas já criados pelo usuário.

        Attributes:
            _grafo: receberá a instância de GrafoIF na qual serão realizadas as operações
            de inserção de vértices e arestas, conforme requerido.
    '''
    def __init__(self):
        self._grafo = None

    def build(self):
        '''
            Esta função deve ser chamada ao final de todas as outras, retornando a instância
            do grafo criado pelo GrafoBuilder.
        '''
        return self._grafo

    def tipo(self, grafo: GrafoIF):
        '''
            Esta função define o tipo do grafo a ser utilizado no GrafoBuilder.
            Args:
                grafo: recebe uma instância de GrafoIF (ex.: GrafoListaAdjacencia)
            Raises:
                GrafoInvalidoError: se a instância da classe passada não herda de GrafoIF
        '''
        if not isinstance(grafo, GrafoIF):
            raise GrafoInvalidoError('A classe utilizada não é um grafo')

        self._grafo = grafo
        return self

    def vertices(self, qtd: int=1, start: chr='A', vertices=[]):
        '''
            Recebe os parâmetros para inserção dos vértices pelo GrafoBuilder.
            Args:
                vertices: recebe uma lista de objetos do tipo bibgrafo.Vertice
                Caso esta lista tenha um tamanho maior do que 1, este parâmetro
                fará com que todos os outros sejam ignorados pela função.
                qtd: a quantidade de vértices a serem adicionados.
                start: recebe uma letra do alfabeto maiúscula, que será o rótulo
                do primeiro vértice.
            Raises:
                GrafoBuilderError: caso a lista de vértices não contenha objetos do tipo bibgrafo.Vertice
                ou caso o caractere passado para 'start' não seja uma letra maiúscula
        '''
        if vertices:
            for v in vertices:
                try:
                    self._grafo.adiciona_vertice(v)
                except NotImplementedError:
                    raise GrafoBuilderError('A lista de vértices deve conter objetos do tipo Vertice')
        else:
            if not start.isupper() or not start.isalpha():
                raise GrafoBuilderError('O rótulo dos vértices deve ser uma letra maiúscula')

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
                    self._grafo.adiciona_vertice(''.join(rotulo_v))
                else: self._grafo.adiciona_vertice(chr(ord(start) + i))
        return self

    def _peso(self, min, max):
        if min >= max: raise GrafoBuilderError('Forneça um intervalo válido para o peso das arestas')
        if min == 0 and max == 1: return max
        else: return randint(min, max)

    @singledispatchmethod
    def arestas(self, arg: int, **kwargs):
        vertices = [v.rotulo for v in self._grafo.vertices]
        if arg > (len(vertices) * (len(vertices) - 1)) / 2:
            raise GrafoBuilderError('Não é possível construir um grafo com esta quantidade de arestas')

        desconexos = kwargs.get('desconexos', 0)
        if desconexos < 0 or desconexos > len(vertices):
            raise GrafoBuilderError('Forneça um número válido para os vértices desconexos')
        lacos = kwargs.get('lacos', 0)
        if lacos < 0: raise GrafoBuilderError('Forneça um número de laços positivo')
        paralelas = kwargs.get('paralelas', 0)
        if paralelas < 0: raise GrafoBuilderError('Forneça um número de arestas paralelas positivo')
        peso_min = kwargs.get('peso_min', 0)
        peso_max = kwargs.get('peso_max', 1)

        vertices_desc = []
        if desconexos:
            for i in range(desconexos):
                v_desc = vertices.pop(randint(0, len(vertices) - 1))
                vertices_desc.append(v_desc)
            rotulo_v = 1
            if len(vertices_desc) > 1:
                for v1 in range(len(vertices_desc)):
                    for v2 in range(v1 + 1, len(vertices_desc)):
                        self._grafo.adiciona_aresta('{}c'.format(rotulo_v),
                        vertices_desc[v1], vertices_desc[v2], self._peso(peso_min, peso_max))
                        rotulo_v += 1
            else:
                self._grafo.adiciona_aresta('{}c'.format(rotulo_v),
                    vertices_desc[0], vertices_desc[0], self._peso(peso_min, peso_max))

        pares = []
        adjacentes = []

        for v1 in range(len(vertices)):
            for v2 in range(v1 + 1, len(vertices)):
                pares.append([vertices[v1], vertices[v2]])

        for i in range(arg):
            par = pares.pop(randint(0, len(pares) - 1)) if len(pares) > 1 else pares[0]
            shuffle(par)
            adjacentes.append(par)
            self._grafo.adiciona_aresta('a{}'.format(i), par[0],
                par[1], self._peso(peso_min, peso_max))

        if paralelas:
            for i in range(paralelas):
                par = adjacentes[randint(0, len(adjacentes) - 1)]
                self._grafo.adiciona_aresta('{}p'.format(i + 1),
                    par[0], par[1], self._peso(peso_min, peso_max))

        if lacos:
            for i in range(lacos):
                v = vertices[randint(0, len(vertices) - 1)]
                self._grafo.adiciona_aresta('{}l'.format(i + 1),
                v, v, self._peso(peso_min, peso_max))

        return self

    @arestas.register
    def _(self, arg: bool, **kwargs):
        peso_min = kwargs.get('peso_min', 0)
        peso_max = kwargs.get('peso_max', 1)
        vertices = [v.rotulo for v in self._grafo.vertices]
        rotulo_a = 1
        for v1 in range(len(vertices)):
            for v2 in range(v1 + 1, len(vertices)):
                self._grafo.adiciona_aresta('a{}'.format(rotulo_a),
                    vertices[v1], vertices[v2], self._peso(peso_min, peso_max))
                rotulo_a += 1

        return self

    @arestas.register
    def _(self, arg:list, **kwargs):
        for aresta in arg:
            self._grafo.adiciona_aresta(aresta)
        return self
