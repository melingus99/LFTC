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
    self.start=self.start[-1][0:-1]
    lines=lines[4:]
    for line in lines:
      line=line.replace(' ','')
      line=line.split("->")
      if line[0] in self.P:
        line[1]=line[1][0:-1]
        self.P[line[0]].append(line[1])
      else:
        line[1]=line[1][0:-1]
        self.P[line[0]]=[line[1]]

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
