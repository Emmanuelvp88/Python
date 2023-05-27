cadena = input('Ingresa una cadena de texto: ')
frase = input('Ingresa la frase que deseas eliminar de la cadena: ')
indice = cadena.find(frase)

fraseRecortada = cadena[:indice] + cadena[indice + len(frase)+1:]
print(fraseRecortada)