
class Lab4():
    def __init__(self):
        f=open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\FA.in","r")
        self.DFA=True
        self.states=[]
        self.alphabet=[]
        self.finalState=""
        self.transitions={}
        for line in f.readlines():
            line=line.split(":")
            if(line[0]=='Q'):
                self.states=line[1].split(",")
                self.states[-1]=self.states[-1][0:-1]
            elif(line[0]=="sigma"):
                self.alphabet=line[1].split(",")
                self.alphabet[-1]=self.alphabet[-1][0:-1]
            elif(line[0]=="F"):
                self.finalState=line[1][0:-1]
            else:
                someStates=line[1].split(",")
                someStates[-1]=someStates[-1][0:-1]
                if len(someStates)>1:
                    self.DFA=False
                line[0]=line[0].split(",")
                self.transitions[(line[0][0],line[0][1])]=someStates
        f.close()
    def menu(self):
        while(True):
            print("1.Show set of states \n"
                  "2.Show alphabet \n"
                  "3.Show transitions \n"
                  "4.Show final state \n"
                  "5.Process seq \n"
                  "0. to exit \n")
            x=input("choose an option:")
            if(x=="1"):
                for i in self.states:
                    print(i,end=" ")
                print("\n")
            elif x=='2':
                for i in self.alphabet:
                    print(i,end=" ")
                print("\n")
            elif x=="3":
                for i in self.transitions:
                    str=""
                    for j in range(0,len(self.transitions[i])):
                        str+=self.transitions[i][j]+","
                    str=str[0:-1]
                    keys=""
                    for j in i:
                        keys+=j+","
                    keys=keys[0:-1]
                    print("delta(%s):{%s}" %(keys,str))
            elif x=='4':
                print(self.finalState)
            elif x=="5":
                if self.DFA==False:
                    print('not DFA')
                    continue

                f=open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\Sequence.in","r")

                seq=f.read()
                seq=seq.split(" ")
                seq[-1]=seq[-1][0:-1]
                state='q0'
                ok=1
                for i in seq:
                    key=(state,i)
                    try:
                        state=self.transitions[key][0]
                    except:
                        ok=0
                        break
                if state=='qf' and ok==1:
                    print("accepted")
                else:
                    print("not accepted")
            else:
                break

lab4=Lab4()
lab4.menu()



