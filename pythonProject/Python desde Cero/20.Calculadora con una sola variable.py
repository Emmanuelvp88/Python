print("****************************************************")
print("Bienvenido a la Calculadora Con Una sola Variable")
print("****************************************************")
print("Donde podras realizar la siguentes Operaciones.")
print("1.- Suma.")
print("2.- Resta.")
print("3.- Multiplicacion.")
print("4.- Divicion.")
print("5.- Exponente.")
print("6.- Resto.")
print("7.- Divicion entera.\n")

numero = int(input("Que Operacion deseas realizar."))


if numero == 1:
    print("Elegiste Suma.\n")
    numero = float(input("Ingresa tu primer numero."))
    numero += float(input("Ingresa tu segundo numero."))
    print("El resultado de tu Suma es: ", numero)
elif numero == 2:
    print("Elegiste Resta.\n")
    numero = float(input("Ingresa tu primer numero."))
    numero -= float(input("Ingresa tu segundo numero."))
    print("El resultado de tu Resta es: ", numero)
elif numero == 3:
    print("Elegiste Multiplicacion.\n")
    numero = float(input("Ingresa tu primer numero."))
    numero *= float(input("Ingresa tu segundo numero."))
    print("El resultado de tu multiplicacion es: ", numero)
elif numero == 4:
    print("Elegiste Divicion.\n")
    numero = float(input("Ingresa tu primer numero."))
    numero /= float(input("Ingresa tu segundo numero."))
    print("El resultado de tu Divicion es: ", numero)
elif numero == 5:
    print("Elegiste Exponente.\n")
    numero = float(input("Ingresa tu primer numero."))
    numero ^= float(input("Ingresa el exponente."))
    print("El resultado de tu Resta es: ", numero)
elif numero == 6:
    print("Elegiste Resto.\n")
    numero = float(input("Ingresa tu primer numero."))
    numero %= float(input("Ingresa tu segundo numero."))
    print("El resto de tu divicion es: ", numero)
elif numero == 7:
    print("Elegiste Divicion entera.\n")
    numero = float(input("Ingresa tu primer numero."))
    numero //= float(input("Ingresa tu segundo numero."))
    print("El resultado de tu Divicion entera es: ", numero)
else:
    print("La opcion que elegiste no existe.")
