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

class GrafoJSONError(Exception):
    """
    Esta classe deve ser usada para erros no módulo GrafoJSON, quando informações inválidas forem passadas
    para as funções do módulo.
    """

class GrafoInvalidoError(Exception):
    """
    Esta classe deve ser usada quando uma instância que não herde de GrafoIF seja passada para o builder.
    Pode ser usada na classe GrafoBuilder.
    """

class GrafoBuilderError(Exception):
    """
    Esta classe deve ser usada quando configurações conflitantes forem utilizadas no GrafoBuilder.
    """
    pass
