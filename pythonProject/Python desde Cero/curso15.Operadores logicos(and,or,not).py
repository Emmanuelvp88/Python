#OPERADORES LOGICOS

#Operador "And"
print("Operador (and) Conjuncion")

num = int(input("Escribe un numero mayor que 1 y menor que 10"))

if num > 1 and num < 10:
    print(" Efectivamente el numero ", num, " es mayor que 1 y menor que 10")
else:
    print("Lo siento el numero qu edigitaste no cumple con el requeriminto")
    
#Operador "Or"

print("\n Operador (Or) Disyuncion")

palabra = input("Ingresa tu nombre o apellido ")
if palabra == "Emmanuel"  or  palabra == "Villalva":
    print("Correcto la palabra que ingresaste es una de las dos necesarias:  ", palabra)
else:
    print("Lo siento la palabra no es ninguan de las dos que necesitamos")

#Operador "Not"
print("\nOperador (Not) Negacion")
num = int(input("Ingresa un numero menor a 7 para que se cumpla la condicion"))
if not num > 7:
    print("En efecto el numero ", num, " es menor a '7' ")
else:
        print(" La condicion no se cumplio en numero ", num, " no es menor que '7'")
    
