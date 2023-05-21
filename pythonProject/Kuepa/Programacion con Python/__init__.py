lista = {"El Correo es:": 'stephen.marquard@uct.ac.za', 'El Dia que se mando fue:': 'Saturday',
         'El numero de dia fue: ': 5, 'El mes que se mando fue: ': 'Jan', 'El año que se mando fue: ': 2008,
         'La Hora a la que se mando fue: ': '09:14.16'}
while 1 == 1:
    validacion = input('Escriba el nombre del archivo correcto: ')
    if validacion == "Historial.txt":
        for i in lista:
            print(f'{i}{lista[i]}')

    else:
        print("nombre del archivo incorrecto,vuelve a intentarlo")
