from src.SymbolTable import SymbolTable
st=SymbolTable()

st.insert('mama')
print(st.search('mama'))
print(st.search('mmaa'))
st.insert('mmaa')
print(st.search('mmaa'))
st.insert('mar')
print(st.table)
