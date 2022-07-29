from bibgrafo.grafo import GrafoIF
from bibgrafo.aresta import Aresta
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class GrafoListaAdjacencia(GrafoIF):

    def __init__(self, N=None, A=None):
        '''
        Constrói um objeto do tipo GrafoListaAdjacencia. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        Nessa implementação o Grafo é representado por uma lista de adjacências.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param A: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma tupla que contém dois os 2 vértices da aresta.
        '''

        if N == None:
            N = list()
        else:
            for v in N:
                if not(GrafoListaAdjacencia.vertice_valido(v)):
                    raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
        self.N = deepcopy(N)

        if A == None:
            A = dict()
        else:
            for a in A:
                if not(self.aresta_valida(A[a])):
                    raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = deepcopy(A)

    @classmethod
    def vertice_valido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != ''

    def existe_vertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return GrafoListaAdjacencia.vertice_valido(vertice) and vertice in self.N

    def adiciona_vertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.vertice_valido(v) and not self.existe_vertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido ou já existe no grafo')

    def remove_vertice(self, v):
        '''
        Remove um vértice passado como parâmetro e remove em cascata as arestas que estão conectadas a esse vértice.
        :param v: O vértice a ser removido.
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser removido.
        '''
        newA = dict()
        if self.existe_vertice(v):
            self.N.remove(v)
            for a in self.A.keys():
                if not(self.A[a].eh_ponta(v)):
                    newA[a] = self.A[a]
            self.A = newA
        else:
            raise VerticeInvalidoException('O vértice {} não existe no grafo.'.format(v))

    def existe_rotulo_aresta(self, r=''):
        '''
        Verifica se um rótulo de aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se o rótulo da aresta existe no grafo.
        '''
        return r in self.A

    def get_aresta(self, r):
        '''
        Retorna uma cópia da aresta que tem o rótulo passado como parâmetro
        :param r: O rótulo da aresta solicitada
        :return: Um objeto do tipo Aresta que é a aresta requisitada ou False se a aresta não existe
        '''
        if self.existe_rotulo_aresta(r):
            return deepcopy(self.A[r])
        return False
    
    def aresta_valida(self, aresta=Aresta()):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Verifica se os vértices existem no Grafo
        if type(aresta) == Aresta and self.existe_vertice(aresta.get_v1()) and self.existe_vertice(aresta.get_v2()):
            return True
        return False

    def adiciona_aresta(self, rotulo='', v1='', v2='', peso=1):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        :returns: True se a aresta foi adicionada com sucesso
        '''
        a = Aresta(rotulo, v1, v2, peso)
        if self.aresta_valida(a):
            if rotulo not in self.A: # Verifica se a aresta já existe no grafo
                self.A[rotulo] = a
            else:
                raise ArestaInvalidaException('A aresta {} não pode ter o mesmo rótulo de uma aresta já existente no grafo'.format(str(a)))
        else:
            raise ArestaInvalidaException('A aresta ' + str(a) + ' é inválida')
        return True

    def remove_aresta(self, r):
        '''
        Remove uma aresta a partir de seu rótulo
        :param r: O rótulo da aresta a ser removida
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser removida
        '''
        if self.existe_rotulo_aresta(r):
            self.A.pop(r)
        else:
            raise ArestaInvalidaException('A aresta {} não existe no grafo'.format(r))

    def __eq__(self, other):
        '''
        Define a igualdade entre a instância do GrafoListaAdjacencia para o qual essa função foi chamada e a instância de um GrafoListaAdjacencia passado como parâmetro.
        :param other: O grafo que deve ser comparado com este grafo.
        :return: Um valor booleano caso os grafos sejam iguais.
        '''
        if len(self.A) != len(other.A) or len(self.N) != len(other.N):
            return False
        for n in self.N:
            if not other.existe_vertice(n):
                return False
        for a in self.A:
            if not self.existe_rotulo_aresta(a) or not other.existe_rotulo_aresta(a):
                return False
            if not self.A[a] == other.get_aresta(a):
                return False
        return True

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo.
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += str(self.A[a]) + '\n'

        return grafo_str































