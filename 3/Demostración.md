# Demostración de Gramática LL(1)

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
