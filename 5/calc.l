%{
#include "y.tab.h"
%}

%%

"1"         { return TRUE; }
"0"         { return FALSE; }
"AND"       { return AND; }
"OR"        { return OR; }
"NOT"       { return NOT; }
"("         { return '('; }
")"         { return ')'; }

[ \t]       ;
\n          { return '\n'; }

.           { printf("Caracter inválido\n"); }

%%
