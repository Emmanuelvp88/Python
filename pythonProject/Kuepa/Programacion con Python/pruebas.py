frase = input('Ingresa una frase: ')
contador = 0
if contador < len(frase):
    for letra in frase:
        print(frase[contador], sep=", ")
        contador+=1