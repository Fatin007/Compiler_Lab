/* 06. Write a lex program to recognize "to be" verbs from a given paragraph. */
%{ 
#include<stdio.h> 
#include<string.h> 
int count = 0; 
%} 
TO_BE am|is|are|was|were|been|have|has|be 
%% 
{TO_BE} { count++; printf("To-Be Verb Found: %s\n", yytext); } 
.|\n ; 
%% 
int yywrap() { 
    return 1; 
} 
int main() { 
    yylex(); 
    printf("Total No of To-Be Verbs: %d\n", count); 
    return 0; 
} 