
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     INT_CT = 258,
     STRING_CT = 259,
     BOOL = 260,
     STRING = 261,
     INT = 262,
     EQ = 263,
     IF = 264,
     ELSE = 265,
     FOR = 266,
     WHILE = 267,
     TRUE = 268,
     FALSE = 269,
     BREAK = 270,
     END = 271,
     INPUT = 272,
     IN = 273,
     PRINT = 274,
     CONST = 275,
     VOID = 276,
     MAIN = 277,
     IDENTIFIER = 278,
     OR = 279,
     AND = 280
   };
#endif
/* Tokens.  */
#define INT_CT 258
#define STRING_CT 259
#define BOOL 260
#define STRING 261
#define INT 262
#define EQ 263
#define IF 264
#define ELSE 265
#define FOR 266
#define WHILE 267
#define TRUE 268
#define FALSE 269
#define BREAK 270
#define END 271
#define INPUT 272
#define IN 273
#define PRINT 274
#define CONST 275
#define VOID 276
#define MAIN 277
#define IDENTIFIER 278
#define OR 279
#define AND 280




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 1676 of yacc.c  */
#line 8 "input.y"

  	int l_val;
	char *p_val;



/* Line 1676 of yacc.c  */
#line 109 "y.tab.h"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


