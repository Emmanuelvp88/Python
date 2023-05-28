nombreArchivo = input('Ingrse el nombre del archivo: ')
try:
     archivo = open(nombreArchivo)
except:
    print('el archivo', nombreArchivo, 'es invalido')
    quit()
dicc = dict()#creamos un diccionario
for lineas in archivo:#recoremos el archivo
    if lineas.startswith("From "):#seleccionamos las lineas que empizan con from
        listaLineas = lineas.split()#Almacenamos las lineas en una lista
        dia = listaLineas[2]#Guardamos
        listaDia = dia.split()
        for i in listaDia:
            dicc[i] = dicc.get(i, 0) + 1
print(dicc)




