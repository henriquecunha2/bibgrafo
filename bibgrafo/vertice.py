class Vertice:
    """
    Esta classe representa um vértice de um grafo.

    Attributes:
        _rotulo (str): O rótulo (ou nome) do vértice
    """

    _rotulo: str
    _attr: dict

    def __init__(self, rotulo: str, attr=None):
        """
        Constrói um objeto do tipo Vertice.

        Args:
            rotulo (str): O rótulo (ou nome) do vértice.
            attr (dict): Um dicionário de atributos do vértice
        """
        self._rotulo = rotulo
        if attr is None:
            self._attr = dict()
        else:
            self._attr = attr

    @property
    def rotulo(self):
        """ str: O rótulo (ou nome) do vértice. """
        return self._rotulo

    @rotulo.setter
    def rotulo(self, r: str):
        if type(r) is not str:
            raise TypeError("O tipo do rótulo deve ser string")
        self._rotulo = r

    @property
    def attr(self):
        """
        dict: Um dicionário de atributos do vértice.
        De acordo com a modelagem que se deseja fazer, vértices podem ter atributos não previstos nessa implementação.
        Dessa forma, foi incluído um dicionário de atributos para que o usuário possa incluir outros atributos que
        desejar.
        """
        return self._attr

    @attr.setter
    def attr(self, attr: dict):
        if type(attr) is not dict:
            raise TypeError("O tipo do atributo deve ser dict.")
        self._attr = attr

    def adiciona_attr(self, chave, valor):
        """
        Adiciona um novo atributo para o vértice.

        Args:
            chave: A chave para armazenamento do atributo no dicionário.
            valor: O valor associado à chave.
        """
        self._attr[chave] = valor

    def remove_attr(self, chave):
        """
        Adiciona um novo atributo para o vértice.

        Args:
            chave: A chave do atributo que deve ser removido.
        """
        self._attr.pop(chave)

    def get_um_attr(self, chave):
        """
        Retorna o valor de um atributo definido pelo usuário da classe

        Args:
            chave: A chave do atributo para o qual deve ser retornado o valor
        """
        return self._attr[chave]

    def __eq__(self, other):
        """
        É chamado quando se tenta usar o operador de igualdade entre um Vertive e outro objeto.

        Args:
            other: O outro objeto que se deseja verificar a igualdade.

        Returns:
            True se os objetos forem iguais ou False, caso contrário.
        """
        return self.rotulo == other.rotulo and \
               self.attr == other.attr

    def __str__(self):
        """
        Fornece uma representação em String de um vértice
        """
        return self.rotulo
