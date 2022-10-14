from bibgrafo.grafo import GrafoIF
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from multipledispatch import dispatch
from copy import deepcopy


class GrafoListaAdjacencia(GrafoIF):

    """
    Esta classe representa um grafo com implementação interna em lista de adjacência

    Attributes:
        _vertices (list): Uma lista dos vértices (ou nodos) do grafo.
        _arestas: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é um
        objeto do tipo Aresta que deve conter referências para os vértices
    """

    def __init__(self, vertices=None, arestas=None):
        """
        Constrói um objeto do tipo GrafoListaAdjacencia. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, um erro é lançado.
        Nessa implementação o Grafo é representado por uma lista de adjacências.

        Args:
            vertices: Uma lista dos vértices (ou nodos) do grafo.
            arestas: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é um
            objeto do tipo Aresta que deve conter uma referência para os vértices
        """

        if vertices is None:
            vertices = list()
        else:
            for v in vertices:
                if not (GrafoListaAdjacencia.vertice_valido(v)):
                    raise VerticeInvalidoError('O vértice ' + v + ' é inválido')
        self._vertices = deepcopy(vertices)

        if arestas is None:
            arestas = dict()
        else:
            for a in arestas:
                if not(self.aresta_valida(arestas[a])):
                    raise ArestaInvalidaError('A aresta ' + arestas[a] + ' é inválida')

        self._arestas = deepcopy(arestas)

    @property
    def vertices(self):
        """ list: Uma lista de vértices. """
        return self._vertices

    @vertices.setter
    def vertices(self, novos_vertices):
        if novos_vertices is None:
            novos_vertices = list()
        else:
            for v in novos_vertices:
                if not(GrafoListaAdjacencia.vertice_valido(v)):
                    raise VerticeInvalidoError('O vértice ' + v + ' é inválido')
        self._vertices = deepcopy(novos_vertices)

    @property
    def arestas(self):
        """ dict: Um dicionário de arestas. """
        return self._arestas

    @arestas.setter
    def arestas(self, novas_arestas):
        if novas_arestas is None:
            novas_arestas = dict()
        else:
            for a in novas_arestas:
                if not(self.aresta_valida(novas_arestas[a])):
                    raise ArestaInvalidaError('A aresta ' + novas_arestas[a] + ' é inválida')

        self._arestas = deepcopy(novas_arestas)

    @classmethod
    def vertice_valido(cls, vertice: Vertice) -> bool:
        """
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        O rótulo do vértice não pode ser vazio.
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
        Return: Um valor booleano que indica se o vértice existe no grafo.
        """
        return GrafoListaAdjacencia.vertice_valido(vertice) and vertice in self._vertices

    def existe_rotulo_vertice(self, rotulo: str) -> bool:
        """
        Verifica se há algum vértice no grafo com o rótulo que é passado como parâmetro.
        Args:
            rotulo: O vértice que deve ser verificado.
        Returns:
            Um valor booleano que indica se o vértice existe no grafo.
        """
        for i in range(len(self.vertices)):
            if self.vertices[i].rotulo == rotulo:
                return True
        return False

    def get_vertice(self, rotulo: str) -> Vertice:
        """
        Retorna o objeto do tipo vértice que tem como rótulo o parâmetro passado.
        Args:
            rotulo: O rótulo do vértice a ser retornado
        Returns:
            Um objeto do tipo vértice que tem como rótulo o parâmetro passado
        Raises:
            VerticeInvalidoError se o vértice não for encontrado.
        """
        if not self.existe_rotulo_vertice(rotulo):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        for i in range(len(self._vertices)):
            if self._vertices[i].rotulo == rotulo:
                return self._vertices[i]

    @dispatch(str)
    def adiciona_vertice(self, rotulo: str):
        """
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        Args:
            rotulo: O rótulo do vértice a ser adicionado
        Raises:
            VerticeInvalidoError se já houver um vértice com o mesmo nome no grafo
        """
        if not self.existe_rotulo_vertice(rotulo):
            self._vertices.append(Vertice(rotulo))
        else:
            raise VerticeInvalidoError('O rótulo de vértice ' + rotulo + ' já existe no grafo')

    @dispatch(Vertice)
    def adiciona_vertice(self, v: Vertice):
        """
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        Args:
            v: O vértice a ser adicionado
        Raises:
            VerticeInvalidoError se o vértice passado como parâmetro não puder ser adicionado
        """
        if self.vertice_valido(v) and not self.existe_vertice(v) and not self.existe_rotulo_vertice(v.rotulo()):
            self._vertices.append(v)
        else:
            raise VerticeInvalidoError('O vértice ' + str(v) + ' é inválido ou já existe no grafo')

    def remove_vertice(self, v: str):
        """
        Remove um vértice que tenha o rótulo passado como parâmetro e remove em cascata as arestas que estão
        conectadas a esse vértice.
        Args:
            v: O rótulo do vértice a ser removido.
        Raises:
            VerticeInvalidoError se o vértice passado como parâmetro não existir no grafo.
        """
        newA = dict()
        if self.existe_rotulo_vertice(v):
            self._vertices.remove(v)
            for a in self._arestas.keys():
                if not(self._arestas[a].eh_ponta(v)):
                    newA[a] = self._arestas[a]
            self._arestas = newA
        else:
            raise VerticeInvalidoError('O vértice {} não existe no grafo.'.format(v))

    def existe_rotulo_aresta(self, r=''):
        """
        Verifica se um rótulo de aresta passada como parâmetro pertence ao grafo.
        Args:
            r: O rótulo da aresta a ser verificada
        Returns:
            Um valor booleano que indica se o rótulo da aresta existe no grafo.
        """
        return r in self._arestas

    def get_aresta(self, r):
        """
        Retorna uma referência para a aresta que tem o rótulo passado como parâmetro
        Args:
            r: O rótulo da aresta solicitada
        Returns:
            Um objeto do tipo Aresta que é uma referência para a aresta requisitada ou False se a aresta não existe
        """
        if self.existe_rotulo_aresta(r):
            return self._arestas[r]
        return False
    
    def aresta_valida(self, aresta: Aresta):
        """
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo e for uma instância da classe Aresta.
        Args:
            aresta: A aresta que se quer verificar se está no formato correto.
        Returns:
            Um valor booleano que indica se a aresta está no formato correto.
        """

        # Verifica se os vértices existem no Grafo
        if isinstance(aresta, Aresta) and \
                self.existe_vertice(aresta.v1) and self.existe_vertice(aresta.v2):
            return True
        return False

    @dispatch(Aresta)
    def adiciona_aresta(self, a: Aresta):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome.
        Args:
            a: Um objeto do tipo aresta a ser adicionado no grafo.
        Returns:
            True se a aresta foi adicionada com sucesso
        Raises:
            ArestaInvalidaError se a aresta passada como parâmetro não puder ser adicionada
        """
        if self.aresta_valida(a):
            if not self.existe_rotulo_aresta(a.rotulo):  # Verifica se a aresta já existe no grafo
                self._arestas[a.rotulo] = a
            else:
                raise ArestaInvalidaError('A aresta {} não pode ter o mesmo rótulo de uma aresta já existente'
                                          'no grafo'.format(str(a)))
        else:
            raise ArestaInvalidaError('A aresta ' + str(a) + ' é inválida')
        return True

    @dispatch(str, str, str, int)
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str, peso: int = 1):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        Args:
            rotulo: O rótulo da aresta a ser adicionada
            v1: O primeiro vértice da aresta
            v2: O segundo vértice da aresta
            peso: O peso da aresta
        Returns:
            True se a aresta foi adicionada com sucesso
        Raises:
            ArestaInvalidaError se a aresta passada como parâmetro não puder ser adicionada
        """
        a = Aresta(rotulo, self.get_vertice(v1), self.get_vertice(v2), peso)
        return self.adiciona_aresta(a)

    @dispatch(str, str, str)
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome.
        O peso atribuído à aresta será 1.
        Args:
            rotulo: O rótulo da aresta a ser adicionada.
            v1: O primeiro vértice da aresta.
            v2: O segundo vértice da aresta.
        Returns:
            True se a aresta foi adicionada com sucesso.
        Raises:
            ArestaInvalidaError se a aresta passada como parâmetro não puder ser adicionada.
        """
        a = Aresta(rotulo, self.get_vertice(v1), self.get_vertice(v2), 1)
        return self.adiciona_aresta(a)

    def remove_aresta(self, r: str):
        """
        Remove uma aresta a partir de seu rótulo.
        Args:
            r: O rótulo da aresta a ser removida.
        Raises:
            ArestaInvalidaError se a aresta passada como parâmetro não puder ser removida.
        """
        if self.existe_rotulo_aresta(r):
            self._arestas.pop(r)
        else:
            raise ArestaInvalidaError('A aresta {} não existe no grafo'.format(r))

    def __eq__(self, other):
        """
        Define a igualdade entre a instância do GrafoListaAdjacencia para o qual essa função foi chamada e a
        instância de um GrafoListaAdjacencia passado como parâmetro.
        Args:
            other: O grafo que deve ser comparado com este grafo.
        Returns:
            Um valor booleano caso os grafos sejam iguais.
        """
        if len(self._arestas) != len(other._arestas) or len(self._vertices) != len(other._vertices):
            return False
        for n in self._vertices:
            if not other.existe_vertice(n):
                return False
        for a in self._arestas:
            if not self.existe_rotulo_aresta(a) or not other.existe_rotulo_aresta(a):
                return False
            if not self._arestas[a] == other.get_aresta(a):
                return False
        return True

    def __str__(self):
        """
        Fornece uma representação do tipo String do grafo. O String contém um sequência dos vértices separados por
        vírgula, seguido de uma sequência das arestas no formato padrão.
        Returns:
            Uma string que representa o grafo.
        """
        grafo_str = ''

        for v in range(len(self._vertices)):
            grafo_str += str(self._vertices[v])
            if v < (len(self._vertices) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self._arestas):
            grafo_str += str(self._arestas[a]) + '\n'

        return grafo_str
