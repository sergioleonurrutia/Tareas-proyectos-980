import eDP as DivisorPropio

cont=2
bandera=0
temp1=0
temp2=0
numero= int(input("Ingrese un numero entero: "))

while bandera<numero:
    amigo1=DivisorPropio.divisores(cont)
    amigo2=DivisorPropio.divisores(amigo1)
    
    if amigo1==amigo2:
        cont=cont+1

    if (temp2==amigo1 and temp1==amigo2):
        cont=cont+1

    if cont==amigo2:
        bandera=bandera+1
        print("Los numeros "+str(amigo1)+" y "+str(amigo2)+" son los amigos No. "+str(bandera))
        temp1=amigo1
        temp2=amigo2  
    cont=cont+1
