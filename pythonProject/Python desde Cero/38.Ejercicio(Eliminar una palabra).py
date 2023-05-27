frase = input('Ingresa una frase que desees: ')
palabra = input('Ingresa la palabra que deseas eliminar de esa frase: ')
indice = frase.find(palabra)

fraseRecortada = frase[0:indice] + frase[indice + len(palabra)+1:  ]
print(fraseRecortada)