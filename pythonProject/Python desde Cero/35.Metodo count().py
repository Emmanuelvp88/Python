print('*************  Metodo count()   *************\n')
print('el metodo conunt() nos permite contar cuantos caracteres tienen una cadena de texto\n'
      'si no le pasamos parametros Ejemplo: dadena.count("") solo contara cuantos caracteres tiene una cadena de texto\n'
      'En este otro Eejemplo: cadena.count("m") nos contara cuantas "m" existen en la cadena de etexto,\n'
      'el este  otro Ejemplo: cadena.count("ma", 3, 9) cuando le pasamos 3 parametros, buscara la palabra o caracter\n'
      'que le pasamos como primer parametro y los otros dos de tipo "int" son el inicio y el final de \n'
      'de busqueda en la cadena.\n')

cadena = input('ingresa una cadena de texto: ')
caracter = input('Que caracter quieres contar: ')
comienzo = int(input('De donde quieres que empieze: '))
final = int(input('Donde quieres que termine: '))
print(f'La palabra o caracter "{caracter}" se encuentra {cadena.count(caracter, comienzo, final)} veces en la cadena "{cadena}"')

