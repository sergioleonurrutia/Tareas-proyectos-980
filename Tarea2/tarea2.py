def divisores(N):
    lista=list(range(1,N))
    suma=0
    for i in lista:
        modulo=N%i
        if modulo ==0:
            suma=suma+i
    return suma
#*****************************************************************+

cont=2
bandera=0
numero= int(input("Ingrese un numero entero: "))

while bandera<=numero:
    amigo1=divisores(cont)
    print("Respuesta del primer numero: " +str(amigo1))
    amigo2=divisores(amigo1)
    print("Respuesta del segundo numero: " + str(amigo2))
    cont=cont+1

    if amigo1==amigo2:
        bandera=bandera+1
