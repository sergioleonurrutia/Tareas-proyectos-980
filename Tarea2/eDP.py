def divisores(N):
    lista=list(range(1,N))
    suma=0
    for i in lista:
        modulo=N%i
        if modulo ==0:
            suma=suma+i
    return suma