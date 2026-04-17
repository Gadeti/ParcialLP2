# Calculadora booleana con YACC y LEX

## Descripción

Este programa evalúa expresiones booleanas usando un analizador sintáctico generado con YACC (LALR) y un analizador léxico con LEX.

Ejemplos de entrada:

```text
1 AND 0
1 OR 0
NOT 1
(1 AND 0) OR 1
```

---

## Compilación y ejecución

Todo en una sola línea, como debería ser:

```bash
bison -d calc.y && flex calc.l && gcc y.tab.c lex.yy.c -o calc -lfl && ./calc < pruebas.txt
```

Si quieres modo interactivo:

```bash
./calc
```

---

## Archivo de pruebas (`pruebas.txt`)

```text
1 AND 0
1 OR 0
NOT 1
NOT 0
(1 AND 1) OR 0
(1 OR 0) AND (NOT 0)
(1 AND (0 OR 1)) OR (NOT (1 AND 0))
(1 OR 1) AND (1 OR 0)
NOT (1 AND 1)
NOT (0 OR 0)
(1 AND 0) OR (1 AND 1)
(1 OR 0) OR (0 AND 1)
NOT NOT 1
NOT NOT 0
(1 AND (1 AND (1 AND 1)))
(0 OR (0 OR (0 OR 1)))
(1 AND 0) OR (1 AND 0) OR (1 AND 1)
(1 OR 0) AND (1 OR 0) AND (1 OR 1)
NOT (1 AND (0 OR (1 AND 0)))
(1 OR (0 AND (1 OR 0)))
```

---

## Desempeño y conclusiones

El analizador sintáctico generado es de tipo **LALR(1)**, lo que permite procesar expresiones de forma eficiente y determinista.

* Complejidad temporal: **O(n)**
* Uso de memoria: proporcional a la profundidad de la expresión

La evaluación se realiza directamente durante el parsing, evitando fases adicionales, lo que mejora el rendimiento.

En comparación con otros enfoques:

* Es más eficiente que CYK (O(n³))
* Más robusto que parsers recursivos simples
* Maneja correctamente precedencia y asociatividad

En la práctica, el desempeño es **rápido incluso con expresiones largas**, siendo limitado únicamente por la profundidad de anidamiento y la pila del parser.

---
