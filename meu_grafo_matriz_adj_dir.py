from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        nao_adjacentes = list()
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if i != j and not bool(self.M[i][j]):
                    nao_adjacentes.append('{}-{}'.format(self.N[i], self.N[j]))
        return nao_adjacentes

    def ha_laco(self):
        for i in range(len(self.M)):
            if bool(self.M[i][i]):
                return True
        return False

    def grau(self, V=''):

        if V not in self.N:
            raise VerticeInvalidoException('O vértice {} não existe no grafo'.format(V))

        grau = 0
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for k in self.M[i][j].values():
                    if k.getV1() == V:
                        grau += 1
                    if k.getV2() == V:
                        grau += 1
        return grau

    def ha_paralelas(self):
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        # Se o vértice não existir
        if V not in self.N:
            raise VerticeInvalidoException('O vértice {} não existe no grafo'.format(V))
        arestas = list()
        v = self.N.index(V)
        for i in range(len(self.M)):
            if bool(self.M[i][v]):
                for k in self.M[i][v]:
                    arestas.append(k)
            if i != v and bool(self.M[v][i]):
                for k in self.M[v][i]:
                    arestas.append(k)
        return arestas

    def eh_completo(self):
        # Primeiro tem que verificar se é simples
        if self.ha_laco() or self.ha_paralelas():
            return False

        # Se for simples
        vert_nao_adj = self.vertices_nao_adjacentes()
        if vert_nao_adj == []:
            return True
        return False

    def dfs(self, raiz=''):
        arvore_dfs = MeuGrafo()
        arvore_dfs.adicionaVertice(raiz)
        return self.dfs_rec(raiz, arvore_dfs)

    def dfs_rec(self, V, arvore_dfs):
        adj = list(self.arestas_sobre_vertice(V))
        adj.sort()
        for i in adj:
            a = self.A[i]
            proximo_vertice = a.getV2() if a.getV1() == V else a.getV1()
            if not arvore_dfs.existeVertice(proximo_vertice):
                arvore_dfs.adicionaVertice(proximo_vertice)
                arvore_dfs.adicionaAresta(a.getRotulo(), a.getV1(), a.getV2())
                self.dfs_rec(proximo_vertice, arvore_dfs)
        return arvore_dfs
