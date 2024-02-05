import unittest
from meu_grafo_lista_adj_dir import *
from bibgrafo.grafo_errors import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Este grafo possui orientações diferentes nas arestas, e também não tem paralelas
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'E', 'J')
        self.g_p3.adiciona_aresta('a3', 'E', 'C')
        self.g_p3.adiciona_aresta('a4', 'C', 'P')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Este grafo possui orientações diferentes nas arestas, e também não tem paralelas
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'C', 'J')
        self.g_p4.adiciona_aresta('a2', 'J', 'C')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'C', 'P')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

        # Grafo da Paraíba alterado para buscas
        self.g_busca = MeuGrafo()
        for v in self.g_p.vertices: self.g_busca.adiciona_vertice(v.rotulo)
        self.g_busca.adiciona_aresta('a1', 'J', 'Z')
        self.g_busca.adiciona_aresta('a2', 'Z', 'C')
        self.g_busca.adiciona_aresta('a3', 'C', 'T')
        self.g_busca.adiciona_aresta('a4', 'T', 'P')
        self.g_busca.adiciona_aresta('a5', 'P', 'C')
        self.g_busca.adiciona_aresta('a6', 'P', 'E')
        self.g_busca.adiciona_aresta('a7', 'E', 'Z')
        self.g_busca.adiciona_aresta('a8', 'E', 'M')
        self.g_busca.adiciona_aresta('a9', 'C', 'J')
        self.g_busca.adiciona_aresta('b1', 'T', 'C')
        self.g_busca.adiciona_aresta('b2', 'M', 'P')
        self.g_busca.adiciona_aresta('b3', 'Z', 'E')
        self.g_busca.adiciona_aresta('b4', 'C', 'P')

        self.g_dfs_j = MeuGrafo()
        for v in self.g_busca.vertices: self.g_dfs_j.adiciona_vertice(v.rotulo)
        self.g_dfs_j.adiciona_aresta('a1', 'J', 'Z')
        self.g_dfs_j.adiciona_aresta('a2', 'Z', 'C')
        self.g_dfs_j.adiciona_aresta('a3', 'C', 'T')
        self.g_dfs_j.adiciona_aresta('a4', 'T', 'P')
        self.g_dfs_j.adiciona_aresta('a6', 'P', 'E')
        self.g_dfs_j.adiciona_aresta('a8', 'E', 'M')

        self.g_dfs_p = MeuGrafo()
        for v in self.g_busca.vertices: self.g_dfs_p.adiciona_vertice(v.rotulo)
        self.g_dfs_p.adiciona_aresta('a5', 'P', 'C')
        self.g_dfs_p.adiciona_aresta('a3', 'C', 'T')
        self.g_dfs_p.adiciona_aresta('a9', 'C', 'J')
        self.g_dfs_p.adiciona_aresta('a1', 'J', 'Z')
        self.g_dfs_p.adiciona_aresta('b3', 'Z', 'E')
        self.g_dfs_p.adiciona_aresta('a8', 'E', 'M')

        self.g_dfs_t = MeuGrafo()
        for v in self.g_busca.vertices: self.g_dfs_t.adiciona_vertice(v.rotulo)
        self.g_dfs_t.adiciona_aresta('a4', 'T', 'P')
        self.g_dfs_t.adiciona_aresta('a5', 'P', 'C')
        self.g_dfs_t.adiciona_aresta('a9', 'C', 'J')
        self.g_dfs_t.adiciona_aresta('a1', 'J', 'Z')
        self.g_dfs_t.adiciona_aresta('b3', 'Z', 'E')
        self.g_dfs_t.adiciona_aresta('a8', 'E', 'M')

        self.g_dfs_m = MeuGrafo()
        for v in self.g_busca.vertices: self.g_dfs_m.adiciona_vertice(v.rotulo)
        self.g_dfs_m.adiciona_aresta('b2', 'M', 'P')
        self.g_dfs_m.adiciona_aresta('a5', 'P', 'C')
        self.g_dfs_m.adiciona_aresta('a3', 'C', 'T')
        self.g_dfs_m.adiciona_aresta('a9', 'C', 'J')
        self.g_dfs_m.adiciona_aresta('a1', 'J', 'Z')
        self.g_dfs_m.adiciona_aresta('b3', 'Z', 'E')

        self.g_bfs_j = MeuGrafo()
        for v in self.g_busca.vertices: self.g_bfs_j.adiciona_vertice(v.rotulo)
        self.g_bfs_j.adiciona_aresta('a1', 'J', 'Z')
        self.g_bfs_j.adiciona_aresta('a2', 'Z', 'C')
        self.g_bfs_j.adiciona_aresta('b3', 'Z', 'E')
        self.g_bfs_j.adiciona_aresta('a3', 'C', 'T')
        self.g_bfs_j.adiciona_aresta('b4', 'C', 'P')
        self.g_bfs_j.adiciona_aresta('a8', 'E', 'M')

        self.g_bfs_p = MeuGrafo()
        for v in self.g_busca.vertices: self.g_bfs_p.adiciona_vertice(v.rotulo)
        self.g_bfs_p.adiciona_aresta('a5', 'P', 'C')
        self.g_bfs_p.adiciona_aresta('a6', 'P', 'E')
        self.g_bfs_p.adiciona_aresta('a3', 'C', 'T')
        self.g_bfs_p.adiciona_aresta('a9', 'C', 'J')
        self.g_bfs_p.adiciona_aresta('a1', 'J', 'Z')
        self.g_bfs_p.adiciona_aresta('a8', 'E', 'M')

        self.g_bfs_t = MeuGrafo()
        for v in self.g_busca.vertices: self.g_bfs_t.adiciona_vertice(v.rotulo)
        self.g_bfs_t.adiciona_aresta('a4', 'T' ,'P')
        self.g_bfs_t.adiciona_aresta('b1', 'T', 'C')
        self.g_bfs_t.adiciona_aresta('a6', 'P', 'E')
        self.g_bfs_t.adiciona_aresta('a7', 'E', 'Z')
        self.g_bfs_t.adiciona_aresta('a8', 'E', 'M')
        self.g_bfs_t.adiciona_aresta('a9', 'C', 'J')

        self.g_bfs_m = MeuGrafo()
        for v in self.g_busca.vertices: self.g_bfs_m.adiciona_vertice(v.rotulo)
        self.g_bfs_m.adiciona_aresta('b2', 'M', 'P')
        self.g_bfs_m.adiciona_aresta('a5', 'P', 'C')
        self.g_bfs_m.adiciona_aresta('a6', 'P', 'E')
        self.g_bfs_m.adiciona_aresta('a3', 'C', 'T')
        self.g_bfs_m.adiciona_aresta('a9', 'C', 'J')
        self.g_bfs_m.adiciona_aresta('a1', 'J', 'Z')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau_saida('J'), 1)
        self.assertEqual(self.g_p.grau_entrada('J'), 0)
        self.assertEqual(self.g_p.grau_saida('C'), 2)
        self.assertEqual(self.g_p.grau_entrada('C'), 5)
        self.assertEqual(self.g_p.grau_saida('E'), 0)
        self.assertEqual(self.g_p.grau_entrada('E'), 2)
        self.assertEqual(self.g_p.grau_saida('P'), 2)
        self.assertEqual(self.g_p.grau_entrada('P'), 0)
        self.assertEqual(self.g_p.grau_saida('M'), 2)
        self.assertEqual(self.g_p.grau_entrada('M'), 0)
        self.assertEqual(self.g_p.grau_saida('T'), 2)
        self.assertEqual(self.g_p.grau_entrada('T'), 1)
        self.assertEqual(self.g_p.grau_saida('Z'), 0)
        self.assertEqual(self.g_p.grau_entrada('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau_saida('G'), 5)

        self.assertEqual(self.g_d.grau_entrada('A'), 0)
        self.assertEqual(self.g_d.grau_saida('A'), 1)
        self.assertEqual(self.g_d.grau_entrada('C'), 0)
        self.assertEqual(self.g_d.grau_saida('C'), 0)
        self.assertNotEqual(self.g_d.grau_entrada('D'), 2)
        self.assertNotEqual(self.g_d.grau_entrada('D'), 2)
        self.assertEqual(self.g_d2.grau_entrada('A'), 0)
        self.assertNotEqual(self.g_d.grau_saida('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau_entrada('J'), 0)
        self.assertEqual(self.g_c.grau_saida('J'), 3)
        self.assertEqual(self.g_c.grau_entrada('C'), 3)
        self.assertEqual(self.g_c.grau_saida('C'), 0)
        self.assertEqual(self.g_c.grau_saida('E'), 1)
        self.assertEqual(self.g_c.grau_entrada('E'), 2)
        self.assertEqual(self.g_c.grau_saida('P'), 2)
        self.assertEqual(self.g_c.grau_entrada('P'), 1)

        # Com laço.
        self.assertEqual(self.g_l1.grau_saida('A'), 3)
        self.assertEqual(self.g_l1.grau_entrada('A'), 2)
        self.assertEqual(self.g_l2.grau_entrada('B'), 2)
        self.assertEqual(self.g_l2.grau_saida('B'), 2)
        self.assertEqual(self.g_l4.grau_entrada('D'), 1)
        self.assertEqual(self.g_l4.grau_saida('D'), 1)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas()) # X
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas()) # X
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas()) # X
        self.assertFalse(self.g_p3.ha_paralelas())
        self.assertFalse(self.g_p4.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_busca.dfs('J'), self.g_dfs_j)
        self.assertEqual(self.g_busca.dfs('P'), self.g_dfs_p)
        self.assertEqual(self.g_busca.dfs('T'), self.g_dfs_t)
        self.assertEqual(self.g_busca.dfs('M'), self.g_dfs_m)

    def test_bfs(self):
        self.assertEqual(self.g_busca.bfs('J'), self.g_bfs_j)
        self.assertEqual(self.g_busca.bfs('P'), self.g_bfs_p)
        self.assertEqual(self.g_busca.bfs('T'), self.g_bfs_t)
        self.assertEqual(self.g_busca.bfs('M'), self.g_bfs_m)