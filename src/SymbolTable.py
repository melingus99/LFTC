class SymbolTable():
    #input:key - if you want to use a custom key
    #      function - if you want to use a custom function
    #output:ST object
    def __init__(self,key=7,hash=''):
        if hash =='':
            self.__hash=self.__myHash
        else:
            self.__hash=hash
        self.__key=key
        self.table={}

    #preconditions:symbol must be a string
    #input:string-the symbol to be hashed
    #output:integer
    #this function returns the sum of the ascii code of all the letters % 7
    def __myHash(self,key,symbol):
        return sum(ord(ch) for ch in symbol)%key

    #preconditions: symbol must be a string
    #input:string-the symbol to be introduced
    #output:
    #this function inserts in the symbol table the given string in the aproppiate hash index
    def insert(self,symbol):
        if self.search(symbol)!=False:
            return
        val=self.__hash(self.__key,symbol)
        if val in self.table:
            self.table[val].append(symbol)
        else:
            self.table[val]=[symbol]

    #preconditions: symbol must be a string
    #input:string -the symbol to be searched
    #output: True - the symbol exists in the ST
    #        False - the symbol does not exists in the ST
    #this function checks if the given string exists in the symbol table
    def search(self,symbol):
        val=self.__hash(self.__key,symbol)
        if val not in self.table:
            return False

        for i in range(len(self.table[val])):
            if self.table[val][i]==symbol:
                return i

        return False
