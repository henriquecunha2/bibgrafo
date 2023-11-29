import unittest
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import *
from bibgrafo.grafo_builder import *
from bibgrafo.grafo_errors import GrafoBuilderError
from meu_grafo_teste_builder import *

class TestBuilderGrafo(unittest.TestCase):

    def test_rotulo_vertices(self):
        for i in range(50):
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(i).build()
            for v in grafo.vertices: self.assertTrue(v.rotulo.isalpha() and v.rotulo.isupper())
        with self.assertRaises(GrafoBuilderError):
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(3, start='1').build()

    def test_grafo_completo(self):
        for i in range(1, 30):
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(i)\
                .arestas(True).build()
            self.assertTrue(grafo.eh_completo())

    def test_grafo_simples(self):
        for i in range(2, 20):
            for j in range(i, 100):
                try:
                    grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(i) \
                        .arestas(j).build()
                    self.assertFalse(grafo.ha_laco() and grafo.ha_paralelas())
                except GrafoBuilderError: continue

    def test_laco_paralelas(self):
        for i in range(2, 20):
            for j in range(1, i):
                grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(i) \
                    .arestas(i - 1, paralelas=1, lacos=1).build()
                self.assertTrue(grafo.ha_paralelas() and grafo.ha_laco())

        with self.assertRaises(GrafoBuilderError):
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(2) \
                .arestas(-1).build()
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(2) \
                .arestas(2, lacos=-1).build()
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(2) \
                .arestas(2, paralelas=-1).build()
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(2) \
                .arestas(2, desconexos=3).build()

    def test_grafo_conexo(self):
        for i in range(1, 20):
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(i) \
                .arestas(True).build()
            self.assertTrue(grafo.conexo())

    def test_vertices(self):
        self.assertTrue(GrafoBuilder().tipo(MeuGrafo()).vertices(['A', 'B', 'C']).build())
        with self.assertRaises(GrafoBuilderError):
            self.assertTrue(GrafoBuilder().tipo(MeuGrafo()).vertices([]).build())

    def test_arestas(self):
        self.assertTrue(GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas([Aresta('a1',
            Vertice('A'), Vertice('B'))], peso_min=1, peso_max=3).build())
        with self.assertRaises(GrafoBuilderError):
            self.assertTrue(GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas([]).build())