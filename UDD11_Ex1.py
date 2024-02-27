#Crear una funció que compti la longitud de cada paraula d’una cadena de caràcters que li passem.
# Utilitzar map. Ex: def lenp(frase): -- retorni una llista amb la longitud de cada paraula de la frase.

#Map--> aplica la funció a cada element que li pasem, en aquest cas els elements de f. Split-->Separa per paraules.Entre les cometes de f.split
#Hi ha un espai, per indicar que separi per cada espai que hi ha.

def lenp(frase):
    r = frase.split(" ")
    l = list(map(len,r))
    print(l)



frase = input("Introdueix una frase: ")
lenp(frase)

