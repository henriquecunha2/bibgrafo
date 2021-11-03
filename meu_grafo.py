from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

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
            adjacencias.append('{}-{}'.format(a.getV1(), a.getV2()))
        return adjacencias

    def vertices_nao_adjacentes(self):
        adjacencias = self.getListaAdjacencias()
        nao_adjacentes = set()
        for i in self.N:
            for j in self.N:
                aresta_indo = '{}-{}'.format(i, j)
                aresta_vindo = '{}-{}'.format(j, i)
                if i != j and aresta_indo not in adjacencias and aresta_vindo not in adjacencias and aresta_vindo not in nao_adjacentes:
                    nao_adjacentes.add(aresta_indo)
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
            if V == aresta.getV1():
                grau += 1
            if V == aresta.getV2():
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
        arestas = set()
        for a in self.A.values():
            if a.getV1() == V or a.getV2() == V:
                arestas.add(a.getRotulo())
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

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass