print('*********************  Metodo startswith() y endswith()   ****************\n')
print('El metodo stratswith() busca y compara si ciertos carasteres se encuentran'
      'al principio en una cadena de carasteres, solo funciona con parametros, Ejemplo: cadena.startswith("D")'
      'Si lo manejamos con 3 parametros Ejemplo: cadena.startwith("D", "int" "int") donde el primer parametro '
      'nos indica el caracter o palabra a buscar y los parametro 2 y 3 nos indican donde  vamos a empezar '
      'y hasta donde vamos a terminar en la cadena\n')

cadena = 'Diana lava la ropa'
print('******    Metodo startswith()    *********')
print(f'La cadena "{cadena}" ¿Empieza con la letra "D"?: {cadena.startswith("D")}')
print(f'La cadena "{cadena}" ¿Empieza con la palabra "Diana"?: {cadena.startswith("Diana")}')
