grammar Enquestes;

chatboot: (preguntas|respuesta|item|alternative|enque)+;

preguntas: IDPREGUNTA TP PREGUNTA (PARAULA)+ INTERROGANTE;

respuesta: IDRESPUESTA TP RESPOSTA respuestas;

respuestas: (NUM TP (PARAULA)+ PC)+;

item: IDITEM TP ITEM IDPREGUNTA EDGE IDRESPUESTA;

alternative: IDALTER TP ALTERNATIVA IDITEM AC alter (COMA alter)* CC;

alter: AP NUM COMA IDITEM CP;

enque: PARAULA TP ENQUESTA (IDITEM)+ END;

EDGE: '->';
PC: ';';
TP: ':';
AP: '(';
CP: ')';
AC: '[';
CC: ']';
COMA: ',';
NUM: [0-9]+;
END: 'END';
IDALTER: 'A'[0-9]+;
ALTERNATIVA: 'ALTERNATIVA';
ENQUESTA: 'ENQUESTA';
IDRESPUESTA: 'R'[0-9]+;
RESPOSTA: 'RESPOSTA';
IDPREGUNTA: 'P'[0-9]+;
INTERROGANTE: '?';
PREGUNTA: 'PREGUNTA';
IDITEM: 'I'[0-9]+;
ITEM: 'ITEM';
PARAULA: [a-zA-Z][a-zA-Z0-9\u0080-\u00FF]*;
WS : [ \t\r\n\f]+ -> skip;