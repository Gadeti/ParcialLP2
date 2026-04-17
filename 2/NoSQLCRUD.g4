grammar NoSQLCRUD;

/** 1. ESTRUCTURA DEL PROGRAMA **/
// El análisis sintáctico permite decidir si una cadena pertenece a la GIC [2]
program : instruccion+ EOF ;

instruccion 
    : crear 
    | leer 
    | actualizar 
    | borrar 
    ;

/** 2. OPERACIONES CRUD **/
crear      : 'INSERT' 'INTO' ID 'VALUES' objeto ;
leer       : 'FIND' 'IN' ID 'WHERE' filtro ;
actualizar : 'UPDATE' ID 'SET' objeto 'WHERE' filtro ;
borrar     : 'REMOVE' 'FROM' ID 'WHERE' filtro ;

/** 3. MANEJO DE DATOS (ASA: Derivación de Listas) **/
// Basado en el ejemplo 'int a,b,c;' para acumular tokens de atributos [2]
objeto : '{' listaAtributos? '}' ;

listaAtributos 
    : par (',' par)* 
    ;

par : ID ':' valor ;

valor 
    : STRING 
    | NUMBER 
    | BOOLEAN 
    | objeto 
    ;

/** 4. JERARQUÍA DE FILTROS (Precedencia y Asociatividad) **/
// Se implementan niveles para evitar ambigüedad en el análisis lineal [2]
filtro 
    : filtro '||' terminoAnd  // Nivel 1: Menor precedencia (OR)
    | terminoAnd
    ;

terminoAnd 
    : terminoAnd '&&' comparacion // Nivel 2: Precedencia media (AND)
    | comparacion
    ;

comparacion 
    : ID OP_REL valor // Nivel 3: Mayor precedencia (Relacional)
    | '(' filtro ')' 
    ;

/** 5. ESPECIFICACIÓN LÉXICA **/
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING  : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;
NUMBER  : [1, 2]+ ('.' [1, 2]+)? ;
BOOLEAN : 'true' | 'false' ;
OP_REL  : '==' | '!=' | '>' | '<' | '>=' | '<=' ;
WS      : [ \t\r\n]+ -> skip ; 

/******************************************************************
 * BLOQUE DE PRUEBAS AUTOMATIZABLES (Casos de Éxito y Error)
 * Siguiendo el proceso de validación del Analizador Sintáctico [2]
 ******************************************************************
 * PRUEBA SINTÁCTICA 1: Inserción con Objeto Complejo
 * Entrada: INSERT INTO clientes VALUES { nombre: "Juan", edad: 25 }
 * Resultado Esperado: ÉXITO. Valida reducción de listaAtributos.
 *
 * PRUEBA SINTÁCTICA 2: Consulta con Precedencia Booleana
 * Entrada: FIND IN stock WHERE precio > 100 && activo == true
 * Resultado Esperado: ÉXITO. El ASA debe evaluar '>' antes que '&&'. [2]
 *
 * PRUEBA SINTÁCTICA 3: Error por Falta de Tokens (Falta coma)
 * Entrada: INSERT INTO col VALUES { a:1 b:2 }
 * Resultado Esperado: ERROR. Reporte de error: "Falta ',' entre pares". [2]
 *
 * PRUEBA SINTÁCTICA 4: Expresión No Válida (Filtro incompleto)
 * Entrada: FIND IN productos WHERE precio > 
 * Resultado Esperado: ERROR. Reporte: "No es una expresión válida". [2]
 ******************************************************************/
