from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_lista_adj_dir import *
from bibgrafo.aresta import ArestaDirecionada

'''
    TODO: adicionar docstring
'''

vertices_pb = ['J', 'C', 'E', 'P', 'M', 'Z', 'T']

grafo_pb = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices_pb).arestas([
        ArestaDirecionada('a1', Vertice('J'), Vertice('C')),
        ArestaDirecionada('a2', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a3', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a4', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a5', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a6', Vertice('T'), Vertice('C')),
        ArestaDirecionada('a7', Vertice('M'), Vertice('C')),
        ArestaDirecionada('a8', Vertice('M'), Vertice('T')),
        ArestaDirecionada('a9', Vertice('T'), Vertice('Z'))
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb, 'test_json/grafo_pb.json')

grafo_pb2 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices_pb).arestas([
        ArestaDirecionada('a1', Vertice('J'), Vertice('C')),
        ArestaDirecionada('a2', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a3', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a4', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a5', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a6', Vertice('T'), Vertice('C')),
        ArestaDirecionada('a7', Vertice('M'), Vertice('C')),
        ArestaDirecionada('a8', Vertice('M'), Vertice('T')),
        ArestaDirecionada('a9', Vertice('T'), Vertice('Z'))
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb2, 'test_json/grafo_pb2.json')

'''
    Este grafo da Paraíba possui uma pequena diferença
    na primeira aresta, para testes com o método __eq__
    (operador de comparação ==).
'''
grafo_pb3 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices_pb).arestas([
        ArestaDirecionada('a0', Vertice('J'), Vertice('C')),
        ArestaDirecionada('a2', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a3', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a4', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a5', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a6', Vertice('T'), Vertice('C')),
        ArestaDirecionada('a7', Vertice('M'), Vertice('C')),
        ArestaDirecionada('a8', Vertice('M'), Vertice('T')),
        ArestaDirecionada('a9', Vertice('T'), Vertice('Z'))
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb3, 'test_json/grafo_pb3.json')

'''
    Este grafo da Paraíba possui uma pequena diferença
    na segunda aresta para testes com o método __eq__.
'''
grafo_pb4 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices_pb).arestas([
        ArestaDirecionada('a1', Vertice('J'), Vertice('C')),
        ArestaDirecionada('a2', Vertice('J'), Vertice('E')),
        ArestaDirecionada('a3', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a4', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a5', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a6', Vertice('T'), Vertice('C')),
        ArestaDirecionada('a7', Vertice('M'), Vertice('C')),
        ArestaDirecionada('a8', Vertice('M'), Vertice('T')),
        ArestaDirecionada('a9', Vertice('T'), Vertice('Z'))
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb4, 'test_json/grafo_pb4.json')

grafo_pb_simples = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices_pb).arestas([
        ArestaDirecionada('a1', Vertice('J'), Vertice('C')),
        ArestaDirecionada('a2', Vertice('C'), Vertice('E')),
        ArestaDirecionada('a3', Vertice('P'), Vertice('C')),
        ArestaDirecionada('a4', Vertice('T'), Vertice('C')),
        ArestaDirecionada('a5', Vertice('M'), Vertice('C')),
        ArestaDirecionada('a6', Vertice('M'), Vertice('T')),
        ArestaDirecionada('a7', Vertice('T'), Vertice('Z'))
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb_simples, 'test_json/grafo_pb_simples.json')

'''
    Este é um grafo da Paraíba completo.
'''
grafo_pb_completo = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices_pb).arestas(True).build()

GrafoJSON.grafo_to_json(grafo_pb_completo, 'test_json/grafo_pb_completo.json')
