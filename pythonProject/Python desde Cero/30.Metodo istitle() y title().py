nombre = "eMManuEL viLLalVa peRez"
print(f"Cadena original: {nombre}\n");
print(f'Cadena con metodo istitle(): {nombre.istitle()}');
print("nos regreso false proque la cadena esta escrito incoreectamente, tiene mezcaldas mayusculas y minisculas.\n")
print(f'Cadena con el metodo title(): {nombre.title()} ');
print(
    f'El metodo title() se encarga de componer la cadena de la manera correcta, mayusculas al principio y las demas minusculas.')

# El metodo istitle() se encarga de revisar con anticipacion la cadena de texto, mandandonos un "true o false"
# si la cadena esta escrita correctamente respetando mayusculas y minusculas con respecto asu correcta semantica,
# si esta escrita correctamente nos mandara como resultado un "true" y si esta mal escrita "false"
