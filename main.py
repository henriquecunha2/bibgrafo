from meu_grafo import *

g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adiciona_aresta('a1', 'J', 'C')
g_p.adiciona_aresta('a2', 'C', 'E')
g_p.adiciona_aresta('a3', 'C', 'E')
g_p.adiciona_aresta('a4', 'P', 'C')
g_p.adiciona_aresta('a5', 'P', 'C')
g_p.adiciona_aresta('a6', 'T', 'C')
g_p.adiciona_aresta('a7', 'M', 'C')
g_p.adiciona_aresta('a8', 'M', 'T')
g_p.adiciona_aresta('a9', 'T', 'Z')

print(g_p)

g_p.removeVertice('P')
g_p.removeVertice('E')

print(g_p)

g_p.removeVertice('E')