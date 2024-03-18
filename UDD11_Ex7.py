#Crear una llista amb les lletres d’una paraula qualsevol. Utilitzar list comprehensions. 
#Ex: “institut”, retorni [‘i’,’n’,’s’,’t’,’i’,’t’,’u’,’t’].


def compresio(c):
    r = [x for x in c]
    print(r)


#Principal
c = input("escriu:")
compresio(c)




#Manera sense list comprehesions
"""
def compresio(paraula):
    l = []
    for i,e in enumerate(paraula):
        l.append(e)
    print(l)


#Principal
paraula = input("Introdueix una paraula:")
compresio(paraula)
"""