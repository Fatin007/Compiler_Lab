/* 04. Write a lex program to identify and count the spaces and comments in a given C program. */
%{ 
#include<stdio.h> 
int comment = 0; 
int space = 0; 
%} 
%% 
[ \t]+ {space+=yyleng;} 
"//".* {comment++; } 
"/*"([^*]|\*+[^*/])*"*"+"/" {comment++; } 
\n ; 
. ; 
%% 
int yywrap() { 
    return 1; 
} 
int main() { 
    yylex(); 
    printf("No of Comment: %d\n",comment); 
    printf("No of Space: %d\n", space); 
    return 0; 
}