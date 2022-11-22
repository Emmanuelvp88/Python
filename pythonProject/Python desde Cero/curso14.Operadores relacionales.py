#OPERADORES RELACIONALES

print ('''En esta leccion veremos la diferencia entre dos numeros
usando los operadores relacionales \n''')

numero1 = int(input ("Introduce tu primer numero"))
numero2 = int(input("Introduce tu sendo numero"))

print("\n Los numeros a comprar son: ", numero1," y ", numero2)

if numero1 > numero2:
    print(numero1, " es mayor que  ", numero2)  
if numero1<numero2:
    print(numero1, " es menor que ",  numero2)
if numero1 >= numero2:
    print(numero1, " es mayor o igual a ", numero2)
if numero1<= numero2:
    print(numero1," es menor o igual a ",  numero2)
if numero1 != numero2:
    print (numero1," es Diferente de ", numero2)
else:
        print(numero1 , " es igual a ",  numero2) 
        
