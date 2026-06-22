/* 01. Write a lex program to recognize telephone operators in Bangladesh. */
%{
#include<stdio.h>
%}
%%
"013"[0-9]{8} {printf("Grameenphone: %s\n", yytext);}
"014"[0-9]{8} {printf("Banglalink: %s\n", yytext);}
"015"[0-9]{8} {printf("Teletalk: %s\n",yytext);}
"016"[0-9]{8} {printf("Airtel: %s\n",yytext);}
"017"[0-9]{8} {printf("Grameenphone: %s\n", yytext);}
"018"[0-9]{8} {printf("Robi: %s\n",yytext);}
"019"[0-9]{8} {printf("Banglalink: %s\n", yytext);}
.|\n ;
%%
int yywrap() {
    return 1;
}
int main() {
    yylex();
    return 0;
}
