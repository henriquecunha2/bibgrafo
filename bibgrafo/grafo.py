from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from multipledispatch import dispatch


class GrafoIF:

    """
    Esta classe define uma interface que todos as classes que implementam um grafo devem ter.
    Esta classe não é concreta. Não deve ser instanciada.
    """

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
        pass

    def existe_vertice(self, vertice: Vertice) -> bool:
        """
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        Args:
            vertice: O vértice que deve ser verificado.
        Return: Um valor booleano que indica se o vértice existe no grafo.
        """
        pass

    def existe_rotulo_vertice(self, rotulo: str) -> bool:
        """
        Verifica se há algum vértice no grafo com o rótulo que é passado como parâmetro.
        Args:
            rotulo: O vértice que deve ser verificado.
        Returns:
            Um valor booleano que indica se o vértice existe no grafo.
        """
        pass

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
        pass

    @dispatch(str)
    def adiciona_vertice(self, rotulo: str):
        """
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        Args:
            rotulo: O rótulo do vértice a ser adicionado
        Raises:
            VerticeInvalidoError se já houver um vértice com o mesmo nome no grafo
        """
        pass

    @dispatch(Vertice)
    def adiciona_vertice(self, v: Vertice):
        """
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        Args:
            v: O vértice a ser adicionado
        Raises:
            VerticeInvalidoError se o vértice passado como parâmetro não puder ser adicionado
        """
        pass

    def remove_vertice(self, v: str):
        """
        Remove um vértice que tenha o rótulo passado como parâmetro e remove em cascata as arestas que estão
        conectadas a esse vértice.
        Args:
            v: O rótulo do vértice a ser removido.
        Raises:
            VerticeInvalidoError se o vértice passado como parâmetro não existir no grafo.
        """
        pass

    def existe_rotulo_aresta(self, r: str) -> bool:
        """
        Verifica se um rótulo de aresta passada como parâmetro pertence ao grafo.
        Args:
            r: O rótulo da aresta a ser verificada
        Returns:
            Um valor booleano que indica se o rótulo da aresta existe no grafo.
        """
        pass

    def get_aresta(self, r):
        """
        Retorna uma referência para a aresta que tem o rótulo passado como parâmetro
        Args:
            r: O rótulo da aresta solicitada
        Returns:
            Um objeto do tipo Aresta que é uma referência para a aresta requisitada ou False se a aresta não existe
        """
        pass

    def aresta_valida(self, aresta: Aresta):
        """
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo e for uma instância da classe Aresta.
        Args:
            aresta: A aresta que se quer verificar se está no formato correto.
        Returns:
            Um valor booleano que indica se a aresta está no formato correto.
        """
        pass

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
        pass

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
        pass

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
        pass

    def remove_aresta(self, r: str):
        """
        Remove uma aresta a partir de seu rótulo.
        Args:
            r: O rótulo da aresta a ser removida.
        Raises:
            ArestaInvalidaError se a aresta passada como parâmetro não puder ser removida.
        """
        pass

    def __eq__(self, other) -> bool:
        """
        Define a igualdade entre a instância do GrafoListaAdjacencia para o qual essa função foi chamada e a
        instância de um GrafoListaAdjacencia passado como parâmetro.
        Args:
            other: O grafo que deve ser comparado com este grafo.
        Returns:
            Um valor booleano caso os grafos sejam iguais.
        """
        pass

    def __str__(self) -> str:
        """
        Fornece uma representação do tipo String do grafo.
        Returns:
            Uma string que representa o grafo.
        """
        pass
