import sys
sys.path.insert(0, 'generated')

from antlr4 import *
from PruebaLL1Lexer import PruebaLL1Lexer
from PruebaLL1Parser import PruebaLL1Parser

def test(input_str):
    input_stream = InputStream(input_str)
    lexer = PruebaLL1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PruebaLL1Parser(stream)

    # Intentar construir el árbol de derivación
    tree = parser.program()
    print(f"Entrada: '{input_str}' -> Procesada correctamente")

if __name__ == '__main__':
    # Pruebas basadas en la tabla de análisis
    test("ab") # Deriva de ReglaS1: A(eps) a A(eps) b
    test("ba") # Deriva de ReglaS2: B(eps) b B(eps) a
