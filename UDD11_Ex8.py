#Crear una llista dels 10 primers parells. Utilitzar list comprehensions. Ex: [2, 4, 6, 8, 10, 12, ...].



def compresio():
    r = [x for x in range(20) if x % 2==0]
    print(r)


#Principal
compresio()

