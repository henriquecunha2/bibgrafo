from functools import singledispatchmethod
from random import randint, shuffle
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

    @singledispatchmethod
    def vertices(self, arg:int, **kwargs):
        '''
            Esta assinatura da função vertices recebe um número inteiro
            representando a quantidade de vértices a serem inseridos.
            Args:
                arg: número inteiro positivo para a quantidade de vértices
                a serem adicionados no grafo.
            Kwargs:
                start: argumento opcional que recebe uma letra maiúscula,
                que será o rótulo o primeiro vértice, a partir do qual
                serão definidos os rótulos seguintes. O seu valor padrão
                é a letra "A".
            Raises:
                GrafoBuilderError: caso o valor de arg seja menor que zero
                ou caso o caractere passado para 'start' não seja uma letra maiúscula
        '''
        if arg < 0: raise GrafoBuilderError('Forneça um número de vértices válido')
        start = kwargs.get('start', 'A')
        if not start.isupper() or not start.isalpha():
            raise GrafoBuilderError('O rótulo dos vértices deve ser uma letra maiúscula')

        START_MAX = ord('Z') - ord(start) + 1
        for i in range(arg):
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

    @vertices.register
    def _(self, arg: list, **kwargs):
        '''
            Esta assinatura da função vertices recebe uma lista de vértices
            a serem adicionados no grafo.
            Args:
                arg: lista de vértices, podendo ser do tipo bibgrafo.Vertice
                ou strings, representando os seus rótulos.
            Raises:
                GrafoBuilderError: caso arg seja uma lista vazia.
        '''
        if len(arg) == 0: raise GrafoBuilderError('A lista de vértices não pode estar vazia')
        for v in arg:
            self._grafo.adiciona_vertice(v)

        return self

    def _peso(self, min, max):
        '''
            Função privada que randomiza o peso das arestas a serem adicionadas.
            Caso min e max sejam 0 e 1, respectivamente, o valor retornado será 1.
            Args:
                min: valor mínimo, que tem por padrão o valor 0.
                max: que tem por padrão o valor 1.
            Raises:
                GrafoBuilderError: caso o valor de min seja maior ou igual ao valor de max.
        '''
        if min >= max: raise GrafoBuilderError('Forneça um intervalo válido para o peso das arestas')
        if min == 0 and max == 1: return max
        else: return randint(min, max)

    @singledispatchmethod
    def arestas(self, arg: int, **kwargs):
        '''
            Esta assinatura de arestas recebe um número inteiro positivo, que representa
            a quantidade de arestas a serem adicionadas. Caso não sejam especificadas
            quantidades de laços ou arestas paralelas, o grafo gerado será um grafo
            simples. Também é possível especificar uma quantidade de vértices desconexos,
            gerando assim um subgrafo completo entre estes.
            Args:
                arg: número inteiro positivo, quantidade de arestas a serem adicionadas.
            Kwargs:
                peso_min: peso mínimo possível das arestas.
                peso_max: peso máximo possível das arestas.
                lacos: quantidade de laços a serem adicionados.
                paralelas: quantidade de arestas paralelas a serem adicionadas.
                desconexos: quantidade de vértices desconexos. Máximo: n - 2
            Raises:
                GrafoBuilderError: se algum dos parâmetros passados for inválido (ex.: número
                negativo de arestas ou laços), se o número de arestas for grande demais
                para um grafo simples (máximo: (n * (n - 1)) / 2), ou se a lista de vértices
                não tiver sido implementada no grafo.
        '''
        vertices = [v.rotulo for v in self._grafo.vertices]
        if arg > (len(vertices) * (len(vertices) - 1)) / 2 or arg < 0:
            raise GrafoBuilderError('Não é possível construir um grafo com esta quantidade de arestas')
        if len(vertices) == 0: raise GrafoBuilderError('A lista de vértices ainda está vazia')

        desconexos = kwargs.get('desconexos', 0)
        if desconexos < 0 or desconexos >= len(vertices) - 1:
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
        '''
            Esta assinatura da função arestas recebe um valor booleano,
            sinalizando assim que o grafo a ser construído deve ser um grafo
            Kn, sendo n o número de vértices adicionados.
            Args:
                arg: valor booleano.
            Kwargs:
                peso_min: peso mínimo possível das arestas.
                peso_max: peso máximo possível das arestas.
            Raises:
                GrafoBuilderError: caso a lista de vértices ainda estiver vazia.
        '''
        peso_min = kwargs.get('peso_min', 0)
        peso_max = kwargs.get('peso_max', 1)
        vertices = [v.rotulo for v in self._grafo.vertices]
        if len(vertices) == 0: raise GrafoBuilderError('A lista de vértices ainda está vazia')
        rotulo_a = 1
        for v1 in range(len(vertices)):
            for v2 in range(v1 + 1, len(vertices)):
                self._grafo.adiciona_aresta('a{}'.format(rotulo_a),
                    vertices[v1], vertices[v2], self._peso(peso_min, peso_max))
                rotulo_a += 1

        return self

    @arestas.register
    def _(self, arg:list, **kwargs):
        '''
            Esta assinatura da função arestas recebe uma lista de objetos
            do tipo bibgrafo.Aresta, que serão adicionadas no grafo.
            É possível também usar os parâmetros opcionais de peso_min
            e peso_max para randomizar o peso das arestas passadas.
            Args:
                arg: lista de objetos do tipo bibgrafo.Aresta.
            Kwargs:
                peso_min: peso mínimo possível das arestas.
                peso_max: peso máximo possível das arestas.
            Raises:
                GrafoBuilderError: caso a lista de vértices ainda estiver vazia
                ou se a lista de arestas passadas estiver vazia.
        '''
        peso_min = kwargs.get('peso_min', 0)
        peso_max = kwargs.get('peso_max', 1)
        if peso_min != 0 and peso_max != 1:
            for aresta in arg: aresta.peso = self._peso(peso_min, peso_max)

        if len(self._grafo.vertices) == 0: raise GrafoBuilderError('A lista de vértices ainda está vazia')
        elif len(arg) == 0: raise GrafoBuilderError('A lista de arestas não pode estar vazia')
        for aresta in arg:
            self._grafo.adiciona_aresta(aresta)
        return self
