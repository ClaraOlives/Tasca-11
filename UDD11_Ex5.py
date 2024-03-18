#Crear una funció que donada una llista, retorni un diccionari que tingui com a clau: 
#els valors de la llista i com a valor el seu índex dins la llista. Utilitzar enumerate. 
#Ex: (‘casa’,’cotxe’,’cadira’,’taula’) retorni {‘casa’:0, ‘cotxe’:1, ‘cadira’:2, ‘taula’:3}.

def diccionari(llista):
    dic = {}
    for i,e in enumerate(llista):
    #L'element té el nombre de la seva posició
        dic[e]= i
    print("De la llista {} hem creat el diccionari \n{}".format(llista, dic))

#Principal
llista = ["Cotxe", "Casa", "Vaixell","Colom", "Ca", "Mussol", "Clara"]
diccionari(llista)