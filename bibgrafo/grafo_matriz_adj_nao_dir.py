from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from multipledispatch import dispatch
from copy import deepcopy


class GrafoMatrizAdjacenciaNaoDirecionado(GrafoMatrizAdjacenciaDirecionado):

    N: list
    M: list

    def __init__(self, N=None, M=None):
        """
        Constrói um objeto do tipo grafo não direcionado com matriz de adjacência.
        Se nenhum parâmetro for passado, cria um grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param M: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um
        dicionário de arestas (objetos do tipo Aresta) para que seja possível representar arestas paralelas
        e que cada aresta tenha seus próprios atributos distintos. Como a matriz é não direcionada, os elementos
        abaixo da diagonal principal são espelhados em relação aos elementos acima da diagonal principal.
        """

        if N is None:
            N = list()
        if M is None:
            M = list()

        for v in N:
            if not(GrafoMatrizAdjacenciaNaoDirecionado.vertice_valido(v)):
                raise VerticeInvalidoError('O vértice ' + v + ' é inválido')

        self.N = deepcopy(N)

        if not M:
            self.M = list()
            for k in range(len(N)):
                self.M.append(list())
                for m in range(len(N)):
                    self.M[k].append(dict())

        if len(self.M) != len(N):
            raise MatrizInvalidaError('A matriz passada como parâmetro não tem o mesmo tamanho da quantidade de'
                                      'vértices')

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
                        raise ArestaInvalidaError('A aresta ' + str(aresta) + ' é inválida')

                if i != j and self.M[i][j] != self.M[j][i]:
                    raise MatrizInvalidaError('A matriz não representa uma matriz de grafo não direcionado')

    @dispatch(str)
    def adiciona_vertice(self, rotulo: str):
        """
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param rotulo: O vértice a ser incluído no grafo.
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
        """
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        """
        if GrafoMatrizAdjacenciaNaoDirecionado.existe_vertice(v):
            raise VerticeInvalidoError('O vértice {} já existe'.format(v))

        if self.vertice_valido(v):

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            i_v = self.indice_do_vertice(v)

            for k in range(len(self.N)):
                self.M[k].append(dict())  # adiciona os elementos da coluna do vértice
                self.M[i_v].append(dict())  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoError('O vértice ' + str(v) + ' é inválido')

    def existe_aresta(self, aresta: Aresta) -> bool:
        """
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        """
        if GrafoMatrizAdjacenciaNaoDirecionado.aresta_valida(self, aresta):
            if aresta.get_rotulo() in self.M[self.indice_do_vertice(aresta.get_v1())][self.indice_do_vertice(aresta.get_v2())]:
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

    def aresta_valida(self, aresta: Aresta):
        """
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        """

        # Verifica se os vértices existem no Grafo
        if type(aresta) == Aresta and self.existe_vertice(aresta.get_v1()) and self.existe_vertice(aresta.get_v2()):
            return True
        return False

    @dispatch(Aresta)
    def adiciona_aresta(self, a: Aresta):
        """
        Adiciona uma aresta ao grafo
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        """
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
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str, peso=1):
        """
        Adiciona uma aresta ao grafo
        :param rotulo: O rótulo da aresta
        :param v1: O primeiro vértice da aresta
        :param v2: O segundo vértice da aresta
        :param peso: O peso da aresta
        :raise: Lança ArestaInvalidaError caso a aresta não estiver em um formato válido
        """
        a = Aresta(rotulo, self.get_vertice(v1), self.get_vertice(v2), peso)
        return self.adiciona_aresta(a)

    @dispatch(str, str, str)
    def adiciona_aresta(self, rotulo: str, v1: str, v2: str):
        """
        Adiciona uma aresta ao grafo
        :param rotulo: O rótulo da aresta
        :param v1: O primeiro vértice da aresta
        :param v2: O segundo vértice da aresta
        :raise: Lança ArestaInvalidaError caso a aresta não estiver em um formato válido
        """

        # Quando o peso não é informado, atribui-se peso 1
        a = Aresta(rotulo, self.get_vertice(v1), self.get_vertice(v2), 1)
        return self.adiciona_aresta(a)

    def remove_aresta(self, r: str, v1=None, v2=None):
        """
        Remove uma aresta do grafo. Os parâmetros v1 e v2 são opcionais e servem para acelerar a busca pela aresta de
        interesse.
        Se for passado apenas o parâmetro r, deverá ocorrer uma busca por toda a matriz.
        :param r: O rótulo da aresta a ser removida
        :param v1: O vértice 1 da aresta a ser removida
        :param v2: O vértice 2 da aresta a ser removida
        :raise: lança uma exceção caso a aresta não exista no grafo ou caso algum dos vértices passados não existam
        :return: Retorna True se a aresta foi removida com sucesso.
        """

        def remove_com_indices(rotulo, v1_ind, v2_ind):
            """
            Função interna apenas para remover do dicionário de arestas, quando há índices conhecidos
            """
            arestas_top = self.M[v1_ind][v2_ind]
            arestas_bottom = self.M[v2_ind][v1_ind]

            if arestas_top.get(rotulo) is not None:
                arestas_top.pop(rotulo)

            if arestas_bottom.get(rotulo) is not None:
                arestas_bottom.pop(rotulo)

        def percorre_e_remove(M, ind):
            """
            Função interna apenas para remover do dicionário de arestas, quando NÃO há índices conhecidos
            """
            # linha
            for x in range(0, len(M)):
                arestas_percorrer = M[ind][x]
                if arestas_percorrer.get(r) is not None:
                    arestas_percorrer.pop(r)
                    break
            # coluna
            for x in range(0, len(M)):
                arestas_percorrer = M[x][ind]
                if arestas_percorrer.get(r) is not None:
                    arestas_percorrer.pop(r)

        if not self.existe_rotulo_aresta(r):
            raise ArestaInvalidaError("A aresta não existe no grafo.")

        if v1 is None:
            if v2 is None:
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
        """
        Define a igualdade entre a instância do grafo para o qual essa função foi chamada e a instância de um
        GrafoMatrizAdjacenciaNaoDirecionado passado como parâmetro.
        :param other: O grafo que deve ser comparado com este grafo.
        :return: Um valor booleano caso os grafos sejam iguais.
        """
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
        """
        Fornece uma representação do tipo String do grafo.
        :return: Uma string que representa o grafo
        """

        grafo_str = '  '

        for v in range(len(self.N)):
            grafo_str += str(self.N[v])
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for m in range(len(self.M)):
            grafo_str += str(self.N[m]) + ' '
            for c in range(len(self.M)):
                if self.M[m][c] == '-':
                    grafo_str += str(self.M[m][c]) + ' '
                else:
                    if bool(self.M[m][c]):
                        grafo_str += '*' + ' '
                    else:
                        grafo_str += 'o' + ' '
            grafo_str += '\n'

        for m in range(len(self.N)):
            for c in range(len(self.N)):
                if bool(self.M[m][c]) and m > c:
                    grafo_str += str(self.N[m]) + '-' + str(self.N[c]) + ': '
                    for k in self.M[m][c]:
                        grafo_str += k + ' | '
                    grafo_str += '\n'

        return grafo_str
