from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from multipledispatch import dispatch


class GrafoIF:
    SEPARADOR_ARESTA = '-'

    @classmethod
    def vertice_valido(cls, vertice: Vertice) -> bool:
        """
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        O rótulo do vértice não pode ser vazio.
        :param vertice: Um objeto do tipo Vertice que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        """
        pass

    def existe_vertice(self, vertice: Vertice) -> bool:
        """
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        """
        pass

    def existe_rotulo_vertice(self, rotulo: str) -> bool:
        """
        Verifica se há algum vértice no grafo com o rótulo que é passado como parâmetro.
        :param rotulo: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        """
        pass

    def get_vertice(self, rotulo: str) -> Vertice:
        """
        Retorna o objeto do tipo vértice que tem como rótulo o parâmetro passado.
        :param rotulo: O rótulo do vértice a ser retornado
        :return: Um objeto do tipo vértice que tem como rótulo o parâmetro passado
        :raises: VerticeInvalidoError se o vértice não for encontrado.
        """
        pass

    @dispatch(str)
    def adiciona_vertice(self, rotulo: str):
        """
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param rotulo: O rótulo do vértice a ser adicionado
        :raises: VerticeInvalidoError se já houver um vértice com o mesmo nome no grafo
        """
        pass

    @dispatch(Vertice)
    def adiciona_vertice(self, v: Vertice):
        """
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoError se o vértice passado como parâmetro não puder ser adicionado
        """
        pass

    def remove_vertice(self, v: str):
        """
        Remove um vértice que tenha o rótulo passado como parâmetro e remove em cascata as arestas que estão
        conectadas a esse vértice.
        :param v: O rótulo do vértice a ser removido.
        :raises: VerticeInvalidoError se o vértice passado como parâmetro não existir no grafo.
        """
        pass

    def existe_rotulo_aresta(self, r: str) -> bool:
        """
        Verifica se um rótulo de aresta passada como parâmetro pertence ao grafo.
        :param r: O rótulo da aresta a ser verificada
        :return: Um valor booleano que indica se o rótulo da aresta existe no grafo.
        """
        pass

    def get_aresta(self, r):
        """
        Retorna uma referência para a aresta que tem o rótulo passado como parâmetro
        :param r: O rótulo da aresta solicitada
        :return: Um objeto do tipo Aresta que é uma referência para a aresta requisitada ou False se a aresta não existe
        """
        pass

    def aresta_valida(self, aresta: Aresta):
        """
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo e for uma instância da classe Aresta.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        """
        pass

    @dispatch(Aresta)
    def adiciona_aresta(self, a: Aresta):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome.
        :param a: Um objeto do tipo aresta a ser adicionado no grafo.
        :raises: ArestaInvalidaError se a aresta passada como parâmetro não puder ser adicionada
        :returns: True se a aresta foi adicionada com sucesso
        """
        pass

    @dispatch(str, str, str, int)
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str, peso: int = 1):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param rotulo: O rótulo da aresta a ser adicionada
        :param v1: O primeiro vértice da aresta
        :param v2: O segundo vértice da aresta
        :param peso: O peso da aresta
        :raises: ArestaInvalidaError se a aresta passada como parâmetro não puder ser adicionada
        :returns: True se a aresta foi adicionada com sucesso
        """
        pass

    @dispatch(str, str, str)
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome.
        O peso atribuído à aresta será 1.
        :param rotulo: O rótulo da aresta a ser adicionada
        :param v1: O primeiro vértice da aresta
        :param v2: O segundo vértice da aresta
        :raises: ArestaInvalidaError se a aresta passada como parâmetro não puder ser adicionada
        :returns: True se a aresta foi adicionada com sucesso
        """
        pass

    def remove_aresta(self, r: str):
        """
        Remove uma aresta a partir de seu rótulo
        :param r: O rótulo da aresta a ser removida
        :raises: ArestaInvalidaError se a aresta passada como parâmetro não puder ser removida
        """
        pass

    def __eq__(self, other):
        """
        Define a igualdade entre a instância do Grafo para o qual essa função foi chamada e a instância de um Grafo
        passado como parâmetro.
        :param other: O grafo que deve ser comparado com este grafo.
        :return: Um valor booleano caso os grafos sejam iguais.
        """
        pass

    def __str__(self) -> str:
        """
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no
        formato v1-v2.
        Em que v1 é o primeiro vértice, v2 é o segundo vértice e o traço (-) é uma representação do caractere separador.
        :return: Uma string que representa o grafo
        """
        pass
