from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_lista_adj_dir import *
from bibgrafo.aresta import ArestaDirecionada

'''
    TODO: adicionar docstring
'''

vertices = ['J', 'C', 'E', 'P', 'M', 'Z', 'T']
vertices_pb = {v: Vertice(v) for v in vertices}

grafo_pb = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb, 'test_json/grafo_pb.json')

grafo_pb2 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb2, 'test_json/grafo_pb2.json')

'''
    Este grafo da Paraíba possui uma pequena diferença
    na primeira aresta, para testes com o método __eq__
    (operador de comparação ==).
'''
grafo_pb3 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a0', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb3, 'test_json/grafo_pb3.json')

'''
    Este grafo da Paraíba possui uma pequena diferença
    na segunda aresta para testes com o método __eq__.
'''
grafo_pb4 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['J'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb4, 'test_json/grafo_pb4.json')

grafo_pb_simples = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a4', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a7', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb_simples, 'test_json/grafo_pb_simples.json')

'''
    Este é um grafo da Paraíba completo.
'''
grafo_pb_completo = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas(True).build()

GrafoJSON.grafo_to_json(grafo_pb_completo, 'test_json/grafo_pb_completo.json')
