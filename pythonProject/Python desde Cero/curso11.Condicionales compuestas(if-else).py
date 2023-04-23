# CONDICIONALES COMPUESTAS (if - else)

nombre = input("Para comenzar,  ¿Cual es tu nombre?")
matematicas = float(input(nombre + " ¿Cual fue tu calificacion en matematicas.?"))
biologia = float(input(nombre + " ¿Cual fue tu calificacion en biologa"))
quimica = float(input(nombre + " ¿Cual fueu tu calicicacion en quimica"))

promedio = (matematicas + quimica + biologia)

if promedio >= 6:
    print("Felicidades  " + nombre + " has Probado con: ", round(promedio, 2))
else:
    print("Lo sentimos ", nombre, " has Reprobado con: ", round(promedio, 2))
print("Fin.")
