#Crear una funció que controli la divisió per zero i ens avisi que volem fer-ho.
def div(a,b):
    try:
        c = a/b
        print("La divisió de {} entre {} és {}.".format(a,b,c))
    except ZeroDivisionError:
        print("El segon paràmetre no pot ser zero.")

#Principal
a = int(input("Introdueix el numerador: "))
b = int(input("Introdueix el denominador: "))
div(a,b)