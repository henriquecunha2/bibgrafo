from bibgrafo.grafo import GrafoIF
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from multipledispatch import dispatch
from copy import deepcopy

class GrafoMatrizAdjacenciaNaoDirecionado(GrafoIF):

    N: list
    M: list

    def __init__(self, N=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if N == None:
            N = list()
        if M == None:
            M = list()

        for v in N:
            if not(GrafoMatrizAdjacenciaNaoDirecionado.vertice_valido(v)):
                raise VerticeInvalidoError('O vértice ' + v + ' é inválido')

        self.N = deepcopy(N)

        if M == []:
            self.M = list()
            for k in range(len(N)):
                self.M.append(list())
                for l in range(len(N)):
                    self.M[k].append(dict())

        if len(self.M) != len(N):
            raise MatrizInvalidaError('A matriz passada como parâmetro não tem o mesmo tamanho da quantidade de vértices')

        for c in self.M:
            if len(c) != len(N):
                raise MatrizInvalidaError('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                '''
                Verifica se cada elemento da matriz é um dicionário de arestas válidas
                '''
                if type(self.M[i][j]) is not dict:
                    raise MatrizInvalidaError("Algum elemento da matriz não é um dicionário de arestas")
                else:
                    dicio_aresta = self.M[i][j]
                for k in dicio_aresta.values():
                    aresta = Aresta(k, dicio_aresta[k].get_v1(), dicio_aresta[k].get_v2())
                    if not(self.aresta_valida(aresta)):
                        raise ArestaInvalidaError('A aresta ' + aresta + ' é inválida')

                if i != j and self.M[i][j] != self.M[j][i]:
                    raise MatrizInvalidaError('A matriz não representa uma matriz de grafo não direcionado')

    def aresta_valida(self, aresta: Aresta):
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

    @classmethod
    def vertice_valido(cls, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return isinstance(vertice, Vertice)

    def existe_vertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return GrafoMatrizAdjacenciaNaoDirecionado.vertice_valido(vertice) and vertice in self.N

    def indice_do_vertice(self, v: Vertice):
        '''
        Dado um vértice retorna o índice do vértice a na lista de vértices
        :param v: O vértice a ser analisado
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(v)

    def existe_aresta(self, a: Aresta) -> bool:
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        if GrafoMatrizAdjacenciaNaoDirecionado.aresta_valida(self, a):
            if a.get_rotulo() in self.M[self.indice_do_vertice(a.get_v1())][self.indice_do_vertice(a.get_v2())]:
                return True
        else:
            raise ArestaInvalidaError("A aresta passada como parâmetro é inválida.")
        return False

    def existe_rotulo_aresta(self, aresta: str) -> bool:
        """
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        """
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if self.M[i][j].get(aresta) is not None:
                    return True
        return False

    def existe_rotulo_vertice(self, r: str):
        """
        TODO Fazer o docstring
        """
        return self.get_vertice(r) is not None

    @dispatch(str)
    def adiciona_vertice(self, rotulo: str):
        """
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        """
        if self.existe_rotulo_vertice(rotulo):
            raise VerticeInvalidoError('O vértice {} já existe'.format(rotulo))

        if rotulo != "":

            v = Vertice(rotulo)
            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            i_v = self.indice_do_vertice(v)

            for k in range(len(self.N)):
                self.M[k].append(dict())  # adiciona os elementos da coluna do vértice
                self.M[i_v].append(dict())  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoError('O vértice ' + rotulo + ' é inválido')

    @dispatch(Vertice)
    def adiciona_vertice(self, v: Vertice):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if GrafoMatrizAdjacenciaNaoDirecionado.existe_vertice(v):
            raise VerticeInvalidoError('O vértice {} já existe'.format(v))

        if self.vertice_valido(v):

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            i_v = self.indice_do_vertice(v)

            for k in range(len(self.N)):
                self.M[k].append(dict()) # adiciona os elementos da coluna do vértice
                self.M[i_v].append(dict())  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoError('O vértice ' + v + ' é inválido')

    def remove_vertice(self, rotulo: str):
        '''
        Remove um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser removido do grafo.
        :return True se o vértice foi removido com sucesso.
        :raises VerticeInvalidoException se o vértice não for encontrado no grafo
        '''
        if not self.existe_rotulo_vertice(rotulo):
            raise VerticeInvalidoError("O vértice passado como parâmetro não existe no grafo.")

        v = self.get_vertice(rotulo)

        v_i = self.indice_do_vertice(v)

        self.M.pop(v_i)

        for i in range(len(self.M)):
            self.M[i].pop(v_i)

        self.N.remove(v)
        return True

    def get_vertice(self, r: str):
        """
        Retorna o objeto do tipo vértice que tem como rótulo o parâmetro passado.
        :param r: O rótulo do vértice a ser retornado
        :return: Um objeto do tipo vértice que tem como rótulo o parâmetro passado ou False se o vértice não
        for encontrado.
        """
        for i in self.N:
            if r == i.get_rotulo():
                return i

    @dispatch(Aresta)
    def adiciona_aresta(self, a: Aresta):
        '''
        Adiciona uma aresta ao grafo
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.existe_aresta(a):
            raise ArestaInvalidaError('A aresta {} já existe no Grafo'.format(a))

        if self.aresta_valida(a):
            i_a1 = self.indice_do_vertice(a.get_v1())
            i_a2 = self.indice_do_vertice(a.get_v2())
            self.M[i_a1][i_a2][a.get_rotulo()] = a
            self.M[i_a2][i_a1][a.get_rotulo()] = a
        else:
            raise ArestaInvalidaError('A aresta {} é inválida'.format(a))

        return True

    @dispatch(str, str, str, int)
    def adiciona_aresta(self, rotulo='', v1='', v2='', peso=1):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''


        a = Aresta(rotulo, self.get_vertice(v1), self.get_vertice(v2), peso)
        return self.adiciona_aresta(a)

    @dispatch(str, str, str)
    def adiciona_aresta(self, rotulo='', v1='', v2=''):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''

        a = Aresta(rotulo, self.get_vertice(v1), self.get_vertice(v2), 1) # Quando o peso não é informado, atribui-se peso 1
        return self.adiciona_aresta(a)

    def remove_aresta(self, r: str, v1=None, v2=None):
        '''
        Remove uma aresta do grafo. Os parâmetros v1 e v2 são opcionais e servem para acelerar a busca pela aresta de
        interesse.
        Se for passado apenas o parâmetro r, deverá ocorrer uma busca por toda a matriz.
        :param r: O rótulo da aresta a ser removida
        :param v1: O vértice 1 da aresta a ser removida
        :param v2: O vértice 2 da aresta a ser removida
        :raise: lança uma exceção caso a aresta não exista no grafo ou caso algum dos vértices passados não existam
        :return: Retorna True se a aresta foi removida com sucesso.
        '''

        def remove_com_indices(r, v1_i, v2_i):
            '''
            Função interna apenas para remover do dicionário de arestas, quando há índices conhecidos
            '''
            arestas_top = self.M[v1_i][v2_i]
            arestas_bottom = self.M[v2_i][v1_i]

            if arestas_top.get(r) is not None:
                arestas_top.pop(r)

            if arestas_bottom.get(r) is not None:
                arestas_bottom.pop(r)

        def percorre_e_remove(M, i):
            '''
            Função interna apenas para remover do dicionário de arestas, quando NÃO há índices conhecidos
            '''
            # linha
            for j in range(0, len(M)):
                arestas_percorrer = M[i][j]
                if arestas_percorrer.get(r) is not None:
                    arestas_percorrer.pop(r)
                    break
            #coluna
            for j in range(0, len(M)):
                arestas_percorrer = M[j][i]
                if arestas_percorrer.get(r) is not None:
                    arestas_percorrer.pop(r)

        if not self.existe_rotulo_aresta(r):
            raise ArestaInvalidaError("A aresta não existe no grafo.")

        if v1 == None:
            if v2 == None:
                for i in range(len(self.M)):
                    for j in range(len(self.M)):
                        remove_com_indices(r, i, j)

            elif self.existe_vertice(v2):
                v2_i = self.indice_do_vertice(self.get_vertice(v2))
                return percorre_e_remove(self.M, v2_i)
            elif not self.existe_vertice(self.get_vertice(v2)):
                raise VerticeInvalidoError("O vértice {} é inválido!".format(v2))

        else:
            if self.existe_rotulo_vertice(v1):
                v1_i = self.indice_do_vertice(self.get_vertice(v1))
                if self.existe_vertice(v2):
                    v2_i = self.indice_do_vertice(self.get_vertice(v2))
                    remove_com_indices(r, v1_i, v2_i)
                else:
                    return percorre_e_remove(self.M, v1_i)
            else:
                raise VerticeInvalidoError("O vértice {} é inválido!".format(v1))


    def __eq__(self, other):
        '''
        Define a igualdade entre a instância do GrafoListaAdjacencia para o qual essa função foi chamada e a instância de um GrafoListaAdjacencia passado como parâmetro.
        :param other: O grafo que deve ser comparado com este grafo.
        :return: Um valor booleano caso os grafos sejam iguais.
        '''
        if len(self.M) != len(other.M) or len(self.N) != len(other.N):
            return False
        for n in self.N:
            if not other.existe_vertice(n):
                return False
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[i][j]) != len(other.M[i][j]):
                    return False
                for k in self.M[i][j]:
                    if k not in other.M[i][j]:
                        return False
        return True

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        grafo_str = '  '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                if self.M[l][c] == '-':
                    grafo_str += str(self.M[l][c]) + ' '
                else:
                    if bool(self.M[l][c]):
                        grafo_str += '*' + ' '
                    else:
                        grafo_str += 'o' + ' '
            grafo_str += '\n'

        for l in range(len(self.N)):
            for c in range(len(self.N)):
                if bool(self.M[l][c]) and l > c:
                    grafo_str += self.N[l] + '-' + self.N[c] + ': '
                    for k in self.M[l][c]:
                        grafo_str += k + ' | '
                    grafo_str += '\n'

        return grafo_str