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
            __grafo: receberá a instância de GrafoIF na qual serão realizadas as operações
            de inserção de vértices e arestas, conforme requerido.
    '''
    def __init__(self):
        self.__grafo = None

    def build(self):
        '''
            Esta função deve ser chamada ao final de todas as outras, retornando a instância
            do grafo criado pelo GrafoBuilder.
        '''
        return self.__grafo

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

        self.__grafo = grafo
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
                    self.__grafo.adiciona_vertice(v)
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
                    self.__grafo.adiciona_vertice(''.join(rotulo_v))
                else: self.__grafo.adiciona_vertice(chr(ord(start) + i))
        return self

    def arestas(self, arestas=list(), completo=False, qtd=1, laco=False, qtd_laco=1,
        conexo=True, qtd_desconexo=2, paralelas=False, qtd_paralelas=1, peso_max=1, peso_min=0):
        '''
            Esta função recebe os parâmetros para inserção das arestas pelo GrafoBuilder.
            Args:
                arestas: recebe uma lista de objetos do tipo bibgrafo.Aresta ou bibgrafo.ArestaDirecionada,
                para serem inseridas pelo GrafoBuilder. Caso essa opção seja utilizada, todas as outras serão
                ignoradas.
                completo: se marcada como True, o grafo gerado será obrigatoriamente um grafo completo
                a partir dos vértices gerados na função anterior. Caso essa opção seja utilizada,
                todas as outras a partir dela serão ignoradas, tendo ela prioridade logo após a opção 'arestas'.

                Caso nenhuma dessas opções seja utilizada, o GrafoBuilder irá gerar um grafo simples.
                qtd: a quantidade de arestas a serem adicionadas.
                laco: caso marcada, após a criação de arestas para um grafo simples, a função irá
                adicionar laços no grafo.
                qtd_laco: a quantidade de lacos a serem adicionados.
                conexo: se marcada como False, o GrafoBuilder irá gerar um grafo completo com alguns
                vértices desconexos e adicionar as suas arestas ao seu próprio grafo.
                qtd_desconexo: a quantidade de vértices desconexos.
                paralelas: se marcada como True, o GrafoBuilder irá gerar arestas paralelas após a criação
                de um grafo simples.
                qtd_paralelas: a quantidade de arestas paralelas presentes no grafo.

                (As opções a seguir também podem ser utilizadas na criação de grafos completos)
                peso_max: o peso máximo das arestas.
                peso_min: o peso mínimo das arestas.
            Raises:
                GrafoBuilderError:
                    - quando o intervalo de peso_max e peso_min é inválido
                    - quando 'qtd' excede [n + (n - 1)] / 2, sendo 'n' o número de vértices
                    - quando a quantidade de vértices desconexos é maior que o número de vértices
                    - se a lista de vértices estiver vazia
        '''

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
            pares_arestas = list()
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
                pares_arestas.append(par_v)

            if paralelas:
                arestas = [a for a in self.__grafo.arestas.values()]
                for i in range(qtd_paralelas):
                    a = pares_arestas[randint(0, len(pares_arestas) - 1)]
                    self.__grafo.adiciona_aresta(str(i) + 'p',
                        a[0], a[1], peso(peso_max))
        return self
