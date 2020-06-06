#****************** FUNCION *************************
def numero_perfecto(N):
    suma=0
    #lista=list(range(0,N))
    for i in range(1,N+1):
        cont=0
        for j in range(1,i):
            modulo=i%j
            if modulo==0:
                cont=cont+j
            suma=cont
        if suma==i:
            print("\n***El numero: "+str(i)+ " es perfecto")
#****************************************************
print('''
---------------------------------------------------------------------
***Bienvenidos al programa que determina si un numero es perfecto***
Programador: Sergio Augusto León Urrutia
Carnet: 201700722
---------------------------------------------------------------------
''')

print("\n")
numero=int(input("Ingrese un numero entero: "))
print("\nEL numero ingresado es: "+ str(numero))

numero_perfecto(numero)