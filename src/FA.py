
class FA():
    #preconditions:
    #input:
    #output:
    def __init__(self,path):
        f=open(path,"r")
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
    #preconditions:
    #input:
    #output:message- if the given sequence is accepted or not by FA
            #states- list of states
            #alphabet -list of symbols
            #finalSate - list of final states
            #transitions - dictionary with key=(state,symbol) value=[states]
    def menu(self):
        while(True):
            print("1.Show set of states \n"
                  "2.Show alphabet \n"
                  "3.Show transitions \n"
                  "4.Show final state \n"
                  "5.Process seq \n"
                  "6.Process identifiers or constants\n"
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
                seq=list(seq)
                seq.remove('\n')
                state='q0'
                ok=1
                for i in seq:
                    key=(state,i)
                    try:
                        state=self.transitions[key][0]
                    except:
                        ok=0
                        break

                if state in self.finalState and ok==1:
                    print("accepted")
                else:
                    print("not accepted")
            elif x=="6":
                f=open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\Identifiers and Constants.in","r")
                token=f.read()
                print(self.isIntOrCt(token))
                f.close()

    #preconditions:token needs to be a string
    #input:token-string
    #output:True-the given token is accepted by the FA
            #False- the given token is not accepted by the FA
    def isIntOrCt(self,token):
        token=list(token)
        # token.remove('\n')
        state='q0'
        letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        letters=letters.split(' ')
        ok=1
        for i in range(len(token)):
            key=(state,token[i])
            try:
                if i==len(token)-1 and token[i] in letters:
                    state=self.transitions[key][1]
                else:
                    state=self.transitions[key][0]
            except:
                ok=0
                break

        if state in self.finalState and ok==1:
            return True
        else:
            return False


# fa=FA("C:\\Users\\Bubu\\LFTC\\Auxiliars\\FA.in")
# fa.menu()
