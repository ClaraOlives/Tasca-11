#Crear una classe anomenada Animal que tingui els següents atributs d’objecte: especie i edat i els següents mètodes: 
#xerrar (abstracte), mourem (abstracte) i quisoc. Llavors, crearem diferents subclasses:  Cavall, Dofí, Abella, Humà, Centaure.... 
#que hauran de redefinir aquestes mètodes. Crearem una nova subclasse d’Humà, anomenada Fiet. 
#Llavors, crearem una subclasse Centaure que heredarà de Cavall i Humà. Finalment, tindrem una nova classe xou que no té cap relació 
#amb els altres, però que té els mateixos mètodes que Animal implementats.
#Abella crearà un nou mètode anomenat, picar. 
#Humà tindrà un nou atribut d’objecte anomenat, nom.
#Fiet tindrà un nou atribut d’objecte anomenat, pares (llista). I un nou mètode anomenat nompares que ens mostrarà el nom dels pares.
#Amb això, crear un llista d’elements de cada tipus i un for (bucle) que cridi als mètodes iguals.

class Animal():
    def _init_(self, atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        pass
    def mourem(self):
        pass
    def quisoc(self):
        print("Sóc un animal.")

class Cavall(Animal):
    def xerrar(self):
        print("Iíííííí")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Sóc un cavall.")

class Dofi(Animal):
    def xerrar(self):
        print("Ichichich")
    def mourem(self):
        print("Em moc nadant")
    def quisoc(self):
        print("Sóc un dofí.")

class Abella(Animal):
    def xerrar(self):
        print("Sssssss")
    def mourem(self):
        print("Em moc volant")
    def quisoc(self):
        print("Sóc una abella.")
    def picar(self):
        print("Si m'emprenyes et picaré!")

class Huma(Animal):
    def _init_(self, nom,atribut, edat,):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        print("Hola! Nosaltres utilitzem un idioma per parlar")
    def mourem(self):
        print("Em moc caminant")
    def quisoc(self):
        print("Sóc un humà.")

class Centaure(Huma,Cavall):
    def xerrar(self):
        print("Hola! Nosaltres utilitzem un idioma per parlar")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Sóc un centaure.")

class Fiet(Huma):
    def _init_(self, nom,atribut, edat,llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares
    def xerrar(self):
        print("Ueeee")
    def mourem(self):
        print("Em moc gatejant")
    def quisoc(self):
        print("Sóc un fiet.")
    def nompares(self):
        for e in self.pares:
            print(e.nom)
class xou():
    def xerrar(self):
        print("xou")
    def mourem(self):
        print("Em moc fent xou")
    def quisoc(self):
        print("Sóc un xou.")



#Principal

a = [Cavall("Marró","4"), Dofi("Gris","10"),Abella("Negra i groga","0,5"),Huma("Sibila","Cristià","7"),Centaure("Fiona","Marrón","18"),Fiet("Jordi","Moreno","9",["Fiona","Marc"]),xou()]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()