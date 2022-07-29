from bibgrafo.grafo_matriz_adj_nao_dir import *
from bibgrafo.grafo_exceptions import *
from sys import maxsize

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        nao_adjacentes = set()
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if i != j and j > i and not bool(self.M[i][j]):
                    nao_adjacentes.add('{}-{}'.format(self.N[i], self.N[j]))
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
                if j >= i:
                    for k in self.M[i][j].values():
                        if k.get_v1() == V:
                            grau += 1
                        if k.get_v2() == V:
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
            if bool(self.M[v][i]) and v <= i:
                for k in self.M[v][i]:
                    arestas.append(k)
            if bool(self.M[i][v]) and i <= v:
                for l in self.M[i][v]:
                    arestas.append(l)
        return arestas

    def eh_laco(self, a):
        v1, v2 = a.split("-")
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

    def warshall(self):
        m = deepcopy(self.M)
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if len(self.M[i][j]) > 0:
                    m[i][j] = 1
                else:
                    m[i][j] = 0

        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if m[j][i] == 1:
                    for k in range(len(self.N)):
                        m[j][k] = max(m[j][k], m[i][k])

        return m

    def vertice_oposto(self, a, v):
        if a.get_v1() == v:
            return a.get_v2()
        return a.get_v1()

    def menor_nao_visitado(self, beta, visitado):
        aux = deepcopy(beta)
        while True:
            minimo = min(aux)
            i_v = beta.index(minimo)
            v = self.N[i_v]
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

        for i in self.N:
            beta.append(maxsize)
            visitado[i] = 0
            predecessor[i] = 0

        indice_v = self.N.index(u)
        beta[indice_v] = 0
        visitado[u] = 1

        w = u
        while w != v:
            # Atualizando os betas de r para cada arco (w,r)
            arestas = self.arestas_sobre_vertice(w)
            for a in arestas:
                r = self.vertice_oposto(a, w)
                i_r = self.N.index(r)
                i_w = self.N.index(w)
                if beta[i_r] > beta[i_w]+a.get_peso():
                    beta[i_r] = beta[i_w]+a.get_peso()
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