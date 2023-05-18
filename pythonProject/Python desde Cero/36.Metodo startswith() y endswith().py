print('*********************  Metodo startswith() y endswith()   ****************\n')
print('El metodo stratswith() busca y compara ciertos carasteres se encuentren\n'
      'al principio en una cadena, solo funciona con parametros, Ejemplo: cadena.startswith("D")\n'
      'Si lo manejamos con 3 parametros Ejemplo: cadena.startwith("D", "int" "int") donde el primer parametro\n'
      'nos indica el caracter o palabra a buscar y los parametro 2 y 3 nos indican donde  vamos a empezar '
      'y hasta donde vamos a terminar en la cadena\n')

cadena = 'Diana lava la ropa'
print('******    Metodo startswith()    *********')
print(f'La cadena "{cadena}" ¿Empieza con la letra "D"?: {cadena.startswith("D")}')
print(f'La cadena "{cadena}" ¿Empieza con la palabra "Diana"?: {cadena.startswith("Diana")}')

print('\n*********     Metodo endswith()   **********')
print(f'La cadena "{cadena}" ¿termina con la letra "p"? {cadena.endswith("p")}')
print(f'La cadena "{cadena}" ¿termina con la palabra "ropa"? {cadena.endswith("ropa")}')