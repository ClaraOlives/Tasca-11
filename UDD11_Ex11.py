#Crear una funció que permeti llegir la informació d’un fitxer, però que controli que el fitxer existeix i 
#que la seva obertura no doni cap problema. Fes-ho també utilitzant with. Si voleu podeu practicar el try,
# except afegint-ho a les funcions anteriors.
#Pot entrar a l'examen!

"""
def llegir(fitxer):
    a = []
    with open(fitxer,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)


#Principal
    
fitxer = "/home/cicles/AO/Tasca11/T11.txt"
llegir(fitxer)
"""

#Variant 

def llegir(fitxer):
    a = []
    with open(fitxer,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def afegir_fitxer(fitxer,llista):
    with open(fitxer,"a+") as f:
        for e in llista:
            f.write(e+"\n")
    
    
#Principal
    
fitxer = "/home/cicles/AO/Tasca11/T11.txt"
llista = ["Margarita", "Antonia","David", "Richard", "Kamavinga", "Escalope", "Calamardo"]
afegir_fitxer(fitxer,llista)
llegir(fitxer)
