class Parser:
  #preconditions:grammar needs to be a viable Grammar class
  #postconditions
  #input:grammar- Grammar
  #output:
  def __init__(self,grammar):
    self.grammar=grammar
    self.start= ('x',[self.grammar.start], 0)
    self.table={}

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
    i=1
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

  #preconditions:
  #postconditions:
  #input:
  #output:self.table- a dictionary with states as key and tuple of action and GOTO
  def makeTable(self):
    cancol=self.CanonicalCollection()
    for state in cancol:
        if cancol[state][0][2]!=len(cancol[state][0][1]):
          self.table[state]=('shift',{})
          for item in cancol[state]:
            newItem = (item[0], item[1], item[2] + 1)
            for state2 in cancol:
              if newItem in cancol[state2]:
                self.table[state][1][item[1][item[2]]]=state2

        elif cancol[state][0][2]==1 and cancol[state][0][1]==['S']:
          self.table[state]=('accept',{})

        elif cancol[state][0][2]==len(cancol[state][0][1]):
          i=0
          for prod in self.grammar.P:
            if cancol[state][0][0]!=prod:
              i+=len(self.grammar.P[prod])
            else:
              for item in self.grammar.P[prod]:
                if item!=cancol[state][0][1]:
                  i+=1
                else:
                  self.table[state]=('reduce '+str(i),{})
        else:
          self.table[state]=('error',{})
    try:
      self.checkConflicts(cancol)
    except:
      print("exception")

    return self.table

  #preconditions:
  #postconditions
  #input:canCol- canonical collection, dictionary of states and closures
  #output:
  def checkConflicts(self, canCol):
    for state in canCol:
      for item in canCol[state]:
        finalExists = False
        if item[2] == len(item[1]): # if . is at the end
          if finalExists:
            raise Exception("reduce-reduce confilct at state " + state)
          finalExists = True
        else:
          if finalExists == True:
            raise Exception("shift-reduce conflict at state " + state)

  #preconditions:
  #postconditions
  #input:i- int representing the number of production
  #output:
  def getProdAtIndex(self,i):
    for lhp in self.grammar.P:
      for rhp in self.grammar.P[lhp]:
        if i == 0:
          return (lhp, rhp)
        else:
           i -= 1
    raise Exception("invalid index")

  #preconditions:w elements must be from the grammar.Sigma
  #postconditions
  #input:w- list of strings
  #output:
  def parse(self, w):
    self.makeTable()
    state = "s0"
    alpha = ["s0"]
    beta = w
    phi = []
    while True:
      action = self.table[state][0]
      if action == "shift":
        a = beta[0]
        beta = beta[1:]
        state = str(self.table[state][1][a])
        alpha.extend([a, str(state)])
      elif "reduce" in action:
        lhp, rhp = self.getProdAtIndex(int(action.replace("reduce ", "")))
        while alpha[-2] != rhp[0]:
          alpha.pop()
          alpha.pop()
        alpha.pop()
        alpha.pop()

        state = str(self.table[alpha[-1]][1][lhp[0]])
        alpha.extend([lhp[0], str(state)])
        phi = [int(action.replace("reduce ", ""))] + phi
      elif action == "accept":
        return phi
      elif action == "error":
        return None

