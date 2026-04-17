grammar NoSQLCRUD;

/** 1. ESTRUCTURA DEL PROGRAMA **/
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

/** 3. MANEJO DE DATOS (Derivación de Listas) **/
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
filtro
    : filtro '||' terminoAnd   // Nivel 1: Menor precedencia (OR)
    | terminoAnd
    ;

terminoAnd
    : terminoAnd '&&' comparacion  // Nivel 2: Precedencia media (AND)
    | comparacion
    ;

comparacion
    : ID OP_REL valor          // Nivel 3: Mayor precedencia (Relacional)
    | '(' filtro ')'
    ;

/** 5. ESPECIFICACIÓN LÉXICA **/
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING  : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
BOOLEAN : 'true' | 'false' ;
OP_REL  : '==' | '!=' | '>' | '<' | '>=' | '<=' ;
WS      : [ \t\r\n]+ -> skip ;
