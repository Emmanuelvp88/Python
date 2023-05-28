with open("Historial.txt") as archivo:
    for i in archivo:
        if i.startswith("From "):
            print(i.rstrip())
#diccionario = dict()
lista1 = archivo.split()
print(lista1)
#for i in lista1:
 #   if i not in diccionario:
  #      diccionario[i] = 1
   # else:
    #    diccionario[i] = diccionario[i] + 1
#print(diccionario)

