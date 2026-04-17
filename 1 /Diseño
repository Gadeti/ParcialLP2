# ESPECIFICACIÓN TÉCNICA: DSL NoSQL-CRUD

Este documento define la estructura formal del lenguaje de dominio específico (DSL) para operaciones CRUD en bases de datos no relacionales, siguiendo los estándares de diseño de procesadores de lenguajes [1].

## 1. Definición de la Gramática (GIC)
Siguiendo el modelo de una **Gramática Independiente del Contexto (GIC)**, el lenguaje se descompone en los siguientes símbolos no terminales para organizar la jerarquía del programa [2].

| No Terminal | Reglas de Producción | Descripción |
| :--- | :--- | :--- |
| **S** | `program` $\rightarrow$ `instruccion+` | Raíz del programa (Secuencia de comandos). |
| **Instruccion** | `crear` \| `leer` \| `actualizar` \| `borrar` | Operaciones CRUD fundamentales. |
| **Crear** | `INSERT INTO ID VALUES objeto` | Inserción de documentos en colecciones. |
| **Leer** | `FIND IN ID WHERE filtro` | Consulta de datos con filtrado lógico. |
| **Objeto** | `{ listaAtributos? }` | Estructura de datos tipo JSON. |
| **Filtro** | `filtro || terminoAnd` \| `terminoAnd` | Nivel de precedencia 1 (Disyunción). |
| **TerminoAnd** | `terminoAnd && comparacion` \| `comparacion` | Nivel de precedencia 2 (Conjunción). |
| **Comparacion** | `ID OP_REL valor` | Nivel de precedencia 3 (Relacional). |

---

## 2. Jerarquía de Precedencia y Asociatividad
Para evitar la **ambigüedad** en el análisis sintáctico lineal, la gramática utiliza terminales distintos para cada nivel de prioridad [2]:

1.  **Mayor Precedencia:** Operadores relacionales (`==`, `!=`, `>`, `<`, `>=`, `<=`). Se evalúan primero.
2.  **Precedencia Media:** Operador lógico `&&` (AND).
3.  **Menor Precedencia:** Operador lógico `||` (OR).

**Asociatividad:** Las reglas están diseñadas con **asociatividad por la izquierda** (ej. `filtro -> filtro || terminoAnd`), lo que garantiza que las expresiones se agrupen de izquierda a derecha durante la construcción del árbol [2].

---

## 3. Estructura de Datos: Derivación de Listas
El manejo de múltiples atributos dentro de un objeto se resuelve mediante una **derivación recursiva**, similar a la declaración de variables en lenguajes como C o Java [2]:

*   `listaAtributos` $\rightarrow$ `par` (`,` `par`)*
*   `par` $\rightarrow$ `ID : valor`

Este diseño permite que el **Analizador Sintáctico Ascendente (ASA)** reconstruya la inversa de una derivación por la derecha de manera eficiente, acumulando tokens para validar la sintaxis del objeto [2].

---

## 4. Ejemplo de Árbol de Derivación (Parse Tree)
Sentencia de entrada: `FIND IN logs WHERE tipo == "error" && severidad > 5`

```text
           [program]
               |
         [instruccion]
               |
            [leer]
      _________|__________________________________________
     |    |    |   |            [filtro]
   FIND   IN   ID WHERE            |
             (logs)           [terminoAnd]
                    _______________|______________________
                   |               |                      |
             [terminoAnd]          &&               [comparacion]
                   |                                ______|______
             [comparacion]                         |      |      |
         __________|__________                     ID   OP_REL  valor
        |          |          |               (severidad) (>)    (5)
        ID       OP_REL     valor
      (tipo)      (==)     ("error")
El diseño asegura que los operadores de mayor prioridad (comparaciones) queden en las hojas más profundas del árbol, evaluándose antes que los operadores lógicos
.

--------------------------------------------------------------------------------
5. Especificación de Tokens (Análisis Léxico)
Basado en el modelo de implementación ANTLR + Python utilizado en el caso de estudio KAFE
:
Token
Expresión Regular / Valor
Función
ID
[a-zA-Z_][a-zA-Z0-9_]*
Identificadores de colecciones y claves.
OP_REL
== | != | > | < | >= | <=
Operadores de comparación.
STRING
"(...)" | '(...)'
Literales de texto.
NUMBER
+(\.
+)?
Valores numéricos.
BOOLEAN
true | false
Valores lógicos.
WS
[ \t\r\n]+ -> skip
Ignorar espacios en blanco.
