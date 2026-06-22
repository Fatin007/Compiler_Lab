/* 05. Write a lex program to recognize and count all of the identifiers in a C program */
%{ 
#include <stdio.h> 
#include <string.h> 
int count = 0; 
%} 
IDENTIFIER [a-zA-Z_][a-zA-Z0-9_]* 
KEYWORD int|float|char|double|long|short|void|return|if|else|while|for|do|switch|case|break|continue|struct|union|typedef 
%% 
{KEYWORD} {} 
{IDENTIFIER} { count++; printf("Identifier: %s\n", yytext); } 
.|\n ;
%% 
int yywrap() { 
    return 1; 
} 
int main() { 
    yylex(); 
    printf("\nTotal Identifiers: %d\n", count); 
    return 0; 
}