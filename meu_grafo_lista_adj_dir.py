from bibgrafo.grafo_lista_adjacencia_dir import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import ArestaDirecionada
from bibgrafo.vertice import Vertice

class MeuGrafo(GrafoListaAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self) -> set:
        vertices_nao_adj = set()

        def aresta_tem_par(v1: Vertice, v2: Vertice) -> bool:
            for a in self.arestas.values():
                if a.eh_ponta(v1) and a.eh_ponta(v2): return True
            return False

        i = 0
        while i < len(self._vertices):
            for v1 in range(len(self._vertices)):
                for v2 in range(v1 + 1, len(self.vertices)):
                    eh_adjacente = aresta_tem_par(self.vertices[v1], self.vertices[v2])
                    if not eh_adjacente:
                        vertices_nao_adj.add("{}-{}".format(self.vertices[v1].rotulo, self.vertices[v2].rotulo))
            i += 1

        return vertices_nao_adj

    def ha_laco(self) -> bool:
        a: ArestaDirecionada
        for a in self.arestas.values():
            if a.v1 == a.v2: return True
        return False

    def grau_saida(self, V:str) -> int:
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo'.format(V))
        a: ArestaDirecionada
        grau = 0
        for a in self.arestas.values():
            if a.v1.rotulo == V: grau += 1
        return grau

    def grau_entrada(self, V:str) -> int:
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo'.format(V))
        a: ArestaDirecionada
        grau = 0
        for a in self.arestas.values():
            if a.v2.rotulo == V: grau += 1
        return grau

    def ha_paralelas(self) -> bool:
        def aresta_paralela(a1: ArestaDirecionada, a2: ArestaDirecionada):
            if a1.v1 == a2.v1 and a1.v2 == a2.v2: return True
            return False

        i = 0
        arestas = list(self.arestas.values())
        while i < len(arestas):
            for a1 in range(len(arestas)):
                for a2 in range(a1 + 1, len(arestas)):
                    if aresta_paralela(arestas[a1], arestas[a2]): return True
            i += 1

        return False

    def arestas_sobre_vertice(self, V: str='') -> set:
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo'.format(V))

        arestas = set()
        a: ArestaDirecionada
        for a in self.arestas.values():
            if V in [a.v1.rotulo, a.v2.rotulo]: arestas.add(a.rotulo)

        return arestas

    def eh_completo(self) -> bool:
        if self.ha_laco() or self.ha_paralelas(): return False

        return len(self.vertices_nao_adjacentes()) == 0

    def dfs(self, raiz: str=''):
        arvore_dfs = MeuGrafo()
        arvore_dfs.adiciona_vertice(raiz)

        def dfs_rec(V: str, arvore_dfs: MeuGrafo):
            adj = list(self.arestas_sobre_vertice(V))
            # adj.sort()
            for i in adj:
                a: ArestaDirecionada = self._arestas[i.rotulo]
                proximo_vertice = a.v2 if a.v1.rotulo == V else a.v1
                if not arvore_dfs.existe_vertice(proximo_vertice):
                    arvore_dfs.adiciona_vertice(proximo_vertice.rotulo)
                    arvore_dfs.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
                    dfs_rec(proximo_vertice.rotulo, arvore_dfs)
            return arvore_dfs

        return dfs_rec(raiz, arvore_dfs)



