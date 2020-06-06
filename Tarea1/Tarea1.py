print('''
***Bienvenidos al programa que determina si un numero es perfecto***
''')
print("\n\n\n")
N=int(input("Ingrese un numero entero: "))
lista=list(range(0,N))
print("\n\n\n")
print("EL numero ingresado es: "+ str(N))
print("\n\n\n")
suma=0
for i in range(1,N+1):
    cont=0
    for j in range(1,i):
        modulo=i%j
        if modulo==0:
            cont=cont+j
            #print("posicion" + str(i) + " J: "+str(j))
            #print("Suma: "+ str(cont))
        suma=cont
    if suma==i:
        print("El numero "+str(i)+ " es perfecto")
