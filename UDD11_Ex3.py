#Crear una funció que donada una llista de paraules i una lletra, retorni una llista amb les paraules 
#que comencen per la lletra donada. Utilitzar filter. Ex: [“maria”, “manta”, “peu”, “mà”] i li deim que 
#ens retorni totes les que comencen per ‘p’, en retorni [‘peu’].


def filtrar(llista,c):
    f = list(filter(lambda x:x[0]==c.lower() or x[0]==c.upper(), llista))
    print("De la llista{} \n, les paraules que comencen per {} són {}".format(llista,c,f))





#Principal
llista = ["hola", "Casa", "barcelona", "pernil", "cabra", "hospital", "institut","ase"]
c = "c"
filtrar(llista,c)

