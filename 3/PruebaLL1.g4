grammar PruebaLL1;

// Un buen diseño permite que la traducción sea más sencilla [2]
program : s EOF ;

s : a 'a' a 'b'    # ReglaS1
  | b 'b' b 'a'    # ReglaS2
  ;

a : /* epsilon */ ;
b : /* epsilon */ ;

WS : [ \t\r\n]+ -> skip ;
