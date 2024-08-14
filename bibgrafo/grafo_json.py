import os
import json
from bibgrafo.grafo import *
from bibgrafo.grafo_errors import GrafoJSONError
class GrafoJSON:
    @staticmethod
    def grafo_to_json(grafo: GrafoIF, path: str):
        if not isinstance(grafo, GrafoIF):
            raise GrafoJSONError('O objeto informado não é um grafo')

        grafo_dict = dict()
        grafo_dict['n'] = list()
        grafo_dict['a'] = list()
        grafo_dict['g'] = dict()

        for v in grafo.vertices: grafo_dict['n'].append(v.rotulo)

        if hasattr(grafo, 'matriz'):
            for v1 in range(len(grafo.vertices)):
                for v2 in range(len(grafo.vertices)):
                    for aresta in grafo.matriz[v1][v2]:
                        grafo_dict['a'].append(aresta)
                        grafo_dict['g'][aresta] = {
                            'v1': grafo.matriz[v1][v2][aresta].v1.rotulo,
                            'v2': grafo.matriz[v1][v2][aresta].v2.rotulo,
                            'peso': grafo.matriz[v1][v2][aresta].peso
                        }

        elif hasattr(grafo, 'arestas'):
            for aresta in grafo.arestas:
                grafo_dict['a'].append(aresta)
                grafo_dict['g'][aresta] = {
                    'v1': grafo.arestas[aresta].v1.rotulo,
                    'v2': grafo.arestas[aresta].v2.rotulo,
                    'peso': grafo.arestas[aresta].peso
                }

        with open(path, 'w') as json_file:
            grafo_json = json.dumps(grafo_dict, indent=4)
            json_file.write(grafo_json)

        return grafo_dict

    @staticmethod
    def json_to_grafo(path: str, grafo: GrafoIF):
        if not isinstance(grafo, GrafoIF):
            raise GrafoJSONError('O objeto informado não é um grafo')

        grafo_dict: dict
        with open(path, 'r') as grafo_json:
            grafo_dict = json.load(grafo_json)

        for v in grafo_dict['n']: grafo.adiciona_vertice(v)

        for a in grafo_dict['a']:
            grafo.adiciona_aresta(a, grafo_dict['g'][a]['v1'],
                grafo_dict['g'][a]['v2'], grafo_dict['g'][a]['peso'])

        return grafo
