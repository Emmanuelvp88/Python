#SISTEMA VACAIONAL

print ("    ******************************************************************")
print("          Bienvenido al sistema vacacional de Coca-Cola-Company")
print ("    ******************************************************************\n")

nombre = input("Cual es el nombre del empleado: ")
departamento = int(input("Hola " + nombre +" Cual es la clave de tu departamento: "))
antiguedad = int (input(nombre + " ahora dime tus años de serviciocio en la corporacion: "))

print("\nCalculando tus dias de vacaciones..... \n")

if departamento == 1:
    
    if antiguedad == 1:
        print("El trabajador  " + nombre +" , Departamento  Clave 1,  Tiene derecho a 6 dias de vacaiones.")
    elif antiguedad >=2 and  antiguedad <=6:
        print("Eltrabajador " + nombre + ", Departamento Clave 1, Tiene derecho a 14 dias de vacaciones.")
    elif antiguedad >= 7:
        print("El trabajador " + nombre  + ", Departamento Calve 1, Tiene decho a  20 dias de vacaiones .")
    else:
        print("El trabajador " + nombre + " aun no alcanza dias de vacaciones")
        
elif departamento == 2:
    
    if antiguedad == 1:
        print("El trabajador " + nombre +", departamento Clave 2 tiene derecho  a  7 dias de vacaiones.")
    elif antiguedad >= 2 and antiguedad <=6:
        print("El trabaajdor " + nombre  + ", departamento Clave 2 tiene derecho a 15 dias de vacaciones")
    elif antiguedad >= 7 :
        print("El trabajador " +  nombre + ", departamento Clave 2 tiene derecho a 22 dias de vacaciones.")
        
elif departamento == 3:
    
    if antiguedad ==1:
        print("El trabajador " + nombre + ", departamento Clave 3 tiene derecho a 10 dias de vacaciones.")
    elif antiguedad >=2 and antiguedad  <= 6:
        print("El trabajador " + nombre + ", departamento Clave 3 tiene derecho  a 20 dias de vacaciones.")
    elif antiguedad >= 7:
        print("El trabajador " + nombre + ", departamento Clave 3 tiene derecho a 30 dias de vacaciones.")
else:
    print("La clave del departamento no existe, Favor de verificar.")
