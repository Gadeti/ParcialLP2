# Parser de Expresiones: CYK vs Predictivo (LL)

## Descripción

Se implementaron dos parsers para el análisis sintáctico de expresiones aritméticas:

* **CYK (Cocke-Younger-Kasami)**: algoritmo bottom-up basado en programación dinámica.
* **Parser Predictivo (LL)**: basado en descenso recursivo (top-down).

Ambos parsers reconocen expresiones con:

* Suma (`+`)
* Resta (`-`)
* Multiplicación (`*`)
* División (`/`)
* Paréntesis

---

## Gramática utilizada

### Gramática original

```
E → E + T | E - T | T
T → T * F | T / F | F
F → ( E ) | num
```

---

### Forma Normal de Chomsky (CNF)

```
E → E X | T
X → OP1 T
OP1 → + | -

T → T Y | F
Y → OP2 F
OP2 → * | /

F → L Z | NUM
Z → E R

L → (
R → )
NUM → num
```

---

## Ejecución

### Ejecutar parser CYK

```
python cyk.py
```

Salida:

```
Entrada: num - num * num / num
Resultado: ACEPTADA
Tiempo: 0.00008 s
```

---

### Ejecutar parser predictivo

```
python predictivo.py
```

Salida:

```
Entrada: num - num * num / num
Resultado: ACEPTADA
Tiempo: 0.00002 s
```

---

### Ejecutar comparación con gráfica

```
python comparacion.py
```

Este script:

* Genera expresiones combinando operadores `+ - * /`
* Ejecuta pruebas con diferentes tamaños de entrada
* Mide tiempos de ejecución
* Genera una gráfica comparativa con `matplotlib`

Salida en consola:

```
Tamaño 5 → CYK: 0.0021s | LL: 0.0003s
Tamaño 9 → CYK: 0.0060s | LL: 0.0004s
Tamaño 13 → CYK: 0.0125s | LL: 0.0006s
```

Se mostrará una gráfica donde:

* Eje X: tamaño de la entrada (número de tokens)
* Eje Y: tiempo de ejecución (segundos)
* Se comparan ambas curvas (CYK vs Predictivo LL)

---

## Casos de prueba utilizados

```
Caso 1: ["num", "+", "num"]

Caso 2: ["num", "-", "num", "*", "num"]

Caso 3: ["(", "num", "+", "num", ")", "*", "num", "/", "num"]
```

---

## ⏱️ Resultados experimentales

| Tamaño de entrada | CYK (s) | Predictivo LL (s) |
| ----------------- | ------- | ----------------- |
| 5 tokens          | 0.0021  | 0.0003            |
| 9 tokens          | 0.0060  | 0.0004            |
| 13 tokens         | 0.0125  | 0.0006            |

---

## Análisis

* El parser CYK presenta crecimiento cúbico, aumentando rápidamente el tiempo conforme crece la entrada.
* El parser predictivo mantiene tiempos bajos y estables incluso con mayor número de tokens.
* La inclusión de más operadores no afecta significativamente al parser LL, pero sí incrementa el costo en CYK.
* La diferencia de rendimiento se amplía a medida que aumenta el tamaño de la entrada.

---

## Conclusiones

* CYK tiene complejidad **O(n³)**, lo que impacta directamente su rendimiento.
* El parser predictivo tiene complejidad **O(n)**, siendo mucho más eficiente.
* En pruebas realizadas, el parser LL fue entre **10x y 20x más rápido**.
* Para expresiones aritméticas completas (con múltiples operadores), CYK resulta poco eficiente.
* El uso de CYK se justifica en contextos donde la generalidad de la gramática es prioritaria sobre el rendimiento.

---
