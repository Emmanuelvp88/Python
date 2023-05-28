print('***********   Metodo sort()  ***********')
#sort() se encarga de ordenar alfabeticamente los elementos de una lista

lista1 = ["Emmanuel", "Juan", "Carlos", "Ruben"]
print('Lista original: ', lista1)
lista1.sort()# NO se puede poner este metodo dentro del mismo print
print(f'lista ordenada: {lista1}')

print('**********   Metodos min(), max(), sum()   **********')
lista2 = [3,5,23,45,23]
print(min(lista2))
print(max(lista2))
print(sum(lista2))