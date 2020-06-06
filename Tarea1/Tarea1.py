N=int(input("Ingrese un numero entero: "))
lista=list(range(1,N))
suma=0
cont=0
print("EL numero ingresado es: "+ str(N))
print("La lista de numeros desde 0 hasta N es: " + str(lista))

for i in range(0,len(lista)):
    cont=0
    for j in range(1,i):
        modulo=i%j
        if modulo==0:
            cont=cont+j
            print("posicion" + str(i) + " J: "+str(j))
            #suma=cont+suma
            print("Suma: "+ str(cont))
        if suma==i:
            print("El numero "+str(i)+ " es perfecto")
