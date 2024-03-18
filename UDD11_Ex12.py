#Crear un directori dins /home/cicles/AO que es digui Prova, canviar-nos a aquest directori, a dins, 
#crear el fitxer Ex12.txt i posar a dins el nom de tots els companys de classe. Tancar el fitxer. 
#Obrir-lo per afegir el nom dels professors. Tancar-lo. Finalment, l’obrirem i posarem tot el seu contingut dins una llista de noms.

import os
companys = ["Jordi","Claudia", "Clara", "Paula", "Joan", "Marc", "Ian", "Sergi","Sebas","Anas","Hugo","Oscar","Josep","Fede","Alvaro","Joselu","Leiner","Ayoub","David"]
os.mkdir("/home/cicles/AO//Tasca11/Prova")
os.chdir("/home/cicles/AO//Tasca11/Prova")
with open("ex12.txt", "w") as f:
    print("Fitxer creat correctament!")
    for e in companys:
        f.write(e+"\n")
professors = ["David","Pep","Fela","Lluís","Joan"]
with open("ex12.txt","a+") as f:
    for e in professors:
        f.write(e+"\n")
a = []
with open("ex12.txt","r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])

print(a)