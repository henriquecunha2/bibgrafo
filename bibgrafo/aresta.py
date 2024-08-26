from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import VerticeInvalidoError

class Aresta:
    """
    Esta classe representa uma aresta de um Grafo.

    Attributes:
        _rotulo (str): O rótulo (ou nome) da aresta
        _v1 (Vertice): O primeiro vértice da aresta
        _v2 (Vertice): O segundo vértice da aresta
        _peso (int): O peso da aresta
    """

    _rotulo: str
    _v1: Vertice
    _v2: Vertice
    _peso: int

    def __init__(self, rotulo: str, v1: Vertice, v2: Vertice, peso: int = 1):
        """
        Constrói um objeto do tipo Aresta.
        Se o peso não for especificado, será considerado 1.
        Args:
            rotulo (str): O rótulo (ou nome) do vértice.
            v1 (Vertice): O primeiro vértice da aresta.
            v2 (Vertice): O segundo vértice da aresta.
            peso (int): O peso da aresta.
        """
        if not isinstance(v1, Vertice) or not isinstance(v2, Vertice):
            raise VerticeInvalidoError("Os vértices passados com parâmetro são inválidos.")
        self._v1 = v1
        self._v2 = v2
        self._rotulo = rotulo
        self._peso = peso

    @property
    def rotulo(self):
        """ str: O rótulo (ou nome) da aresta. """
        return self._rotulo

    @rotulo.setter
    def rotulo(self, novo_rotulo):
        self._rotulo = novo_rotulo

    @property
    def v1(self):
        """ Vertice: O primeiro vértice da aresta. """
        return self._v1

    @v1.setter
    def v1(self, v: Vertice):
        self._v1 = v

    @property
    def v2(self):
        """ Vertice: O segundo vértice da aresta. """
        return self._v2

    @v2.setter
    def v2(self, v: Vertice):
        self._v2 = v

    @property
    def peso(self):
        """ int: O peso da aresta. """
        return self._peso

    @peso.setter
    def peso(self, p):
        if type(p) == int or type(p) == float:
            self._peso = p
        else:
            raise TypeError("O peso deve ser um inteiro ou real.")

    def eh_ponta(self, v):
        """
        Verifica se um vértice passado como parâmetro é uma das pontas da aresta.
        Args:
            v: O vértice que se deseja verificar se é ponta da aresta.
        Returns:
            True se for ponta da aresta ou False, caso contrário.
        """
        return v == self._v1 or v == self._v2

    def __eq__(self, other):
        """
        É chamado quando se tenta usar o operador de igualdade entre uma Aresta e outro objeto.
        São comparados apenas os vértices de cada aresta.
        Args:
            other: O outro objeto que se deseja verificar a igualdade.
        Returns:
            True se os objetos forem iguais ou False, caso contrário.
        Raises:
            NotImplementedError: se `other` não for do tipo Aresta.
        """
        if not isinstance(other, Aresta):
            raise NotImplementedError("Não é possível comparar bibgrafo.Aresta com {}".format(other.__class__))
        return ((self._v1 == other.v1 and self._v2 == other.v2) or
                (self._v1 == other.v2 and self._v2 == other.v1))
    
    def __ne__(self, other):
        """
        É chamado quando se tenta usar o operador de desigualdade entre uma Aresta e outro objeto.
        São comparados apenas os vértices de cada aresta.
        Args:
            other: O outro objeto que se deseja verificar a desigualdade.
        Returns:
            True se os objetos forem diferentes ou False, caso contrário.
        Raises:
            NotImplementedError: se `other` não for do tipo Aresta.
        """
        return not (self == other)

    def __gt__(self, other):
        """
        É chamado quando se tenta usar o operador de maior que (`>`) entre uma Aresta e outro objeto.
        Nesta comparação, é avaliado apenas o peso das arestas.
        Args:
            other: O outro objeto que se deseja comparar.
        Returns:
            True se o peso de `self` for maior que o peso de `other` ou False, caso contrário.
        Raises:
            NotImplementedError: se `other` não for do tipo Aresta.
        """
        if not isinstance(other, Aresta):
            raise NotImplementedError("Não é possível comparar bibgrafo.Aresta com {}".format(other.__class__))
        return self.peso > other.peso

    def __ge__(self, other):
        """
        É chamado quando se tenta usar o operador de maior ou igual (`>=`) entre uma Aresta e outro objeto.
        Nesta comparação, é avaliado apenas o peso das arestas.
        Args:
            other: O outro objeto que se deseja comparar.
        Returns:
            True se o peso de `self` for maior ou igual que o peso de `other` ou False, caso contrário.
        Raises:
            NotImplementedError: se `other` não for do tipo Aresta.
        """
        if not isinstance(other, Aresta):
            raise NotImplementedError("Não é possível comparar bibgrafo.Aresta com {}".format(other.__class__))
        return self.peso >= other.peso

    def __lt__(self, other):
        """
        É chamado quando se tenta usar o operador de menor (`<`) entre uma Aresta e outro objeto.
        Nesta comparação, é avaliado apenas o peso das arestas.
        Args:
            other: O outro objeto que se deseja comparar.
        Returns:
            True se o peso de `self` for menor que o peso de `other` ou False, caso contrário.
        Raises:
            NotImplementedError: se `other` não for do tipo Aresta.
        """
        return not (self.peso > other.peso)

    def __le__(self, other):
        """
        É chamado quando se tenta usar o operador de menor ou igual (`<`) entre uma Aresta e outro objeto.
        Nesta comparação, é avaliado apenas o peso das arestas.
        Args:
            other: O outro objeto que se deseja comparar.
        Returns:
            True se o peso de `self` for menor ou igual que o peso de `other` ou False, caso contrário.
        Raises:
            NotImplementedError: se `other` não for do tipo Aresta.
        """
        return not (self.peso >= other.peso)

    def __str__(self):
        """
        Fornece uma representação em String de uma aresta
        """
        return "{}({}-{}), {}".format(self.rotulo, self.v1, self.v2, self.peso)


class ArestaDirecionada(Aresta):
    def __eq__(self, other):
        """
        É chamado quando se tenta usar o operador de igualdade entre uma ArestaDirecionada e outro objeto.
        São comparados apenas os vértices de cada aresta.
        Args:
            other: O outro objeto que se deseja verificar a igualdade.
        Returns:
            True se os objetos forem iguais ou False, caso contrário.
        """
        return self._v1 == other.v1 and self._v2 == other.v2

    def __str__(self):
        """
        Fornece uma representação em String de uma aresta
        """
        return "{}({}->{}), {}".format(self._rotulo, self._v1, self._v2, self._peso)
