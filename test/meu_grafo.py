from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.aresta import Aresta
from bibgrafo.grafo_errors import *
from sys import maxsize

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def getListaAdjacencias(self):
        '''
        Transforma o dicionário de Arestas em uma lista no seguinte formato:
        ['v1-v2', 'v3-v4', 'v5-v6', ...]
        ['A-B', 'A-C']
        :return: A lista de adjacências
        '''
        arestas = self._arestas.values()
        adjacencias = list()
        for a in arestas:
            adjacencias.append('{}-{}'.format(a.v1, a.v2))
        return adjacencias

    def vertices_nao_adjacentes(self):
        adjacencias = self.getListaAdjacencias()
        nao_adjacentes = set()
        for i in self._vertices:
            for j in self._vertices:
                aresta_indo = '{}-{}'.format(i, j)
                aresta_vindo = '{}-{}'.format(j, i)
                if i != j and aresta_indo not in adjacencias and aresta_vindo not in adjacencias and aresta_vindo not in nao_adjacentes:
                    nao_adjacentes.add(aresta_indo)
        return nao_adjacentes

    def ha_laco(self):
        adjacencias = self.getListaAdjacencias()
        for i in self._vertices:
            aresta = '{}-{}'.format(i, i)
            if aresta in adjacencias:
                return True
        return False

    def grau(self, v=''):

        vertice = self.get_vertice(v)

        if vertice not in self._vertices:
            raise VerticeInvalidoError('O vértice {} não existe no grafo'.format(v))

        grau = 0
        for aresta in self._arestas.values():
            if vertice == aresta.v1:
                grau += 1
            if vertice == aresta.v2:
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
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo'.format(V))
        arestas = set()
        for a in self._arestas.values():
            if a.v1.rotulo == V or a.v2.rotulo == V:
                arestas.add(a.rotulo)
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
            a = self._arestas[i]
            proximo_vertice = a.v2() if a.v1() == V else a.v1()
            if not arvore_dfs.existe_vertice(proximo_vertice):
                arvore_dfs.adiciona_vertice(proximo_vertice)
                arvore_dfs.adiciona_aresta(a.rotulo(), a.v1(), a.v2())
                self.dfs_rec(proximo_vertice, arvore_dfs)
        return arvore_dfs

    def vertice_oposto(self, a: Aresta, v):
        if self._arestas[a].v1() == v:
            return self._arestas[a].v2()
        return self._arestas[a].v1()

    def seleciona_proximo_v(self, temp, menor_caminho_v):
        menor = maxsize
        menor_v = ""
        for v in menor_caminho_v:
            if menor_caminho_v[v] < menor and temp[v]:
                menor = menor_caminho_v[v]
                menor_v = v
        return menor_v

    def dijkstra(self, vi, vf):
        menor_caminho_v = dict()
        temp = dict()
        predecessor = dict()
        carga_v = dict()
        for v in self._vertices:
            menor_caminho_v[v] = maxsize
            temp[v] = True
            predecessor[v] = ""

        menor_caminho_v[vi] = 0

        w = vi

        while w != vf:
            arestas = self.arestas_sobre_vertice(w)

            for a in arestas:
                v_oposto = self.vertice_oposto(a, w)
                if (menor_caminho_v[v_oposto] > menor_caminho_v[w] + self._arestas[a].peso()):
                    menor_caminho_v[v_oposto] = menor_caminho_v[w] + self._arestas[a].peso()
                    predecessor[v_oposto] = (w, a)

            temp[w] = False

            w = self.seleciona_proximo_v(temp, menor_caminho_v)

        caminho = list()
        caminho.append(vf)
        p = predecessor[vf]
        while True:
            caminho.insert(0, p[1])
            caminho.insert(0, p[0])
            p = predecessor[p[0]]
            if p[0] == vi:
                caminho.insert(0, p[1])
                caminho.insert(0, p[0])
                break
        return caminho



















