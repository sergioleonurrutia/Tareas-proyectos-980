import eperfecto as NumeroPerfecto  #Importo el archivo que contiene la funcion del Numero perfecto

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

NumeroPerfecto.numero_perfecto(numero)