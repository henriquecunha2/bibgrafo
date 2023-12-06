from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_lista_adj_dir import *
from bibgrafo.aresta import ArestaDirecionada

'''
    TODO: adicionar docstring
'''

vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
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

grafo_pb5 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['J'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['C'], vertices_pb['P']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb5, 'test_json/grafo_pb5.json')

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

a = Vertice('A')
b = Vertice('B')
c = Vertice('C')
d = Vertice('D')

grafo_l1 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()).vertices(2) \
    .arestas([
        ArestaDirecionada('a1', a, a),
        ArestaDirecionada('a2', b, a),
        ArestaDirecionada('a3', a, a)]).build()

GrafoJSON.grafo_to_json(grafo_l1, 'test_json/grafo_l1.json')

grafo_l2 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(4).arestas([
        ArestaDirecionada('a1', a, b),
        ArestaDirecionada('a2', b, b),
        ArestaDirecionada('a3', b, a)]).build()

GrafoJSON.grafo_to_json(grafo_l2, 'test_json/grafo_l2.json')

grafo_l3 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(4).arestas([
        ArestaDirecionada('a1', c, a),
        ArestaDirecionada('a2', c, c),
        ArestaDirecionada('a3', d, d),
        ArestaDirecionada('a4', d, d)]).build()

GrafoJSON.grafo_to_json(grafo_l3, 'test_json/grafo_l3.json')

grafo_l4 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()).vertices([Vertice('A')]).build()

# grafo_l4 e grafo_l5 para matrizes de adjacência podem ser aleatórios
