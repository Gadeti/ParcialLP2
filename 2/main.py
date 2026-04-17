import sys
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from generated.NoSQLCRUDLexer import NoSQLCRUDLexer
from generated.NoSQLCRUDParser import NoSQLCRUDParser


# ── Error listener personalizado ──────────────────────────────────────────────
class CRUDErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"  [ERROR] línea {line}:{column} → {msg}")


# ── Función principal de análisis ─────────────────────────────────────────────
def analizar(entrada: str, descripcion: str):
    print(f"\n{'─'*60}")
    print(f"  {descripcion}")
    print(f"  Entrada: {entrada.strip()}")
    print(f"{'─'*60}")

    stream = InputStream(entrada)
    lexer  = NoSQLCRUDLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = NoSQLCRUDParser(tokens)

    # Reemplazar listeners de error por defecto
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    error_listener = CRUDErrorListener()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.errors:
        for e in error_listener.errors:
            print(e)
    else:
        print("  [ÉXITO] Árbol sintáctico:")
        print(f"  {tree.toStringTree(recog=parser)}")


# ── Casos de prueba ───────────────────────────────────────────────────────────
if __name__ == "__main__":

    # Prueba 1: Inserción con objeto complejo
    analizar(
        'INSERT INTO clientes VALUES { nombre: "Juan", edad: 25 }',
        "Prueba 1 — Inserción con objeto complejo"
    )

    # Prueba 2: Consulta con precedencia booleana (> antes que &&)
    analizar(
        'FIND IN stock WHERE precio > 100 && activo == true',
        "Prueba 2 — Consulta con precedencia booleana"
    )

    # Prueba 3: Actualización con filtro OR
    analizar(
        'UPDATE usuarios SET { activo: false } WHERE rol == "invitado" || rol == "temporal"',
        "Prueba 3 — Actualización con filtro OR"
    )

    # Prueba 4: Eliminación simple
    analizar(
        'REMOVE FROM logs WHERE nivel == "debug"',
        "Prueba 4 — Eliminación simple"
    )

    # Prueba 5 (ERROR): Falta coma entre pares del objeto
    analizar(
        'INSERT INTO col VALUES { a:1 b:2 }',
        "Prueba 5 — ERROR: falta ',' entre pares"
    )

    # Prueba 6 (ERROR): Filtro incompleto (falta valor tras operador)
    analizar(
        'FIND IN productos WHERE precio >',
        "Prueba 6 — ERROR: filtro incompleto"
    )
