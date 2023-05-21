#Escribimos una lista que contenga la clave y el valor
lista = {"El Correo es:": 'stephen.marquard@uct.ac.za', 'El Dia que se mando fue:': 'Saturday',
         'El numero de dia fue: ': 5, 'El mes que se mando fue: ': 'Jan',
         'El año que se mando fue: ': 2008,'La Hora a la que se mando fue: ': '09:14.16'}

#loop donde podamos regresar simpre que la validacion del archivo sea incorrecta
while 1 == 1:
    #Mandamos a pedir datos al usuario
    validacion = input('Escriba el nombre del archivo correcto: ')

    #Validacion de datos del usuario que sean correctos
    if validacion == "Historial.txt":
        #imprecion de datos mediante un "for in"
        for i in lista:
            print(f'{i}{lista[i]}')
        break
        #Para terminar programa si todo salio bien

    #Si no escribio bien el nombre del archivo volverlo a intentar por eso esta el "While"
    else:
        print("nombre del archivo incorrecto,vuelve a intentarlo")
