/* 10. C Lexical Analyzer */

%{
    #include<stdio.h>
    #include<stdlib.h>

    int keywords = 0, identifiers = 0, lines = 0;
    int punctuations = 0, operators = 0, multiOps = 0;
    int statements = 0;
%}

%x COMMENT
%x PREPROCESSOR

LETTER    [a-zA-Z_]
DIGIT     [0-9]
ID        {LETTER}({LETTER}|{DIGIT})*
INT       {DIGIT}+
FLOAT     ({DIGIT}+\.{DIGIT}*|{DIGIT}*\.{DIGIT}+)([eE][+-]?{DIGIT}+)?
CHAR      \'([^'\\\n]|\\.)+\'
STRING    \"([^"\\\n]|\\.)*\"
WS        [ \t\r]+

%%

    /* Preprocessor */
^"#"                { BEGIN(PREPROCESSOR); }
<PREPROCESSOR>\\\n  { lines++; }
<PREPROCESSOR>\n     { lines++; BEGIN(INITIAL); }
<PREPROCESSOR>.       { }

    /* Comments */
"/*"                 { BEGIN(COMMENT); }
<COMMENT>"*/"         { BEGIN(INITIAL); }
<COMMENT>\n           { lines++; }
<COMMENT>.            { }
"//".*                { }

    /* Keywords */
"auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|"double"|"else"|"enum"|"extern"|"float"|"for"|"goto"|"if"|"inline"|"int"|"long"|"register"|"restrict"|"return"|"short"|"signed"|"sizeof"|"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|"void"|"volatile"|"while"  { keywords++; }

    /* Constants & Identifiers */
{INT}       { }
{FLOAT}     { }
{STRING}    { }
{CHAR}      { }
{ID}        { identifiers++; }

    /* Operators */
"<<"|">>"|"<="|">="|"=="|"!="|"&&"|"||"|"++"|"--"|"->"|"+="|"-="|"*="|"/="|"%="|"&="|"|="|"^="|"<<="|">>="  { multiOps++; }

"+"|"-"|"*"|"/"|"%"|"&"|"|"|"^"|"~"|"!"|"<"|">"|"="|"?"|":"  { operators++; }

    /* Punctuation */
"("|")"|"{"|"}"|"["|"]"|","|"."  { punctuations++; }
";"                                   { statements++; }

{WS}    { }
\n      { lines++; }
.       { }

%%

int yywrap(void) { return 1; }

int main(int argc, char* argv[]) {
    if(argc < 2) {
        printf("Usage: %s <file.c>\n", argv[0]);
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if(!f) {
        printf("Cannot open: %s\n", argv[1]);
        return 1;
    }
    yyin = f;
    yylex();
    fclose(f);

    printf("\n=== Lexer Summary ===\n");
    printf("Lines:            %d\n", lines);
    printf("Keywords:         %d\n", keywords);
    printf("Identifiers:      %d\n", identifiers);
    printf("Operators (1-char): %d\n", operators);
    printf("Operators (2-char): %d\n", multiOps);
    printf("Punctuations:     %d\n", punctuations);
    printf("Statements:       %d\n", statements);
    return 0;
}

