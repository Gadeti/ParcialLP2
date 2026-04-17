import sys
sys.path.insert(0, 'generated')

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from PruebaLL1Lexer import PruebaLL1Lexer
from PruebaLL1Parser import PruebaLL1Parser


class CRUDErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"línea {line}:{column} → {msg}")


def test(input_str, descripcion):
    print(f"\n{'─'*50}")
    print(f"  {descripcion}")
    print(f"  Entrada: '{input_str}'")
    print(f"{'─'*50}")

    input_stream = InputStream(input_str)
    lexer = PruebaLL1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PruebaLL1Parser(stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    error_listener = CRUDErrorListener()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.errors:
        for e in error_listener.errors:
            print(f"  [ERROR] {e}")
    else:
        print(f"  [ÉXITO] Árbol: {tree.toStringTree(recog=parser)}")


if __name__ == '__main__':
    # Casos válidos
    test("ab", "Prueba 1 — ReglaS1: A(ε) a A(ε) b")
    test("ba", "Prueba 2 — ReglaS2: B(ε) b B(ε) a")

    # Casos inválidos
    test("aa", "Prueba 3 — ERROR: 'aa' no pertenece a la gramática")
    test("bb", "Prueba 4 — ERROR: 'bb' no pertenece a la gramática")
    test("",   "Prueba 5 — ERROR: entrada vacía")
