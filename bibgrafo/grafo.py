class GrafoIF():

    SEPARADOR_ARESTA = '-'

    def vertice_valido(self, vertice='') -> bool:
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        O caractere separador serve para prover uma representação em string do grafo e pode ser alterado com o método setCaractereSeparador().
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        pass

    def aresta_valida(self, aresta=tuple()) -> bool:
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um tupla com o formato (a, b), onde:
        a é um string de aresta que é o nome de um vértice adjacente à aresta.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''
        pass

    def existe_vertice(self, vertice='') -> bool:
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        pass

    def existe_rotulo_aresta(self, aresta='') -> bool:
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        pass

    def adiciona_vertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        pass

    def adiciona_aresta(self, nome='', a=tuple()):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param a: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        pass

    def remove_vertice(self, v):
        '''
        Remove um vértice passado como parâmetro e remove em cascata as arestas que estão conectadas a esse vértice.
        :param v: O vértice a ser removido.
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser removido.
        '''
        pass

    def remove_aresta(self, r):
        '''
        Remove uma aresta a partir de seu rótulo
        :param r: O rótulo da aresta a ser removida
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser removida
        '''
        pass

    def __eq__(self, other):
        '''
        Define a igualdade entre a instância do Grafo para o qual essa função foi chamada e a instância de um Grafo passado como parâmetro.
        :param other: O grafo que deve ser comparado com este grafo.
        :return: Um valor booleano caso os grafos sejam iguais.
        '''
        pass

    def __str__(self) -> str:
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato v1-v2.
        Em que v1 é o primeiro vértice, v2 é o segundo vértice e o traço (-) é uma representação do caractere separador.
        :return: Uma string que representa o grafo
        '''
        pass































