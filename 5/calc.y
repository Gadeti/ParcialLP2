%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token TRUE FALSE AND OR NOT
%left OR
%left AND
%right NOT

%%

input:
    /* vacío */
    | input line
    ;

line:
    expr '\n'   { printf("Resultado: %d\n", $1); }
    ;

expr:
    TRUE            { $$ = 1; }
    | FALSE         { $$ = 0; }
    | expr AND expr { $$ = $1 && $3; }
    | expr OR expr  { $$ = $1 || $3; }
    | NOT expr      { $$ = !$2; }
    | '(' expr ')'  { $$ = $2; }
    ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}
