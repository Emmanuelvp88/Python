print(f'*************     Metodos islower() y lower()     *****************\n')
print(f'El metodo islower() siver para comparar si una cadena de texto esta escrita con puras letras minusculas,'
      f'si es verdadero nos regresara "true" de lo contrario "false"\n')
print('El metodo lower() en cambio es para convertir todas las letras minusculas de cualquier cadena de texto\n')

cadena = input(f'Por favor ingresa cualquier cadena de texto: ')
cadena.islower();
if cadena == True:
    print(f'Tu cadena contiene puras minusculas.')
else:
    print(f'Tu cadena esta mezcada mayusculas y minusculas.')
    respuesta = input(f'Quieres convertir tu cadena a puras minusculas?: (Y/N)')
    if respuesta == "Y" or respuesta == "y":
        print(f'Tu respuesta fue si, tu nueva cadena queda asi: {cadena.lower()}')
    elif respuesta == "n" or respuesta == "N":
        print(f'Tu respuesta fue No, tu nueva cadena queda asi:')
    else:
        print('Tu respuesta es invalida intenta denuevo.')