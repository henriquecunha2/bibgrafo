import unittest
from bibgrafo.grafo_builder import *
from bibgrafo.grafo_errors import GrafoBuilderError
from meu_grafo_teste_builder import *

class TestBuilderGrafo(unittest.TestCase):

    def test_rotulo_vertices(self):
        for i in range(50):
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(i).build()
            for v in grafo.vertices: self.assertTrue(v.rotulo.isalpha() and v.rotulo.isupper())

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

    def test_grafo_conexo(self):
        for i in range(1, 20):
            grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(i) \
                .arestas(True).build()
            self.assertTrue(grafo.conexo())
