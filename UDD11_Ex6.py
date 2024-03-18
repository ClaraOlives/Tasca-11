#Crear una funció que donada una llista de valors numèrics, retorni el número d’elements on coincideix el valor 
#i l’índex on és. Utilitzar enumerate. Ex: [0, 2, 3, 3, 4], retorni 3.


def coincidir(llista):
    l = []
    for i,e in enumerate(llista):
        if e == i:
            l.append(e)
    print("Els elements de la llista {} que coincideixen en la seva posició són {}".format(llista, l))

#Principal

llista = [3,7,2,3,4,5,6,7,8,9,10,1]
coincidir(llista)