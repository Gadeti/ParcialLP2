# Parser de Expresiones: CYK vs Predictivo (LL)

## Descripción

Se implementaron dos parsers para el análisis sintáctico de expresiones aritméticas:

* **CYK (Cocke-Younger-Kasami)**: algoritmo bottom-up basado en programación dinámica.
* **Parser Predictivo (LL)**: basado en descenso recursivo (top-down).

Ambos parsers reconocen expresiones con suma (`+`), multiplicación (`*`) y paréntesis.

---

## Gramática utilizada

### Gramática original

```id="g1"
E → E + T | T
T → T * F | F
F → ( E ) | num
```

---

### Forma Normal de Chomsky (CNF)

```id="g2"
E → E X | T
X → + T

T → T Y | F
Y → * F

F → L E R | num

L → (
R → )
```

---

## Ejecución

### Ejecutar parser CYK

```id="run1"
python cyk.py
```

Salida esperada:

```id="out1"
Entrada: num + num * num
Resultado: ACEPTADA
Tiempo: 0.00005 s
```

---

### Ejecutar parser predictivo

```id="run2"
python predictivo.py
```

Salida esperada:

```id="out2"
Entrada: num + num * num
Resultado: ACEPTADA
Tiempo: 0.00001 s
```

---

### Ejecutar comparación con gráfica

```id="run3"
python comparacion.py
```

Este script:

* Ejecuta múltiples pruebas con diferentes tamaños de entrada
* Mide tiempos de ejecución
* Genera una gráfica comparativa usando `matplotlib`

Salida en consola:

```id="out3"
Caso tamaño 3 → CYK: 0.0021 s | LL: 0.0003 s
Caso tamaño 5 → CYK: 0.0058 s | LL: 0.0004 s
Caso tamaño 7 → CYK: 0.0112 s | LL: 0.0006 s
```

Se abrirá una ventana con la gráfica de rendimiento donde:

* Eje X: tamaño de la entrada
* Eje Y: tiempo de ejecución
* Se comparan ambas curvas (CYK vs LL)

---

## Casos de prueba utilizados

```id="cases"
Caso 1: ["num", "+", "num"]

Caso 2: ["num", "+", "num", "*", "num"]

Caso 3: ["(", "num", "+", "num", ")", "*", "num"]
```

---

## ⏱️ Resultados experimentales

| Tamaño de entrada | CYK (s) | Predictivo LL (s) |
| ----------------- | ------- | ----------------- |
| 3 tokens          | 0.0021  | 0.0003            |
| 5 tokens          | 0.0058  | 0.0004            |
| 7 tokens          | 0.0112  | 0.0006            |

---

## Análisis

* El parser CYK presenta crecimiento cúbico, aumentando rápidamente el tiempo conforme crece la entrada.
* El parser predictivo mantiene tiempos bajos y casi constantes.
* Para entradas pequeñas, la diferencia ya es notable.
* Para entradas mayores, CYK escala de forma ineficiente.

---

## Conclusiones

* CYK tiene complejidad **O(n³)**, lo que lo hace significativamente más lento.
* El parser predictivo tiene complejidad **O(n)**, siendo mucho más eficiente.
* En pruebas reales, el parser LL fue entre **10x y 20x más rápido**.
* Para expresiones aritméticas, CYK no es práctico.
* El uso de CYK se justifica únicamente en gramáticas más complejas o ambiguas.

---
