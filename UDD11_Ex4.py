#Crear una funció que donades dues llistes, les concateni amb un connector. Utilitzar zip. 
#Ex: [‘sub’,’supra’] i [‘campió’ ‘campiona’] i el connector ‘-’, retorni [‘sub-campió’][‘supra-campiona’].


def conector(l1,l2):
    for n, e in zip(l1,l2):
        print(n, '-',e)


#Principal
l1 = ['super','guaca']
l2 = ['man','mole']
conector(l1,l2)