# SENTANCIAS CONDICIONALES ANIDADAS

print("****************** \n"
      "CONVERSIONES \n"
      "****************** \n")

print("Preciona 1 para conevertir de numero a palabra.")
print("Preciona 2 para convertir de palabra a numero. \n")
opcion = int(input("¿Cual es la opcion que deseas realizar?  \n"))

if opcion == 1:
    print("Has seleccionado el conversor de numeros a palabras. \n")

    numero = int(input(" Cual es el numero que deseas convertir en  palabra?"))
    if numero == 1:
        print(" El numero es 'Uno'")
    elif numero == 2:
        print(" El numero es 'Dos'")
    elif numero == 3:
        print(" El numero es 'Tres'")
    elif numero == 4:
        print(" El numero es 'Cuatro'")
    elif numero == 5:
        print(" El numero es 'Cinco'")
    else:
        print("El numero no es valido. \nFin.")
elif opcion == 2:
    print("Has seleccionado el conversor de palabras a numeros. \n")
    palabra = input("Que palabra deseas convertir en numero.")
    if palabra == "Uno":
        print(" El numero de tu palabra es '1'")
    elif palabra == "Dos":
        print(" El numero de tu palabra es '2'")
    elif palabra == "Tres":
        print(" El numero de tu palabra es '3'")
    elif palabra == "Cuatro":
        print(" El numero de tu palabrea es '4'")
    elif palabra == "Cinco":
        print(" El numero de tu palabra es '5'")
    else:
        print("La palabra no es valida \n  Fin.")
else:
    print("La opcion no es valida.")
