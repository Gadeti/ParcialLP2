# Demostración de Gramática LL(1)

## Requisitos

- Python `>= 3.10`
- Java `>= 11`

```bash
pip install antlr4-python3-runtime==4.13.2
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

## Estructura del proyecto

```
PruebaLL1/
├── PruebaLL1.g4        # Gramática LL(1)
├── test.py             # Pruebas de análisis sintáctico
└── generated/          # Generado automáticamente por ANTLR4
    ├── PruebaLL1Lexer.py
    ├── PruebaLL1Parser.py
    └── PruebaLL1Listener.py
```

## Ejecución

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -o generated PruebaLL1.g4 && python test.py
```

> La compilación con ANTLR4 solo es necesaria la primera vez, o cuando se modifique `PruebaLL1.g4`. Para ejecuciones posteriores basta con:
>
> ```bash
> python test.py
> ```

## Salida esperada

```
──────────────────────────────────────────────────
  Prueba 1 — ReglaS1: A(ε) a A(ε) b
  Entrada: 'ab'
──────────────────────────────────────────────────
  [ÉXITO] Árbol: (program (s (a) a (a) b) <EOF>)

──────────────────────────────────────────────────
  Prueba 2 — ReglaS2: B(ε) b B(ε) a
  Entrada: 'ba'
──────────────────────────────────────────────────
  [ÉXITO] Árbol: (program (s (b) b (b) a) <EOF>)

──────────────────────────────────────────────────
  Prueba 3 — ERROR: 'aa' no pertenece a la gramática
  Entrada: 'aa'
──────────────────────────────────────────────────
  [ERROR] línea 1:1 → mismatched input 'a' expecting 'b'

──────────────────────────────────────────────────
  Prueba 4 — ERROR: 'bb' no pertenece a la gramática
  Entrada: 'bb'
──────────────────────────────────────────────────
  [ERROR] línea 1:1 → mismatched input 'b' expecting 'a'

──────────────────────────────────────────────────
  Prueba 5 — ERROR: entrada vacía
  Entrada: ''
──────────────────────────────────────────────────
  [ERROR] línea 1:0 → mismatched input '<EOF>' expecting {'a', 'b'}
```

---


## 1. Definición de la Gramática
- $S \rightarrow AaAb \mid BbBa$
- $A \rightarrow \epsilon$
- $B \rightarrow \epsilon$

## 2. Conjuntos de Selección (FIRST y FOLLOW)
Para decidir si es LL(1), calculamos los terminales de inicio y de seguimiento:

| Símbolo | FIRST | FOLLOW |
| :--- | :--- | :--- |
| **S** | {a, b} | { $ } |
| **A** | { $\epsilon$ } | {a, b} |
| **B** | { $\epsilon$ } | {a, b} |

**Análisis de producciones de S:**
- $FIRST(AaAb) = \{a\}$ (Ya que A deriva en vacío, el primer terminal es 'a').
- $FIRST(BbBa) = \{b\}$ (Ya que B deriva en vacío, el primer terminal es 'b').

## 3. Tabla de Análisis Sintáctico LL(1)
La tabla M[NoTerminal, Terminal] permite al analizador tomar decisiones con un solo token de preanálisis (lookahead):

| NT \ T | a | b | $ |
| :--- | :--- | :--- | :--- |
| **S** | $S \rightarrow AaAb$ | $S \rightarrow BbBa$ | - |
| **A** | $A \rightarrow \epsilon$ | $A \rightarrow \epsilon$ | - |
| **B** | $B \rightarrow \epsilon$ | $B \rightarrow \epsilon$ | - |

## 4. Conclusión de la Prueba
Una gramática es LL(1) si para toda producción $A \rightarrow \alpha \mid \beta$:
1. $FIRST(\alpha) \cap FIRST(\beta) = \emptyset$.
   - **Prueba:** $\{a\} \cap \{b\} = \emptyset$. **(Cumple)**.
2. Si $\epsilon \in FIRST(\alpha)$, entonces $FIRST(\beta) \cap FOLLOW(A) = \emptyset$.
   - **Prueba:** No aplica para S, y A/B solo tienen una opción, eliminando conflictos.

**Resultado:** La gramática es **LL(1)**.
