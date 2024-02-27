#Crear una funció que donada una llista de dígits ordenats, retorni el número corresponent.
# Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. 
#Ex: def Passar_a_Numero(llista): -- retorni el número que corresponen els dígits.
from operator import add
from functools import reduce

#amb map
def Passar_a_numero(m):
    c = list(map(lambda x:str(x), m))
    d = reduce(lambda x,y:x+y, c)
    print("La llista {} és el número {}".format(m,d))

m = [3, 5, 7,9,1]
Passar_a_numero(m)















#Sense map i a teclat
"""
def Passar_a_Numero(llista):
    a = 0
    while a!= '.':
        a = input("Introdueix un número: ")
        if a != '.':
            llista.append(a)
        else:
            llista.sort()
            llista.reverse()
            print(llista)

      
#Ordena la llista
llista = []
Passar_a_Numero(llista)
suma = reduce(add, llista)
print(suma)
"""