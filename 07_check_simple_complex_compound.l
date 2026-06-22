/* 07. Write a lex program to identify whether a given sentence is simple/ complex/ compound. */

%{ 
#include <stdio.h> 
int has_complex = 0;
int has_compound = 0;
%} 
COMPLEX_KEYWORDS that|since|because|although|if|when|while|unless|until|after|before
COMPOUND_KEYWORDS and|or|but 
%% 
{COMPLEX_KEYWORDS} { has_complex = 1; } 
{COMPOUND_KEYWORDS} { has_compound = 1; } 
\n { 
    if (has_complex && has_compound)
        printf("Compound-Complex Sentence\n");
    else if (has_complex)
        printf("Complex Sentence\n");
    else if (has_compound)
        printf("Compound Sentence\n");
    else
        printf("Simple Sentence\n");
    has_complex = 0;
    has_compound = 0;
}
. ; 
%% 
int yywrap() { 
    return 1; 
} 
int main() { 
    yylex(); 
    return 0; 
}