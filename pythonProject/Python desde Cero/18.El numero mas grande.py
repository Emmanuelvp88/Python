print("**********************************************************************************")
print("Este es un programa que determina cual es el numero mas grande.")
print("**********************************************************************************")

num1 = int(input("Igresa un primer numero: "))
num2 = int(input ("Ingresa un segundo numero: "))
num3 = int(input("Ingresa untercer numero: "))

if num1 > num2 and num1 > num3:      #Si este if no entra'
    print("El primer numero es ", num1, " y es el mayor de todos.")    
else:                            #'Por consecuencia entra este "else" y ejecuta lo que tiene dentro'
    if num2 > num3:     #Y si este segundo "if" no entra 
        print("El segundo numero es " , num2, " y es el mayor que todos.")
    else:                        #Este  segundo "else" tendra que terminar el programa
        print("El tercer numero es " , num3, " y es el mayor de todos.")
print("Fin.")
