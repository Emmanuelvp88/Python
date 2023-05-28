nombreArchivo = input('Ingrse el nombre del archivo: ')
try:
     archivo = open(nombreArchivo)
except:
    print(f'el archivo "{nombreArchivo}" es invalido')
    quit()
dicc = dict()#creamos un diccionario tambien se puede de ssta otra manera "Dicci = {}"
for lineas in archivo:#recoremos el archivo
    if lineas.startswith("From "):#seleccionamos las lineas que empizan con from
        listaLineas = lineas.split()#Almacenamos las lineas en una lista
        dia = listaLineas[2]#Guardamos el elemento 2 de la lista en una variable
        listaDia = dia.split()# y Guardamos esa var en una lista
        for dias in listaDia:# recorremos esa lista para guardarla en un diccionario y hacer el conteo
            dicc[dias] = dicc.get(dias, 0) + 1
print(dicc)

