from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *
from sys import maxsize

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        nao_adjacentes = list()
        for i in range(len(self._vertices)):
            for j in range(len(self._vertices)):
                if i != j and not bool(self._matriz[i][j]):
                    nao_adjacentes.append('{}-{}'.format(self._vertices[i], self._vertices[j]))
        return nao_adjacentes

    def ha_laco(self):
        for i in range(len(self._matriz)):
            if bool(self._matriz[i][i]):
                return True
        return False

    def grau(self, V=''):

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo'.format(V))

        grau = 0
        for i in range(len(self._matriz)):
            for j in range(len(self._matriz)):
                for k in self._matriz[i][j].values():
                    if k.v1.rotulo == V:
                        grau += 1
                    if k.v2.rotulo == V:
                        grau += 1
        return grau

    def ha_paralelas(self):
        for i in range(len(self._matriz)):
            for j in range(len(self._matriz)):
                if len(self._matriz[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        # Se o vértice não existir
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo'.format(V))
        arestas = set()
        v = self.get_vertice(V)
        v = self._vertices.index(v)
        for i in range(len(self._matriz)):
            if bool(self._matriz[v][i]):
                for k in self._matriz[v][i]:
                    arestas.add(k)
            if bool(self._matriz[i][v]):
                for l in self._matriz[i][v]:
                    arestas.add(l)
        return arestas

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
            proximo_vertice = a.v2() if a.v1() == V else a.v1()
            if not arvore_dfs.existe_vertice(proximo_vertice):
                arvore_dfs.adiciona_vertice(proximo_vertice)
                arvore_dfs.adiciona_aresta(a.rotulo(), a.v1(), a.v2())
                self.dfs_rec(proximo_vertice, arvore_dfs)
        return arvore_dfs

    def warshall(self):
        m = deepcopy(self._matriz)
        for i in range(len(self._vertices)):
            for j in range(len(self._vertices)):
                if len(self._matriz[i][j]) > 0:
                    m[i][j] = 1
                else:
                    m[i][j] = 0

        for i in range(len(self._vertices)):
            for j in range(len(self._vertices)):
                if m[j][i] == 1:
                    for k in range(len(self._vertices)):
                        m[j][k] = max(m[j][k], m[i][k])

        return m

    def vertice_oposto(self, a, v):
        if a.v1() == v:
            return a.v2()
        return a.v1()

    def menor_nao_visitado(self, beta, visitado):
        aux = deepcopy(beta)
        while True:
            minimo = min(aux)
            i_v = beta.index(minimo)
            v = self._vertices[i_v]
            if visitado[v] == 1 and len(aux) > 0:
                aux.remove(minimo)
            else:
                break
        if len(aux) == 0:
            return ""
        return v

    def dijkstra(self, u, v, ci, cm, recarga):
        beta = list()
        visitado = dict()
        predecessor = dict()

        for i in self._vertices:
            beta.append(maxsize)
            visitado[i] = 0
            predecessor[i] = 0

        indice_v = self._vertices.index(u)
        beta[indice_v] = 0
        visitado[u] = 1

        w = u
        while w != v:
            # Atualizando os betas de r para cada arco (w,r)
            arestas = self.arestas_sobre_vertice(w)
            for a in arestas:
                r = self.vertice_oposto(a, w)
                i_r = self._vertices.index(r)
                i_w = self._vertices.index(w)
                if beta[i_r] > beta[i_w]+a.peso():
                    beta[i_r] = beta[i_w]+a.peso()
                    predecessor[r] = w

            # Achando r*
            r_ast = self.menor_nao_visitado(beta, visitado)
            if r_ast == "":
                return False

            visitado[r_ast] = 1
            w = r_ast

        caminho_mais_curto = [w]
        while w != u:
            caminho_mais_curto.insert(0, predecessor[w])
            ant = w
            w = predecessor[w]
            predecessor.pop(ant)
        return caminho_mais_curto