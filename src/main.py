from src.Grammar import Grammar
from src.Parser import Parser
from src.ParserOutput import ParserOutput

g=Grammar('C:\\Users\\Bubu\\LFTC\\Auxiliars\\g1.txt')
g.readGrammar()
parser=Parser(g)
f = open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\w.txt", "r")
parserOutput = ParserOutput(parser,list(f.read()))
if parserOutput.tree!=None:
    parserOutput.printDS()
    parserOutput.writeFile("C:\\Users\\Bubu\\LFTC\\Auxiliars\\out.txt")
