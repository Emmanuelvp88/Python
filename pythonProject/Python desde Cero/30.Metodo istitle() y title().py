
firstName = input('Ingresa tu nombre: ')
lastName = input('ingresa tu apellido: ')
nombre = f'{firstName} {lastName}'

print(f"Cadena original: {nombre}\n");
print(f'Metodo istitle(): {nombre.istitle()}');
if nombre.istitle() == False:
    print("nos regreso false proque la cadena esta escrito incoreectamente, tiene mezcaldas mayusculas y minisculas.\n")
else:
    print('La cadena es semanticamnete correcta')

print(f'Cadena corregida con el metodo title(): {nombre.title()} ');
print(f'El metodo title() se encarga de corregir la cadena poniendo mayusculas al principio de cada palbra\n'
      f' y las demas en minusculas y si encuantra una mayuscula despues de la primera letra la corrige convirtiendola en minuscula .')

# El metodo istitle() se encarga de revisar si una cadena de texto se encuentra bien escrita semanticamente
# si es asi nos mandara un "true" o  un "false" si noe s asi
# la manera correcta seria en principio de cada palabra lleva mayuscula "true"
# minusculas al principio de cada palabra  y mayusculas entrecaladas
