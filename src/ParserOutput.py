from src.Tree import Node,Tree
class ParserOutput:
  #preconditions:
  #postconditions:
  #input:parser- of type Parser
        #input - list of strings
  #output:
  def __init__(self,parser,input):
    self.parser=parser
    try:
      self.tree=self.buildTree(parser.parse(input))
    except Exception as e:
      print(e)
      self.tree=None

  #preconditions:
  #postconditions:
  #input:input-a list of numbers corresponding to the index of production
  #output:tree- a father, sibling relation tree DS
  def buildTree(self,input):
    i=0
    lhp,rhp=self.parser.getProdAtIndex(input[i])
    root=Node(lhp)
    for symbol in rhp:
      root.addChild(Node(symbol))
    i+=1
    self.Util(root,i,input)
    tree=Tree(root)
    return tree

  #preconditions:i<=len(input)
  #postconditions:
  #input:node-Node to be processed,
        #i- index of the production
  #output:
  def Util(self,node,i,input):
    for children in node.childrens:
      if children.value in self.parser.grammar.N:
        lhp,rhp=self.parser.getProdAtIndex(input[i])
        for symbol in rhp:
          children.addChild(Node(symbol))
        i+=1
    for children in node.childrens:
      if children.value in self.parser.grammar.N:
        self.Util(children,i,input)

  #preconditions:tree must have been built
  #postconditions
  #input:
  #output:
  def printDS(self):
    for i in self.tree.breadthSearch():
      print("node: {}, Symbol: {}, Father: {}, Sibling: {}".format(i[0],i[1],i[2],i[3]))

  #preconditions:file must be a viable file path
  #postconditions
  #input:
  #output:
  def writeFile(self,file):
    f=open(file,"w")
    for i in self.tree.breadthSearch():
      f.write("node: {}, Symbol: {}, Father: {}, Sibling: {}\n".format(i[0],i[1],i[2],i[3]))
