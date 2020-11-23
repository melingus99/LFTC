from src.SymbolTable import SymbolTable
import re
from src.FA import FA

class Scanner():
    def __init__(self,tokensPath):
        self.__tokensPath=tokensPath
    #preconditions:
    #input:
    #output:RWOS-list of reserverd words, operators and separators
            #pos-list of positions of those RWOS
    def __listRWOS(self):
        file=open(self.__tokensPath,'r')
        RWOS=[]
        pos=[]
        for line in file.readlines():
            line=line.split(":")
            if line[0]=='':
                line[0]=':'
            pos.append(line[1])
            RWOS.append(line[0])
        RWOS[-1]='\n'
        return RWOS,pos

    #preconditions:path must be valid path to the program
    #input:path-string to the file to be detected
    #output:text- list of tokens
    def detect(self,path):
        f=open(path,'r')
        text=f.read()
        #text=text.splitlines()
        text=re.split("(\ |\n|\:|\=|\;|\(|\)|\+|\-|\*|\/|\<|\>|\%|\[|\]|\,)",text)
        lookup=['+','-','*','/','<','>','!']
        digits=('0','1','2','3','4','5','6','7','8','9')

        for i in range(len(text)-1):
            if text[i] in lookup and text[i+1]=='=':
                text[i]=text[i]+'='
                text[i+1]=''
            elif text[i] in lookup and text[i+2]=='=':
                text[i]=text[i]+'='
                text[i+2]=''
            elif text[i].startswith('â€˜') and text[i].endswith('â€™'):
                text[i]="'"+text[i][3:-3]+"'"

            elif (text[i]=='-' or text[i]=='+') and text[i+1].startswith(digits):
                text[i]=text[i]+text[i+1]
                text[i+1]=''

        return text

    #preconditions:path must be valid path to the program
    #input:path-string the file to be scanned
    #output:pif- program internal form
            #st-symbol table
            #message-string to find out if it was lexically corect or not
    def scan(self,path):
        RWOS,pos=self.__listRWOS()
        text=self.detect(path)
        st=SymbolTable()
        indFA=FA("C:\\Users\\Bubu\\LFTC\\Auxiliars\\indFA.in")
        ctFA=FA("C:\\Users\\Bubu\\LFTC\\Auxiliars\\CtFA.in")
        st.table[-1]=[]
        pif={}
        message=''
        letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        letters=letters.split(' ')
        letters=tuple(letters)
        digits='0 1 2 3 4 5 6 7 8 9'
        digits=digits.split(' ')
        digits=tuple(digits)
        digitsNoZero=digits[1:-1]
        line=1
        for token in text:
            if token=='\n':
                line+=1
            if token !='':
                if token in RWOS:
                    st.table[-1].append(token)
                    pif[token]=-1
                elif ((ctFA.isIntOrCt(token)==True) or (token.startswith("'") and token.endswith("'"))):
                    st.insert(token)
                    pif['ct']=st.search(token)
                elif indFA.isIntOrCt(token)==True:
                    st.insert(token)
                    pif['id']=st.search(token)
                else:
                    message='lexical error at line: ' +str(line)
        if message=='':
            message='lexically correct'

        return pif,st,message


'''
elif (token.startswith(digits) and any(letter in token for letter in letters)==False)\
        or (token.startswith("'") and token.endswith("'")) \
        or (token.startswith(('-','+')) and any(digit in token for digit in digitsNoZero)==True):
    st.insert(token)
    pif['ct']=st.search(token)
elif token.startswith(letters):
    final=False
    ok=True
    for c in token:
        if c in digits:
            final=True
        if c not in letters and c not in digits:
            ok=False
        if final==True and c in letters:
            ok=False

    if ok==False:
        message='lexical error at line: ' +str(line)
    else:
        st.insert(token)
        pif['id']=st.search(token)
'''
