class Parser:
  #preconditions:grammar needs to be a viable Grammar class
  #postconditions
  #input:grammar- Grammar
  #output:
  def __init__(self,grammar):
    self.grammar=grammar
    self.start= ('x',[self.grammar.start], 0)

  #preconditions
  #postconditions
  #input: setItems - list of LR(0) items
  #output: C - list of LR(0) items
  def closure(self,setItems):
    C = setItems
    flag = 1
    while flag == 1:
      flag=0
      for it in C:
        # print(it)
        if it[2] == len(it[1]):
          if it not in C:
            C.append(it)
          continue
        gs=it[1][it[2]]
        if gs in self.grammar.N:
          for prod in self.grammar.P[gs]:
            new_item=(gs, prod, 0)
            if new_item not in C:
              C.append(new_item)
              flag = 1
    return C

  #preconditions
  #postconditions
  #input: setItems - list of LR(0) items, symbol - terminal or non-terminal
  #output: C - list of LR(0) items
  def goto(self,setItems,symbol):
    cl = []
    for item in setItems:
      if item[2] == len(item[1]):
        continue
      if item[1][item[2]] == symbol:
        cl.append((item[0], item[1], item[2] + 1))
    return self.closure(cl)

  #preconditions:
  #postconditions
  #input:
  #output:C-map of state and LR(0) items
  def CanonicalCollection(self):
    C = []
    c={}
    s0 = self.closure([self.start])
    c['s0']=s0
    C.extend(s0)
    flag = 1
    i=0
    while flag:
      flag = 0
      for item in C:
        for symbol in self.grammar.N + self.grammar.Sigma:
          gt = self.goto([item], symbol)
          if len(gt) != 0 and gt[0] not in C:
            c['s'+str(i)]=gt
            i+=1
            C.extend(gt)
            flag=1
    return c
