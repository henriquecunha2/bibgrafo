from functools import singledispatchmethod
from typing import Union, List
from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        # $ n \cdot \log n * (m + 2) $

        vertices_nao_adj = set()
        def aresta_tem_par(v1: Vertice, v2: Vertice) -> bool:
            a: Aresta
            for a in self.arestas.values():
                if a.eh_ponta(v1) and a.eh_ponta(v2): return True
            return False

        i = 0
        while i < len(self.vertices):
            for v1 in range(i, len(self.vertices)):
                for v2 in range(v1 + 1, len(self.vertices)):
                    eh_adjacente = aresta_tem_par(self.vertices[v1], self.vertices[v2])
                    if not eh_adjacente:
                        vertices_nao_adj.add("%s-%s" % (self.vertices[v1].rotulo, self.vertices[v2].rotulo))
            i += 1

        return vertices_nao_adj


    def ha_laco(self) -> bool:
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        aresta: Aresta
        for aresta in self.arestas.values():
            if aresta.v1 == aresta.v2: return True
        return False


    def grau(self, V='') -> int:
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice %s não existe no grafo." % (V))
        a: Aresta
        grau = 0
        for a in self.arestas.values():
            if V == a.v1.rotulo: grau += 1
            if V == a.v2.rotulo: grau += 1

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        def aresta_paralela (a1: Aresta, a2: Aresta):
            if a1.v1 in [a2.v1, a2.v2] and a1.v2 in [a2.v1, a2.v2]:
                return True
            return False

        i = 0
        arestas = list(self.arestas.values())
        while i < len(arestas):
            for a1 in range(i, len(arestas)):
                for a2 in range(a1 + 1, len(arestas)):
                    if aresta_paralela(arestas[a1], arestas[a2]): return True

            return False

    def arestas_sobre_vertice(self, V=''):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista_arestas = set()
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice %s não existe no grafo" % (V))
        a: Aresta
        for a in self.arestas.values():
            if V in [a.v1.rotulo, a.v2.rotulo]: lista_arestas.add(a.rotulo)
        return lista_arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas(): return False

        return len(self.vertices_nao_adjacentes()) == 0

    def bfs(self, raiz=''):
        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(raiz)

        def bfs_rec(V: str, arvore_bfs: MeuGrafo):
            adj = list(self.arestas_sobre_vertice(V))
            adj = sorted(adj)
            vertices_adj = []
            for i in adj:
                a: Aresta = self._arestas[i]
                proximo_vertice = a.v2 if a.v1.rotulo == V else a.v1
                if not arvore_bfs.existe_rotulo_vertice(proximo_vertice.rotulo):
                    vertices_adj.append(proximo_vertice)
                    arvore_bfs.adiciona_vertice(proximo_vertice.rotulo)
                    arvore_bfs.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
            for v in vertices_adj: bfs_rec(v.rotulo, arvore_bfs)
            return arvore_bfs

        return bfs_rec(raiz, arvore_bfs)

    def dfs(self, raiz=''):
        arvore_dfs = MeuGrafo()
        arvore_dfs.adiciona_vertice(raiz)

        def dfs_rec(V: str, arvore_dfs: MeuGrafo):
            adj = list(self.arestas_sobre_vertice(V))
            adj = sorted(adj)
            for i in adj:
                a: Aresta = self._arestas[i]
                proximo_vertice = a.v2 if a.v1.rotulo == V else a.v1
                if not arvore_dfs.existe_rotulo_vertice(proximo_vertice.rotulo):
                    arvore_dfs.adiciona_vertice(proximo_vertice.rotulo)
                    arvore_dfs.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
                    dfs_rec(proximo_vertice.rotulo, arvore_dfs)
            return arvore_dfs

        return dfs_rec(raiz, arvore_dfs)

    def caminho(self, n: int) -> list:

        def dfs_caminho(V, lista_v, lista_a) -> None:
            adj = list(self.arestas_sobre_vertice(V))
            adj = sorted(adj)
            vertices_adj = []
            for i in adj:
                a: Aresta = self._arestas[i]
                if a.rotulo in lista_a: continue
                proximo_vertice = a.v2 if a.v1.rotulo == V else a.v1
                if proximo_vertice.rotulo in lista_v: continue
                else:
                    caminho_vertices.append(proximo_vertice.rotulo)
                    caminho_arestas.append(a.rotulo)
                    dfs_caminho(proximo_vertice.rotulo, lista_v, lista_a)
                    break

        for v in self._vertices:
            caminho_vertices = []
            caminho_vertices.append(v.rotulo)
            caminho_arestas = []
            dfs_caminho(v.rotulo, caminho_vertices, caminho_arestas)
            if len(caminho_arestas) >= n:
                caminho_n = []
                caminho_n.append(caminho_vertices[0])
                for i in range(n):
                    caminho_n.append(caminho_arestas[i])
                    caminho_n.append(caminho_vertices[i + 1])
                return caminho_n

        return []

    def ha_caminho(self, src: str, dest: str) -> list:

        def dfs_ab(src: str, dest: str, dict_vertices: dict, dict_arestas: dict,
            lista_vertices: list, lista_arestas: list) -> bool:
            adj = list(self.arestas_sobre_vertice(src))
            adj = sorted(adj)
            for i in adj:
                a: Aresta = self._arestas[i]
                if a.rotulo in lista_arestas: continue
                proximo_vertice = a.v2 if a.v1.rotulo == src else a.v1
                if proximo_vertice.rotulo == dest:
                    dict_arestas[src] = a.rotulo
                    dict_vertices[src] = proximo_vertice.rotulo
                    return True
                elif proximo_vertice.rotulo not in lista_vertices:
                    lista_vertices.append(proximo_vertice.rotulo)
                    lista_arestas.append(a.rotulo)
                    dict_arestas[src] = a.rotulo
                    dict_vertices[src] = proximo_vertice.rotulo
                    if dfs_ab(proximo_vertice.rotulo, dest,
                        dict_vertices, dict_arestas, lista_vertices, lista_arestas): return True
            return False


        lista_arestas = {}
        lista_vertices = {}
        vertices_percorridos = []
        arestas_percorridas = []
        for v in self._vertices:
            lista_vertices[v.rotulo] = ""
            lista_arestas[v.rotulo] = ""
        dest_encontrado = dfs_ab(src, dest, lista_vertices,
        lista_arestas, vertices_percorridos, arestas_percorridas)
        if dest_encontrado:
            caminho = [src]
            caminho.append(lista_arestas[src])
            caminho.append(lista_vertices[src])
            prox_vertice = lista_vertices[src]
            while not prox_vertice == dest:
                caminho.append(lista_arestas[prox_vertice])
                caminho.append(lista_vertices[prox_vertice])
                prox_vertice = lista_vertices[prox_vertice]
            return caminho
        else: return False

    def conexo(self):
        for v1 in range(len(self._vertices)):
            for v2 in range(v1 + 1, len(self._vertices)):
                caminho = self.ha_caminho(self._vertices[v1].rotulo, self._vertices[v2].rotulo)
                if not caminho:
                    return False
        return True

    def dijkstra(self, src: str, dest: str):

        def sort(list_v, dict_v):
            for v1 in range(len(list_v)):
                for v2 in range(v1, len(list_v)):
                    if dict_v[list_v[v2]] < dict_v[list_v[v1]]:
                        temp = list_v[v2]
                        list_v[v2] = list_v[v1]
                        list_v[v1] = temp

        def bfs_dijkstra(src: str, dest: str, dict_v: dict, dict_a: dict, dict_w: dict, list_v: list, list_a: list):
            adj = self.arestas_sobre_vertice(src)
            adj = sorted(adj)
            vertices_adj = []
            for i in adj:
                a: Aresta
                a = self._arestas[i]
                if a.rotulo in list_a: continue
                proximo_vertice = a.v2 if a.v1.rotulo == src else a.v1
                if proximo_vertice.rotulo in list_v: continue
                vertices_adj.append(proximo_vertice.rotulo)
                novo_peso = dict_w[src] + a.peso
                if novo_peso < dict_w[proximo_vertice.rotulo] or dict_w[proximo_vertice.rotulo] < 0:
                    dict_v[proximo_vertice.rotulo] = src
                    dict_a[proximo_vertice.rotulo] = a.rotulo
                    dict_w[proximo_vertice.rotulo] = novo_peso
            list_v.append(src)
            sort(vertices_adj, dict_w)
            for vertice in vertices_adj:
                if vertice == dest: return True
                # elif vertice in list_v: pass
                elif bfs_dijkstra(vertice, dest, dict_v, dict_a, dict_w, list_v, list_a): return True

        dict_v = {}
        dict_a = {}
        dict_w = {}
        list_v = []
        list_a = []
        for v in self._vertices:
            dict_v[v.rotulo] = ""
            dict_a[v.rotulo] = ""
            if v.rotulo == src: dict_w[v.rotulo] = 0
            else: dict_w[v.rotulo] = -1
        caminho_encontrado = bfs_dijkstra(src, dest, dict_v, dict_a, dict_w, list_v, list_a)
        if caminho_encontrado:
            caminho = []
            prox_vertice = dest
            caminho.append(dict_v[prox_vertice])
            caminho.append(dict_a[prox_vertice])
            caminho.append(dest)
            prox_vertice = dict_v[dest]
            while not prox_vertice == src:
                caminho.insert(0,dict_a[prox_vertice])
                caminho.insert(0,dict_v[prox_vertice])
                prox_vertice = dict_v[prox_vertice]
            return caminho
        else: return False
