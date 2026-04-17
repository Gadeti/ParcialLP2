# Diseño Gramática CRUD 
 
Se diseña una gramática de un lenguaje de programación que permite realizar las operaciones fundamentales de CRUD (Create, Read, Update, Delete) sobre una base de datos no relacional. 
 
---
 
## 1. Definición de la Gramática Independiente del Contexto (GIC)
 
Se definen los símbolos no terminales para organizar la jerarquía lógica del programa.
 
| No Terminal | Reglas de Producción | Descripción |
| :--- | :--- | :--- |
| **S** | `program` → `instruccion+` | Raíz del programa (soporta múltiples comandos). |
| **Instruccion** | `crear` \| `leer` \| `actualizar` \| `borrar` | Clasificación semántica de operaciones. |
| **Crear** | `INSERT INTO ID VALUES objeto` | Operación de inserción de documentos. |
| **Leer** | `FIND IN ID WHERE filtro` | Consulta con lógica de filtrado. |
| **Actualizar** | `UPDATE ID SET objeto WHERE filtro` | Modificación de documentos existentes. |
| **Borrar** | `REMOVE FROM ID WHERE filtro` | Eliminación de registros según condición. |
| **Objeto** | `{ listaAtributos? }` | Estructura de datos JSON-like. |
 
---
 
## 2. Jerarquía de Precedencia y Asociatividad de Expresiones
 
Para evitar ambigüedades en los filtros (cláusula `WHERE`), se implementa un no terminal distinto para cada nivel de precedencia.
 
| Nivel | Operador | No Terminal | Asociatividad | Precedencia |
| :---: | :--- | :--- | :--- | :--- |
| 1 | `\|\|` (OR) | `filtro` | Izquierda (`E → E op T`) | Menor |
| 2 | `&&` (AND) | `terminoAnd` | Izquierda (`E → E op T`) | Media |
| 3 | `==`, `!=`, `>`, `<`, `>=`, `<=` | `comparacion` | N/A (Relacional) | Mayor |
 
> **Nota de diseño:** Al definir `filtro → filtro || terminoAnd`, se garantiza que el operador `||` sea asociativo por la izquierda, procesando de forma lineal el árbol sintáctico.
 
---
 
## 3. Estructura de Datos y Derivación de Listas (ASA)
 
Para el manejo de múltiples atributos (ej. `nombre: "X", edad: 20`), se aplica el concepto de derivación de listas, análogo al manejo de declaraciones como `int a, b, c;` en otros lenguajes.
 
Un **Analizador Sintáctico Ascendente (ASA)** reconstruiría la inversa de una derivación por la derecha de la siguiente forma:
 
```
Entrada:          ID : valor , ID : valor
Reducción 1:      par        , ID : valor
Reducción 2:      par        , par
Reducción Final:  listaAtributos
```
 
Esto permite que el procesador de lenguaje valide secuencias arbitrariamente largas de datos de forma eficiente.
 
---
 
## 4. Visualización del Árbol de Derivación (Parse Tree)
 
Sentencia de entrada: `FIND IN ventas WHERE total > 100 || zona == "norte"`
 
```text
           [program]
               |
         [instruccion]
               |
            [leer]
      _________|__________________________________________
     |    |    |   |            [filtro]
   FIND   IN   ID WHERE   __________|____________________
             (ventas)    |          |                    |
                      [filtro]      ||             [terminoAnd]
                         |                               |
                   [terminoAnd]                    [comparacion]
                         |                          _____|_____
                   [comparacion]                   |     |     |
                 ________|________                 ID  OP_REL valor
                |        |        |             (zona)  (==) ("norte")
                ID     OP_REL   valor
             (total)    (>)     (100)
```
 
> El diseño asegura que las comparaciones `total > 100` y `zona == "norte"` se encuentren en niveles más profundos del árbol, evaluándose antes de aplicar el operador lógico `||`.
 
---
 
## 5. Especificación de Tokens (Análisis Léxico)
 
Inspirado en el caso de estudio KAFE (construido con ANTLR + Python), se definen los siguientes componentes léxicos:
 
| Token | Expresión Regular / Valor | Función |
| :--- | :--- | :--- |
| **Palabras reservadas** | `INSERT`, `FIND`, `UPDATE`, `REMOVE`, `INTO`, `VALUES`, `WHERE`, `SET` | Comandos del lenguaje. |
| `ID` | `[a-zA-Z_][a-zA-Z0-9_]*` | Nombres de colecciones y llaves. |
| `STRING` | `"(...)"` \| `'(...)'` | Literales de texto. |
| `NUMBER` | `[0-9]+(.[0-9]+)?` | Valores numéricos enteros y decimales. |
| `BOOLEAN` | `true` \| `false` | Valores lógicos. |
| `OP_REL` | `==` \| `!=` \| `>` \| `<` \| `>=` \| `<=` | Operadores de comparación. |
| `WS` | `[ \t\r\n]+ -> skip` | Espacios en blanco y saltos de línea (ignorar). |
