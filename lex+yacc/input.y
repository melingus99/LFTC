%{
#include <stdio.h>
#include <stdlib.h>
#define YYDEBUG 1

%}

%union {
  	int l_val;
	char *p_val;
}

%token <p_val> INT_CT
%token <p_val> STRING_CT

%token BOOL
%token STRING
%token INT
%token EQ
%token IF
%token ELSE
%token FOR
%token WHILE
%token TRUE
%token FALSE
%token BREAK
%token END
%token INPUT
%token IN
%token PRINT
%token CONST
%token VOID
%token MAIN

%token IDENTIFIER



%left '+' '-'
%left '%' '*' '/'
%left OR
%left AND

%%
program: VOID MAIN '(' declist ')' ':' cmpstmt
    | VOID MAIN '(' ')' ':' cmpstmt
    ;
declist: declaration
    | declaration ',' declist
    ;
declaration: type IDENTIFIER
    ;
type1: BOOL
    | STRING
    | INT
    ;
array: type IDENTIFIER '[' INT_CT ']'
    | type IDENTIFIER '[' ']'
    ;
type: type1
    | array
    ;
cmpstmt: stmtlist END ';'
stmtlist: stmt
    | stmt ';' stmtlist
    ;
stmt: simplstmt
    | structstmt
    | declist
    ;
simplstmt: assignstmt
    | iostmt
    ;
assignstmt: IDENTIFIER '=' expression
    | IDENTIFIER '+=' expression
    | IDENTIFIER '-=' expression
    | IDENTIFIER '*=' expression
    | IDENTIFIER '/=' expression
    ;
expression: expression '+' term
    | expression '-' term
    | expression '*' term
    | expression '/' term
    | term
    ;
term: term '*' factor
    | factor
    ;
factor: '(' expression ')'
    | IDENTIFIER
    ;
iostmt: IDENTIFIER '=' INPUT '(' ')'
    | PRINT '(' IDENTIFIER ')'
    ;
structstmt: cmpstmt
    | ifstmt
    | whilestmt
    | forstmt
    ;
ifstmt: IF '(' condition ')' ':' stmt END
    | IF '(' condition ')' ':' stmt END ELSE stmt
    ;
whilestmt: WHILE '(' condition ')' ':' stmt END
    ;
forstmt : FOR '(' type1 IDENTIFIER IN IDENTIFIER ')' ':' stmt
    ;
condition: expression relation expression
    | expression relation expression AND expression relation expression
    | expression relation expression OR expression relation expression
    ;
relation: '<'
    | '<='
    | 'EQ'
    | '!='
    | '>='
    | '>'
    ;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}

