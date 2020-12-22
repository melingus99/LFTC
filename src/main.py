from src.Grammar import Grammar
from src.Parser import Parser
from src.ParserOutput import ParserOutput
from src.scanner import Scanner
import json
g=Grammar('C:\\Users\\Bubu\\LFTC\\Auxiliars\\g1.txt')
g.readGrammar()
parser=Parser(g)
da = parser.makeTable()
f = open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\seq.txt", "r")
parserOutput = ParserOutput(parser,list(f.read()))
if parserOutput.tree!=None:
    parserOutput.printDS()
    parserOutput.writeFile("C:\\Users\\Bubu\\LFTC\\Auxiliars\\out1.txt")


# scanner=Scanner("C:\\Users\\Bubu\\LFTC\\Auxiliars\\tokens.in")
# pif,st,message=scanner.scan("C:\\Users\\Bubu\\LFTC\\Programs\\p1")
#
# f=open('C:\\Users\\Bubu\\LFTC\\Auxiliars\\pif.out','w')
# json.dump(pif,f)
