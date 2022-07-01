from bibgrafo.grafo_matriz_adj_nao_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def getListaAdjacencias(self):
        '''
        Transforma o dicionário de Arestas em uma lista no seguinte formato:
        ['v1-v2', 'v3-v4', 'v5-v6', ...]
        ['A-B', 'A-C']
        :return: A lista de adjacências
        '''
        arestas = self.A.values()
        adjacencias = list()
        for a in arestas:
            adjacencias.append('{}-{}'.format(a.get_v1(), a.get_v2()))
        return adjacencias

    def vertices_nao_adjacentes(self):
        nao_adjacentes = list()
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if i < j and not bool(self.M[i][j]):
                    nao_adjacentes.append('{}-{}'.format(self.N[i], self.N[j]))
        return nao_adjacentes

    def ha_laco(self):
        adjacencias = self.getListaAdjacencias()
        for i in self.N:
            aresta = '{}-{}'.format(i, i)
            if aresta in adjacencias:
                return True
        return False

    def grau(self, V=''):

        if V not in self.N:
            raise VerticeInvalidoException('O vértice {} não existe no grafo'.format(V))

        grau = 0
        for aresta in self.A.values():
            if V == aresta.get_v1():
                grau += 1
            if V == aresta.get_v2():
                grau += 1
        return grau

    def ha_paralelas(self):
        adj = self.getListaAdjacencias()
        for i in range(len(adj)):
            for j in range(len(adj)):
                if i != j and adj[i] == adj[j]:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        # Se o vértice não existir
        if V not in self.N:
            raise VerticeInvalidoException('O vértice {} não existe no grafo'.format(V))
        arestas = list()
        v = self.N.index(V)
        for i in range(len(self.M)):
            if bool(self.M[v][i]) and self.M[v][i] != "-":
                for k in self.M[v][i]:
                    arestas.append(k)
            if bool(self.M[i][v]) and self.M[i][v] != "-":
                for l in self.M[i][v]:
                    arestas.append(l)
        return arestas

    def eh_laco(self, adj=''):
        v1, v2 = adj.split('-')
        return v1 == v2

    def eh_completo(self):
        # Primeiro tem que verificar se é simples
        if self.ha_laco() or self.ha_paralelas():
            return False

        # Se for simples
        vert_nao_adj = self.vertices_nao_adjacentes()
        for i in vert_nao_adj:
            if not self.eh_laco(i):
                return False

        return True

    def dfs(self, raiz=''):
        arvore_dfs = MeuGrafo()
        arvore_dfs.adiciona_vertice(raiz)
        return self.dfs_rec(raiz, arvore_dfs)

    def dfs_rec(self, V, arvore_dfs):
        adj = list(self.arestas_sobre_vertice(V))
        adj.sort()
        for i in adj:
            a = self.A[i]
            proximo_vertice = a.get_v2() if a.get_v1() == V else a.get_v1()
            if not arvore_dfs.existe_vertice(proximo_vertice):
                arvore_dfs.adiciona_vertice(proximo_vertice)
                arvore_dfs.adiciona_aresta(a.get_rotulo(), a.get_v1(), a.get_v2())
                self.dfs_rec(proximo_vertice, arvore_dfs)
        return arvore_dfs
