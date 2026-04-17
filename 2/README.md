# DSL NoSQL-CRUD Grammar

Gramática formal diseñada con **ANTLR4** para realizar operaciones CRUD sobre bases de datos no relacionales. Define un lenguaje de dominio específico (DSL) con sintaxis estructurada, jerarquía de precedencia lógica y validación léxica completa.

---

## Operaciones soportadas

| Operación | Sintaxis |
| :--- | :--- |
| **Insertar** | `INSERT INTO <colección> VALUES { ... }` |
| **Consultar** | `FIND IN <colección> WHERE <filtro>` |
| **Actualizar** | `UPDATE <colección> SET { ... } WHERE <filtro>` |
| **Eliminar** | `REMOVE FROM <colección> WHERE <filtro>` |

---

## Ejemplos de uso

```
INSERT INTO clientes VALUES { nombre: "Juan", edad: 25 }

FIND IN stock WHERE precio > 100 && activo == true

UPDATE usuarios SET { activo: false } WHERE rol == "invitado"

REMOVE FROM logs WHERE nivel == "debug" || nivel == "info"
```

---

## Estructura de la gramática

La gramática se organiza en cinco bloques principales dentro de `NoSQLCRUD.g4`:

- **Programa:** acepta una o más instrucciones secuenciales (`instruccion+`).
- **Operaciones CRUD:** cada comando mapea directamente a una regla de producción.
- **Objetos:** estructura JSON-like con derivación recursiva de listas de pares `clave: valor`.
- **Filtros:** tres niveles de precedencia para evitar ambigüedad: `||` (menor) → `&&` (media) → operadores relacionales (mayor), todos con asociatividad por la izquierda.
- **Léxico:** tokens para identificadores, literales, operadores relacionales y manejo de espacios en blanco.

---

## Casos de prueba

| # | Entrada | Resultado esperado |
| :---: | :--- | :--- |
| 1 | `INSERT INTO clientes VALUES { nombre: "Juan", edad: 25 }` | ✅ ÉXITO — valida reducción de `listaAtributos` |
| 2 | `FIND IN stock WHERE precio > 100 && activo == true` | ✅ ÉXITO — `>` se evalúa antes que `&&` |
| 3 | `INSERT INTO col VALUES { a:1 b:2 }` | ❌ ERROR — falta `,` entre pares |
| 4 | `FIND IN productos WHERE precio >` | ❌ ERROR — filtro incompleto, expresión no válida |

---

## Requisitos

- [ANTLR4](https://www.antlr.org/) `>= 4.13`
- Python `>= 3.10` con `antlr4-python3-runtime`

```bash
pip install antlr4-python3-runtime
antlr4 -Dlanguage=Python3 NoSQLCRUD.g4
```
