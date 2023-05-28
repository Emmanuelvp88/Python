print('***********   Metodo sort()  ***********')
# sort() se encarga de ordenar alfabeticamente los elementos de una lista

lista1 = ["Emmanuel", "Juan", "Carlos", "Ruben"]
print('Lista original: ', lista1)
lista1.sort()# NO se puede poner este metodo dentro del mismo print
print(f'lista ordenada: {lista1}')

print('\n**********   Metodos min(), max(), sum()   **********')
# min() nos devuelve el numero menor de la lista
# max() nos devuleve el numero mayor de la lista
# sum() suma todos los elementos de la lista

lista2 = [3,5,23,45,23]
print(f'Metodo min: {min(lista2)}')
print(f'Metodo max: {max(lista2)}')
print(f'Metodo sum: {sum(lista2)}')
print(f'Sacamos el promedio de lista2: {sum(lista2)/len(lista2)}')