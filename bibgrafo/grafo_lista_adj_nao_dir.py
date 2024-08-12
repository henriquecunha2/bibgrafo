from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.aresta import Aresta
from bibgrafo.grafo_errors import *
from functools import singledispatchmethod


class GrafoListaAdjacenciaNaoDirecionado(GrafoListaAdjacenciaDirecionado):

    """
    Esta classe representa um grafo com implementação interna em lista de adjacência
    não-direcionada, herdando a maioria dos métodos da classe GrafoListaAdjacenciaDirecionado,
    porém utilizando em sua implementação interna a classe bibgrafo.Aresta ao invés de bibgrafo.ArestaDirecionada.

    Attributes:
        _vertices (list): Uma lista dos vértices (ou nodos) do grafo.
        _arestas: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é um
        objeto do tipo Aresta que deve conter referências para os vértices
    """
    
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

    @singledispatchmethod
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

    @adiciona_aresta.register
    def _(self, rotulo: str, v1: str, v2: str, peso: int = 1):
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

    def __eq__(self, other):
        """
        Define a igualdade entre a instância do GrafoListaAdjacenciaNaoDirecionado para o qual essa função foi chamada e a
        instância de um GrafoListaAdjacenciaNaoDirecionado passado como parâmetro.
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
