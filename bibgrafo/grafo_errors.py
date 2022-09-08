"""
Este módulo contém classes que definem erros para serem lançados como exceções.
"""

class VerticeInvalidoError(Exception):
    """
    Esta classe deve ser usada quando o vértice não existe no grafo ou quando o formato do vértice for inválido.
    """
    pass

class ArestaInvalidaError(Exception):
    """
    Esta classe deve ser usada quando a aresta não existe no grafo ou quando o formato da aresta for inválida.
    """
    pass

class MatrizInvalidaError(Exception):
    """
    Esta classe deve ser usada quando a matriz de adjacência não estiver no formato correto.
    Pode ser usada nas classes GrafoMatrizAdjacenciaDirecionado e GrafoMatrizAdjacenciaNaoDirecionado.
    """
    pass