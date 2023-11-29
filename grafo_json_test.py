import unittest
import os
from bibgrafo.grafo_json import *
from bibgrafo.grafo_lista_adj_dir import *
from bibgrafo.grafo_matriz_adj_dir import *

class GrafoJSONTest(unittest.TestCase):
    def setUp(self):
        self.g_l = GrafoListaAdjacenciaDirecionado()
        self.g_m = GrafoMatrizAdjacenciaDirecionado()
        for i in range(5):
            self.g_l.adiciona_vertice(chr(ord('A') + i))
            self.g_m.adiciona_vertice(chr(ord('A') + i))
        for v1 in range(len(self.g_l.vertices)):
            for v2 in range(v1 + 1, len(self.g_l.vertices)):
                self.g_l.adiciona_aresta(chr(ord('a') + (v1)) + str(v2),
                    self.g_l.vertices[v1].rotulo, self.g_l.vertices[v2].rotulo)
                self.g_m.adiciona_aresta(chr(ord('a') + (v1)) + str(v2),
                    self.g_l.vertices[v1].rotulo, self.g_l.vertices[v2].rotulo)

        self.g_dict = dict()
        self.g_dict['n'] = (chr(ord('A') + i) for i in range(5))
        self.g_dict['a'] = ['a1', 'a2', 'a3', 'a4', 'b2', 'b3', 'b4', 'c3', 'c4', 'd4']
        self.g_dict['g'] = {
            'a1': {'v1': 'A', 'v2': 'B', 'peso': 1},
            'a2': {'v1': 'A', 'v2': 'C', 'peso': 1},
            'a3': {'v1': 'A', 'v2': 'D', 'peso': 1},
            'a4': {'v1': 'A', 'v2': 'E', 'peso': 1},
            'b2': {'v1': 'B', 'v2': 'C', 'peso': 1},
            'b3': {'v1': 'B', 'v2': 'D', 'peso': 1},
            'b4': {'v1': 'B', 'v2': 'E', 'peso': 1},
            'c3': {'v1': 'C', 'v2': 'D', 'peso': 1},
            'c4': {'v1': 'C', 'v2': 'E', 'peso': 1},
            'd4': {'v1': 'D', 'v2': 'E', 'peso': 1}
        }

        self.g_l_path = 'gl.json'
        self.g_m_path = 'gm.json'

    def test_json(self):
        self.assertTrue(GrafoJSON.grafo_to_json(self.g_l, self.g_l_path), self.g_dict)
        self.assertTrue(GrafoJSON.grafo_to_json(self.g_m, self.g_m_path), self.g_dict)
        self.assertTrue(GrafoJSON.json_to_grafo(self.g_l_path, GrafoListaAdjacenciaDirecionado())
            == self.g_l)
        self.assertTrue(GrafoJSON.json_to_grafo(self.g_m_path, GrafoMatrizAdjacenciaDirecionado())
            == self.g_m)
        self.assertIsNone(os.remove(self.g_l_path))
        self.assertIsNone(os.remove(self.g_m_path))
        with self.assertRaises(FileNotFoundError):
            self.assertIsNone(open(self.g_l_path, 'r'))
        with self.assertRaises(FileNotFoundError):
            self.assertIsNone(open(self.g_m_path, 'r'))
