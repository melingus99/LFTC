class Tree():
  #preconditions:
  #postconditions
  #input:root- Node
  #output:
  def __init__(self,root=None):
    self.root=root

  #preconditions:
  #postconditions
  #input:node- Node
  #output:
  def addNode(self,node):
    if self.root==None:
      self.root=node
    else:
      self.root.addChild()

  #preconditions:
  #postconditions:
  #input:
  #output:finalList- list of tuples(index of the node,value, father index, brother index)
  def breadthSearch(self):
    finalList=[]
    list=[]
    index=0
    list.append(self.root)
    while len(list)!=0:
      list.extend(list[0].childrens)
      list[0].index=index
      if list[0].father!=None:
        if list[0].brother!=None:
          finalList.append((index,list[0].value,list[0].father.index,list[0].brother.index))
        else:
          finalList.append((index,list[0].value,list[0].father.index,None))
      else:
        finalList.append((index,list[0].value,None,None))
      list.pop(0)
      index+=1
    return finalList;



class Node():

  #preconditions:
  #postconditions:
  #input:value-Value of the Node
  #output:
  def __init__(self,value=-1):
    self.value=value
    self.brother=None
    self.father=None
    self.index=None
    self.childrens=[]


  #preconditions:
  #postconditions:
  #input:value- the new value of the Node
  #output:
  def setValue(self,value):
    self.value=value


  #preconditions:
  #postconditions
  #input:node- Node
  #output:
  def addChild(self,node):
    self.childrens.append(node)
    node.father=self
    length=len(self.childrens)

    if length>1:
      node.brother=self.childrens[length-2]

  
