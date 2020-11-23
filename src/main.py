from src.scanner import Scanner
scanner=Scanner("C:\\Users\\Bubu\\LFTC\\Auxiliars\\tokens.in")

pif,st,message=scanner.scan("C:\\Users\\Bubu\\LFTC\\Programs\\p3")
print(message)
print('Symbol Table: ',str(st.table))
print('PIF: '+str(pif))

pif,st,message=scanner.scan("C:\\Users\\Bubu\\LFTC\\Programs\\p1err")

print(message)
print('Symbol Table: ',str(st.table))
print('PIF: '+str(pif))

# f=open("C:\\Users\\Bubu\\LFTC\\Auxiliars\\test.txt","w")
# letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
# letters=letters.split(' ')
# digits='0 1 2 3 4 5 6 7 8 9'
# digits=digits.split(' ')
# for letter in letters:
#     f.write("q5,{}:q5,q6\n".format(letter))
