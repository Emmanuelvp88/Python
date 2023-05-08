print(f'*************     Metodos islower() y lower()     *****************\n')
print(f'El metodo islower() siver para comparar si una cadena de texto esta escrita con puras letras minusculas,'
      f'si es verdadero nos regresara "true" de lo contrario "false"')
print('El metodo lower() en cambio es para convertir todas las letras minusculas de cualquier cadena de texto\n')
print('*****************   Metodos isupper() Y upper()    ******************')
print('El metodo isupper() es para comprobar si una cadena de caracteres contiene puras letras mayusculas,'
      'si esto es verdadero nos regresara un "true" de lo contrario "false"')
print('El metodo upper() se encarga de tranfromar una cadena de texto en puras letras MAYUSCULAS.\n')

cadena = input(f'Por favor ingresa cualquier cadena de texto: ')

if cadena.islower() == True:
    print(f'Tu cadena contiene puras minusculas.')
elif cadena.isupper() == True:
    print('Tu cadena contiene puras MAYUSCULAS.')
elif cadena.islower() == False:
    print(f'Tu cadena esta mezcada MAYUSCULAS y minusculas.\n')
    respuesta = input(f'Selecciona una opcion:  convertir tu cadena a puras minusculas "m" o a Puras MAYUSCULAS "M"?: (m/M)')
    if respuesta == "m":
        print(f'Tu respuesta fue "m", tu cadena fue convertida a puras minusculas: {cadena.lower()}')
    elif respuesta == "M":
        print(f'Tu respuesta fue "M", tu cadena fue convertida en puras MAYUSCULAS:  {cadena.upper()}')
    else:
        print('Tu respuesta es invalida intenta denuevo.')