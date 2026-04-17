Descripción: Instrucciones completas para el uso y compilación del procesador de lenguaje.
# Procesador de Lenguaje NoSQL-CRUD

Este proyecto implementa un analizador sintáctico para un lenguaje de dominio específico (DSL) orientado a bases de datos NoSQL, siguiendo el modelo de estudio del lenguaje KAFE [2].

## 📋 Características
- **Diseño Natural:** Refleja la semántica de operaciones CRUD en el árbol de derivación [1].
- **Manejo de Prioridades:** Implementa niveles de precedencia para operadores lógicos y relacionales [1].
- **Asociatividad:** Garantiza el agrupamiento correcto de izquierda a derecha [1].

## 🛠️ Requisitos
Al igual que KAFE, este proyecto requiere:
- **ANTLR4** (Generador de analizadores).
- **Python 3.x** o **Java Runtime**.

## 🚀 Compilación e Instalación
Siga estos pasos para generar el analizador:

1. **Generar los archivos del Parser y Lexer:**
   ```bash
   antlr4 NoSQLCRUD.g4 -Dlanguage=Python3
(O use Java si prefiere ese entorno).
Probar la gramática visualmente (Requiere Java):
🧪 Ejemplo de Uso
Introduzca la siguiente sentencia para validar el funcionamiento:
FIND IN empleados WHERE salario > 2000 && departamento == "ventas"
El analizador reconstruirá la inversa de una derivación por la derecha (ASA) para validar que la sintaxis es correcta antes de proceder a la traducción
.
