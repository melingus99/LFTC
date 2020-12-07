# from src.scanner import Scanner
# scanner=Scanner("C:\\Users\\Bubu\\LFTC\\Auxiliars\\tokens.in")
#
# pif,st,message=scanner.scan("C:\\Users\\Bubu\\LFTC\\Programs\\p3")
# print(message)
# print('Symbol Table: ',str(st.table))
# print('PIF: '+str(pif))
#
# pif,st,message=scanner.scan("C:\\Users\\Bubu\\LFTC\\Programs\\p1err")
#
# print(message)
# print('Symbol Table: ',str(st.table))
# print('PIF: '+str(pif))

# f=open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\test.txt","w")
# letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
# letters=letters.split(' ')
# digits='0 1 2 3 4 5 6 7 8 9'
# digits=digits.split(' ')
# for letter in letters:
#     f.write("q5,{}:q5,q6\n".format(letter))
from src.Parser import Parser

class Grammar:
  #preconditions:path-a viable path to a file
  #postconditions
  #input:path-string
  #output:
  def __init__(self,path):
    self.Sigma=[]
    self.N=[]
    self.P={}
    self.start=''
    self.file=open(path,'r')

 #preconditions:
  #postconditions
  #input:
  #output:
  def readGrammar(self):
    lines = self.file.readlines()
    self.N = lines[1].split(' ')
    self.N[-1]=self.N[-1][0:-1]
    self.Sigma=lines[2].split(' ')
    self.Sigma[-1]=self.Sigma[-1][0:-1]
    self.start=lines[3]
    self.start=self.start[0:-1]
    lines=lines[4:]
    for line in lines:
      line=line.split(" -> ")
      if line[0] in self.P:
        line[1]=line[1][0:-1]
        self.P[line[0]].append(line[1].split(' '))
      else:
        line[1]=line[1][0:-1]
        self.P[line[0]]=[line[1].split(' ')]

 #preconditions:readGrammar needs to be called before calling this function
  #postconditions
  #input:
  #output:
  def printN(self):
    print('N',end=':')
    for i in self.N:
      print(i,end=' ')
    print()
  #preconditions:readGrammar needs to be called before calling this function
  #postconditions
  #input:
  #output:
  def printSigma(self):
    print('Sigma',end=':')
    for i in self.Sigma:
      print(i,end=' ')
    print()
  #preconditions:readGrammar needs to be called before calling this function
  #postconditions
  #input:
  #output:
  def printP(self):
    print('P',end=':')
    print('\t')
    for i in self.P:
      print(i+'->',end='')
      for j in self.P[i]:
        print(j+'|',end='')
      print('\t')

  #preconditions:readGrammar needs to be called before calling this function
  #postconditions
  #input:
  #output:
  def printP_N(self,n):
    print(n+'->',end='')
    for j in self.P[n]:
      print(j+'|',end='')

g=Grammar('C:\\Users\\Bubu\\LFTC\\Auxiliars\\g2.txt')
g.readGrammar()

# g.printN()
# g.printSigma()
# g.printP()
# g.printP_N('expression')
#g.printP_N('program')
parser=Parser(g)
#closure=parser.closure([('x', 'S', 0)])
#print(closure)
#goto1=parser.goto(closure,'a')
#print(goto1)
c=parser.CanonicalCollection()
for i in c:
    print(i,c[i])

