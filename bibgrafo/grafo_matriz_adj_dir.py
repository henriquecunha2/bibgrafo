from bibgrafo.grafo import GrafoIF
from bibgrafo.aresta import ArestaDirecionada
from bibgrafo.grafo_errors import *
from bibgrafo.vertice import Vertice
from multipledispatch import dispatch
from copy import deepcopy

class GrafoMatrizAdjacenciaDirecionado(GrafoIF):

    """
    Esta classe representa um grafo direcionado com implementação interna em matriz de adjacência

    Attributes:
        _vertices (list): Uma lista dos vértices (ou nodos) do grafo.
        _matriz: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um
        dicionário de arestas (objetos do tipo Aresta) para que seja possível representar arestas paralelas
        e que cada aresta tenha seus próprios atributos distintos.
    """

    def __init__(self, vertices: list = None, matriz: list = None):
        """
        Constrói um objeto do tipo grafo direcionado com matriz de adjacência.
        Se nenhum parâmetro for passado, cria um grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        Args:
            vertices: Uma lista dos vértices (ou nodos) do grafo.
            matriz: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um
            dicionário de arestas (objetos do tipo Aresta) para que seja possível representar arestas paralelas
            e que cada aresta tenha seus próprios atributos distintos.
        """

        if vertices is None:
            vertices = list()
        if matriz is None:
            matriz = list()

        for v in vertices:
            if not (GrafoMatrizAdjacenciaDirecionado.vertice_valido(v)):
                raise VerticeInvalidoError('O vértice ' + v + ' é inválido.')

        self._vertices = deepcopy(vertices)

        if not matriz:
            self._matriz = list()
            for k in range(len(vertices)):
                self._matriz.append(list())
                for m in range(len(vertices)):
                    self._matriz[k].append(dict())

        if len(self._matriz) != len(vertices):
            raise MatrizInvalidaError('A matriz passada como parâmetro não tem o tamanho correto.')

        for c in self._matriz:
            if len(c) != len(vertices):
                raise MatrizInvalidaError('A matriz passada como parâmetro não tem o tamanho correto.')

        # Verifica se as arestas passadas na matriz são válidas
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                dicio_aresta = self._matriz[i][j]
                for k in dicio_aresta.values():
                    aresta = dicio_aresta[k]
                    if not (self.aresta_valida(aresta)):
                        raise ArestaInvalidaError('A aresta ' + aresta + ' é inválida.')

    @property
    def vertices(self):
        """ list: Uma lista de vértices. """
        return self._vertices

    @vertices.setter
    def vertices(self, novos_vertices):
        if novos_vertices is None:
            vertices = list()

        for v in vertices:
            if not (GrafoMatrizAdjacenciaDirecionado.vertice_valido(v)):
                raise VerticeInvalidoError('O vértice ' + v + ' é inválido')

        self._vertices = deepcopy(vertices)

    @property
    def matriz(self):
        """ list: Uma matriz de arestas. """
        return self._matriz

    @matriz.setter
    def matriz(self, nova_matriz):
        if not nova_matriz:
            self._matriz = list()
            for k in range(len(self.vertices)):
                self._matriz.append(list())
                for m in range(len(self.vertices)):
                    self._matriz[k].append(dict())

        if len(self._matriz) != len(self.vertices):
            raise MatrizInvalidaError('A matriz passada como parâmetro não tem o tamanho correto')

        for c in self._matriz:
            if len(c) != len(self.vertices):
                raise MatrizInvalidaError('A matriz passada como parâmetro não tem o tamanho correto')

        # Verifica se as arestas passadas na matriz são válidas
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                dicio_aresta = self._matriz[i][j]
                for k in dicio_aresta.values():
                    aresta = dicio_aresta[k]
                    if not (self.aresta_valida(aresta)):
                        raise ArestaInvalidaError('A aresta ' + aresta + ' é inválida')

    @classmethod
    def vertice_valido(cls, vertice: Vertice) -> bool:
        """
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice não pode ter um rótulo vazio.
        Args:
            vertice: Um objeto do tipo Vertice que representa o vértice a ser analisado.
        Returns:
            Um valor booleano que indica se o vértice está no formato correto.
        """
        return isinstance(vertice, Vertice) and vertice.rotulo != ""

    def existe_vertice(self, vertice: Vertice) -> bool:
        """
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        Args:
            vertice: O vértice que deve ser verificado.
        Returns:
            Um valor booleano que indica se o vértice existe no grafo.
        """
        return GrafoMatrizAdjacenciaDirecionado.vertice_valido(vertice) and vertice in self._vertices

    def get_vertice(self, rotulo: str):
        """
        Retorna o objeto do tipo vértice que tem como rótulo o parâmetro passado.
        Args:
            rotulo: O rótulo do vértice a ser retornado
        Returns:
            Um objeto do tipo vértice que tem como rótulo o parâmetro passado ou False se o vértice não
            for encontrado.
        """
        for i in self._vertices:
            if rotulo == i.rotulo:
                return i

    def existe_rotulo_vertice(self, rotulo: str):
        """
        Verifica se há algum vértice no grafo com o rótulo que é passado como parâmetro.
        Args:
            rotulo: O vértice que deve ser verificado.
        Returns:
            Um valor booleano que indica se o vértice existe no grafo.
        """
        return self.get_vertice(rotulo) is not None

    def indice_do_vertice(self, v: Vertice):
        """
        Dado um vértice retorna o índice do vértice na lista de vértices.
        Pode ser usado para indexar a matriz.
        Args:
            v: O vértice a ser analisado
        Returns:
            O índice do primeiro vértice da aresta na lista de vértices
        """
        return self._vertices.index(v)

    @dispatch(str)
    def adiciona_vertice(self, rotulo: str):
        """
        Inclui um vértice no grafo a partir de um rotulo. É criado um objeto do tipo Vertice com o rotulo inserido.
        Args:
            rotulo: O rótulo do vértice a ser incluído no grafo.
        Raises:
            VerticeInvalidoException: se o vértice já existe ou se ele não estiver no formato válido.
        """
        if self.existe_rotulo_vertice(rotulo):
            raise VerticeInvalidoError('O vértice {} já existe'.format(rotulo))

        if rotulo != "":

            self._vertices.append(Vertice(rotulo))  # Adiciona vértice na lista de vértices
            self._matriz.append([])  # Adiciona a linha

            for k in range(len(self._vertices)):
                self._matriz[k].append(dict())  # adiciona os elementos da coluna do vértice
                if k != len(self._vertices) - 1:
                    self._matriz[self.indice_do_vertice(self.get_vertice(rotulo))].append(
                        dict())  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoError('O vértice ' + rotulo + ' é inválido')

    @dispatch(Vertice)
    def adiciona_vertice(self, v: Vertice):
        """
        Inclui um vértice no grafo se ele estiver no formato correto.
        Args:
            v: O vértice a ser incluído no grafo.
        Raises:
            VerticeInvalidoException: se o vértice já existe ou se ele não estiver no formato válido.
        """
        if self.existe_vertice(v):
            raise VerticeInvalidoError('O vértice {} já existe'.format(v))

        if self.vertice_valido(v):

            self._vertices.append(v)  # Adiciona vértice na lista de vértices
            self._matriz.append([])  # Adiciona a linha

            for k in range(len(self._vertices)):
                self._matriz[k].append(dict())  # adiciona os elementos da coluna do vértice
                if k != len(self._vertices) - 1:
                    self._matriz[self._vertices.index(v)].append(dict())  # adiciona um zero no último elemento da linha

        else:
            raise VerticeInvalidoError('O vértice ' + str(v) + ' é inválido')

    def remove_vertice(self, rotulo: str):
        """
        Remove um vértice do grafo a partir do rótulo do vértice.
        Args:
            rotulo: O rótulo do vértice a ser removido do grafo.
        Returns:
            True se o vértice foi removido com sucesso.
        Raises:
            VerticeInvalidoException: se o vértice não for encontrado no grafo
        """
        if not self.existe_rotulo_vertice(rotulo):
            raise VerticeInvalidoError("O vértice passado como parâmetro não existe no grafo.")

        v = self.get_vertice(rotulo)

        v_i = self.indice_do_vertice(v)

        self._matriz.pop(v_i)

        for i in range(len(self._matriz)):
            self._matriz[i].pop(v_i)

        self._vertices.remove(v)
        return True

    def aresta_valida(self, aresta: ArestaDirecionada):
        """
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo.
        Args:
            aresta: A aresta que se quer verificar se está no formato correto.
        Returns:
            Um valor booleano que indica se a aresta está no formato correto.
        """

        # Verifica se os vértices existem no Grafo
        if type(aresta) == ArestaDirecionada and self.existe_vertice(aresta.v1) and self.existe_vertice(
                aresta.v2):
            return True
        return False

    def existe_aresta(self, aresta: ArestaDirecionada):
        """
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        Args:
            aresta: A aresta a ser verificada.
        Returns:
            Um valor booleano que indica se a aresta existe no grafo.
        """
        if GrafoMatrizAdjacenciaDirecionado.aresta_valida(self, aresta):
            if aresta.rotulo in \
                    self._matriz[self.indice_do_vertice(aresta.v1)][self.indice_do_vertice(aresta.v2)]:
                return True
        return False

    @dispatch(ArestaDirecionada)
    def adiciona_aresta(self, aresta: ArestaDirecionada):
        """
        Adiciona uma aresta ao grafo.
        Args:
            aresta: A aresta a ser adicionada.
        Raises:
            ArestaInvalidaError: caso a aresta não estiver em um formato válido.
        """
        if self.existe_aresta(aresta):
            raise ArestaInvalidaError('A aresta {} já existe no Grafo'.format(aresta))

        if self.aresta_valida(aresta):
            i_a1 = self.indice_do_vertice(aresta.v1)
            i_a2 = self.indice_do_vertice(aresta.v2)
            self._matriz[i_a1][i_a2][aresta.rotulo] = aresta
        else:
            raise ArestaInvalidaError('A aresta {} é inválida'.format(aresta))

        return True

    @dispatch(str, str, str, int)
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str, peso=1):
        """
        Adiciona uma aresta ao grafo.
        Args:
            rotulo: O rótulo da aresta.
            v1: O primeiro vértice da aresta.
            v2: O segundo vértice da aresta.
            peso: O peso da aresta.
        Raises:
            ArestaInvalidaError: caso a aresta não estiver em um formato válido.
        """
        a = ArestaDirecionada(rotulo, self.get_vertice(v1), self.get_vertice(v2), peso)
        return self.adiciona_aresta(a)

    @dispatch(str, str, str)
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str):
        """
        Adiciona uma aresta ao grafo.
        Args:
            rotulo: O rótulo da aresta
            v1: O primeiro vértice da aresta
            v2: O segundo vértice da aresta
        Raises:
            ArestaInvalidaError: caso a aresta não estiver em um formato válido
        """

        a = ArestaDirecionada(rotulo, self.get_vertice(v1), self.get_vertice(v2), 1)
        return self.adiciona_aresta(a)

    def remove_aresta(self, r: str, v1: str = None, v2: str = None):
        """
        Remove uma aresta do grafo. Os parâmetros v1 e v2 são opcionais e servem para acelerar a busca pela aresta de
        interesse.
        Se for passado apenas o parâmetro r, deverá ocorrer uma busca por toda a matriz.
        Args:
            r: O rótulo da aresta a ser removida.
            v1: O rótulo do vértice 1 da aresta a ser removida.
            v2: O rótulo do vértice 2 da aresta a ser removida.
        Raises:
            VerticeInvalidoError: caso a aresta não exista no grafo ou caso algum dos vértices passados não existam.
        Returns:
            Retorna True se a aresta foi removida com sucesso.
        """

        def percorre_e_remove(M, x):
            # linha
            for y in range(0, len(M)):
                # linha
                arestas_percorrer = M[x][y]
                for m in arestas_percorrer:
                    if r == m:
                        arestas_percorrer.pop(r)
                        return True

                # coluna
                arestas_percorrer = M[y][x]
                for m in arestas_percorrer:
                    if r == m:
                        arestas_percorrer.pop(r)
                        return True

        if v1 is None:
            if v2 is None:
                for i in range(len(self._matriz)):
                    for j in range(len(self._matriz)):
                        arestas = self._matriz[i][j]
                        for k in arestas:
                            if r == k:
                                arestas.pop(r)
                                return True
                return False
            elif self.existe_rotulo_vertice(v2):
                v2_i = self.indice_do_vertice(self.get_vertice(v1))
                percorre_e_remove(self._matriz, v2_i)
            elif not self.existe_rotulo_vertice(v2):
                raise VerticeInvalidoError("O vértice {} é inválido!".format(v2))

        else:
            if self.existe_rotulo_vertice(v1):
                v1_i = self.indice_do_vertice(self.get_vertice(v1))
                if self.existe_rotulo_vertice(v2):
                    v2_i = self.indice_do_vertice(self.get_vertice(v1))

                    arestas = self._matriz[v1_i][v2_i]
                    for k in arestas:
                        if r == k:
                            arestas.pop(r)
                            return True
                    return False
                else:
                    return percorre_e_remove(self._matriz, v1_i)
            else:
                raise VerticeInvalidoError("O vértice {} é inválido!".format(v1))

    def __eq__(self, other):
        """
        Define a igualdade entre a instância do grafo para o qual essa função foi chamada e a instância de um
        GrafoMatrizAdjacenciaDirecionado passado como parâmetro.
        Args:
            other: O grafo que deve ser comparado com este grafo.
        Returns:
            Um valor booleano caso os grafos sejam iguais.
        """
        if len(self.matriz) != len(other.matriz) or len(self.vertices) != len(other.vertices):
            return False
        for n in self.vertices:
            if not other.existe_vertice(n):
                return False
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if len(self.matriz[i][j]) != len(other.matriz[i][j]):
                    return False
                for k in self.matriz[i][j]:
                    if k not in other.matriz[i][j]:
                        return False
        return True

    def __str__(self):
        """
        Fornece uma representação do tipo String do grafo.
        Returns:
            Uma string que representa o grafo
        """

        grafo_str = '  '

        for v in range(len(self._vertices)):
            grafo_str += str(self._vertices[v])
            if v < (len(self._vertices) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for m in range(len(self._matriz)):
            grafo_str += str(self._vertices[m]) + ' '
            for c in range(len(self._matriz)):
                if bool(self._matriz[m][c]):
                    grafo_str += '*' + ' '
                else:
                    grafo_str += 'o' + ' '
            grafo_str += '\n'

        for m in range(len(self._vertices)):
            for c in range(len(self._vertices)):
                if bool(self._matriz[m][c]):
                    grafo_str += str(self._vertices[m]) + '-' + str(self._vertices[c]) + ': '
                    for k in self._matriz[m][c]:
                        grafo_str += k
                    grafo_str += '\n'

        return grafo_str
