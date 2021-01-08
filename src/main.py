from src.Grammar import Grammar
from src.Parser import Parser
from src.ParserOutput import ParserOutput
from src.scanner import Scanner
import json

scanner=Scanner("Auxiliars/tokens.in")
pif,st,message=scanner.scan(path='Programs/p1')
if message=='lexically correct':
    pifParser=pif[:]
    for i in pifParser:
        if i[0]==' ' or i[0]=='\n':
            pifParser.remove(i)

    for i in range(len(pifParser)):
        pifParser[i]=pifParser[i][0]

    grammar=Grammar('Auxiliars/g2.txt')
    grammar.readGrammar()
    parser=Parser(grammar)
    parserOutput=ParserOutput(parser=parser,input=pifParser)
    if parserOutput.tree!=None:
      parserOutput.printDS()
      parserOutput.writeFile("out.txt")

else:
    print(message)
