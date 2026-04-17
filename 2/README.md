# DSL NoSQL-CRUD — Implementación ANTLR4 + Python

Implementación de una gramática para operaciones CRUD sobre bases de datos no relacionales. Construida con **ANTLR4** y ejecutada con **Python**.

---

## Requisitos

- Python `>= 3.10`
- Java `>= 11`

```bash
pip install antlr4-python3-runtime==4.13.2
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

---

## Estructura del proyecto

```
NoSQLCRUD/
├── NoSQLCRUD.g4       # Gramática GIC con reglas CRUD
├── main.py            # Pruebas de análisis sintáctico
└── generated/         # Generado automáticamente por ANTLR4
    ├── NoSQLCRUDLexer.py
    ├── NoSQLCRUDParser.py
    └── NoSQLCRUDListener.py
```

---

## Ejecución

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -o generated NoSQLCRUD.g4 && python main.py
```

> La compilación con ANTLR4 solo es necesaria la primera vez, o cuando se modifique `NoSQLCRUD.g4`. Para ejecuciones posteriores basta con:
>
> ```bash
> python main.py
> ```

---

## Pruebas y salida esperada

### ✅ Prueba 1 — Inserción con objeto complejo
```
Entrada:  INSERT INTO clientes VALUES { nombre: "Juan", edad: 25 }
Salida:   [ÉXITO] Árbol sintáctico generado.
```

### ✅ Prueba 2 — Consulta con precedencia booleana
```
Entrada:  FIND IN stock WHERE precio > 100 && activo == true
Salida:   [ÉXITO] Árbol sintáctico generado.
```
> `precio > 100` se reduce antes que `&&`, confirmando la jerarquía de precedencia.

### ✅ Prueba 3 — Actualización con filtro OR
```
Entrada:  UPDATE usuarios SET { activo: false } WHERE rol == "invitado" || rol == "temporal"
Salida:   [ÉXITO] Árbol sintáctico generado.
```

### ✅ Prueba 4 — Eliminación simple
```
Entrada:  REMOVE FROM logs WHERE nivel == "debug"
Salida:   [ÉXITO] Árbol sintáctico generado.
```

### ❌ Prueba 5 — Error: falta coma entre pares
```
Entrada:  INSERT INTO col VALUES { a:1 b:2 }
Salida:   [ERROR] línea 1:20 → mismatched input 'b' expecting {',', '}'}
```

### ❌ Prueba 6 — Error: filtro incompleto
```
Entrada:  FIND IN productos WHERE precio >
Salida:   [ERROR] línea 1:32 → no viable alternative at input 'precio >'
```

---

## Gramática aplicada

| Concepto GIC | Regla en la gramática |
| :--- | :--- |
| Raíz del programa | `program → instruccion+ EOF` |
| Operaciones CRUD | `crear`, `leer`, `actualizar`, `borrar` |
| Derivación de listas | `listaAtributos → par (',' par)*` |
| Precedencia — nivel 1 (OR) | `filtro → filtro '\|\|' terminoAnd` |
| Precedencia — nivel 2 (AND) | `terminoAnd → terminoAnd '&&' comparacion` |
| Precedencia — nivel 3 (relacional) | `comparacion → ID OP_REL valor` |
