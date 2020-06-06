#****************** FUNCION *************************
def numero_perfecto(N):
    suma=0
    for i in range(1,N+1):            #Recorre los valores de 1 hasta N
        cont=0
        for j in range(1,i):          #Hace un recorrido por los valores individuales de i
            modulo=i%j                #Calcula el modulo para determinar los divisores propios (DP)
            if modulo==0:
                cont=cont+j           #Contador de divisores propios
            suma=cont
        if suma==i:                   #Si la suma de DP es igual al numero, entonces es Numero perfecto
            print("\n***El numero: "+str(i)+ " es perfecto")    #Imprime los numeros perfectos de 0-N
#****************************************************