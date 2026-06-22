/* 02. Write a lex program to count the characters, words and lines in a given C program. */

%{ 
#include <stdio.h> 
int char_count = 0, word_count = 0, line_count = 0; 
%} 
%% 
[a-zA-Z0-9_]+ { word_count++; char_count += yyleng; } 
\n { char_count++; line_count++; } 
. { char_count++; } 
%% 
int yywrap() { 
    return 1; 
} 
int main(int argc, char *argv[]) { 
    if (argc > 1) { 
        yyin = fopen(argv[1], "r"); 
        if (!yyin) { 
            printf("Error: Cannot open file %s\n", argv[1]); 
            return 1; 
        } 
    } 
    yylex(); 
    printf("Characters: %d\nWords: %d\nLines: %d\n", char_count, 
word_count, line_count); 
    if (yyin != stdin) fclose(yyin); 
    return 0; 
}