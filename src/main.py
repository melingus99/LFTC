from src.SymbolTable import SymbolTable
import re

#preconditions:
#input:
#output:RWOS-list of reserverd words, operators and separators
        #pos-list of positions of those RWOS
def listRWOS():
    file=open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\tokens.in",'r')
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

#preconditions
#input:path-string to the file to be detected
#output:text- list of tokens
def detect(path):
    f=open(path,'r')
    text=f.read()
    tokens=[]
    #text=text.splitlines()
    text=re.split("(\ |\n|\:|\=|\;|\(|\)|\+|\-|\*|\/|\<|\>|\%|\[|\]|\,)",text)
    lookup=['+','-','*','/','<','>','!']

    for i in range(len(text)-1):
        if text[i] in lookup and text[i+1]=='=':
            text[i]=text[i]+'='
            text[i+1]=''
        if text[i] in lookup and text[i+2]=='=':
            text[i]=text[i]+'='
            text[i+2]=''
        if text[i].startswith('â€˜') and text[i].endswith('â€™'):
            text[i]="'"+text[i][3:-3]+"'"

    return text

#preconditions:
#input:path-string the file to be scanned
#output:pif- program internal form
        #st-symbol table
        #message-string to find out if it was lexically corect or not
def scan(path):
    RWOS,pos=listRWOS()
    text=detect(path)
    st=SymbolTable()
    st.table[-1]=[]
    pif={}
    message=''
    letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    letters=letters.split(' ')
    letters=tuple(letters)

    digits='0 1 2 3 4 5 6 7 8 9'
    digits=digits.split(' ')
    digits=tuple(digits)
    line=1
    for token in text:
        if token=='\n':
            line+=1
        if token !='':
            if token in RWOS:
                st.table[-1].append(token)
                pif[token]=-1
            elif (token.startswith(digits) and any(letter in token for letter in letters)==False)\
                    or (token.startswith("'") and token.endswith("'")):
                st.insert(token)
                pif['ct']=st.search(token)
            elif token.startswith(letters):
                st.insert(token)
                pif['id']=st.search(token)

            else:
                message='lexical error at line: ' +str(line)
                print(token)
    if message=='':
        message='lexically correct'

    return pif,st,message


pif,st,message=scan("C:\\Users\\Bubu\\LFTC\\Programs\\p3")

print(message)
print(st.table)
print(pif)

