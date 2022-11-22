print("Tienda Kuepa")
print("CK__ Cereal Kellog's 920g: $90.00")
print("CSN_ Cafe soluble nescafe 400g: $150.00")
print("PBB_ Pan Blanco Bimbo 680g: $42.10 ")
print("GM__ Galletas Maria Gamesa  141g: $31.90")
print("CL__ Crema Lala  417g: 36.50")
print("CHB_ Casillero Huevo Blaco: $77.00")
print("SM__ Sopa Marucha c/u: $11.00")
print("RBD_ Ron Bacardi 900ml: $189.00")
print("CE__ Cobrar y salir")
print("RE__ Restablecer \n")

inventario = {
    "CK": 90.00,
    "CSN": 150.00,
    "PBB": 42.10,
    "GM": 31.00,
    "CL": 36.50,
    "CHB": 77.00,
    "SM": 11.00,
    "RBD": 189.00,
}

total = 0.00
while 1 == 1:
    codigo = input("\nIngresa el codigo del Producto: ")
    if codigo == "RE":
        total = 0.00
        print("El total se a restabecido $0.00")
    elif codigo == "CE":
        print("\n Compra Cerrada, Total de: $", total, "\n")
        while 1:
            lista = []
            print('"A" Tarjeta Debito/Credito')
            print('"B" Efectivo')
            metodoDePago = input("Que metodo desea utilizar?")
            if metodoDePago == "A":
                print("\nEligio pago con tarjeta")
                print("Total a pagar: $", total)
                monto = float(input("\ningrese la cantidad a pagar, (asegurese que sea igual o mayor al TOTAL): "))
                input("ingrese su NIP: ")
                cambio = monto - total
                print("Su cambio es de: $", cambio)
                ticket = input("Desea inprimir su ticket.?: S / N: ")
                if ticket == "S":
                    while 1:
                        print("\ningrese Productos para la imprecion de ticket, cuando termine solo escriba 'fin'")
                        productos = input("Producto: ")
                        if productos == "fin":
                            print("************** Ticket de Compra *************")
                            break

                        lista.append(productos)
                    for i in range(len(lista)):
                        print("producto: ",str(lista[i]))
                print("\nGracia por Comprar En Tiendas KUEPA, Vuelva Pronto....")
                break
            elif metodoDePago == "B":
                print("\nEligio pago con Efectivo")
                print("Total a pagar: $", total)
                monto = float(input("\ningrese la cantidad a pagar, (asegurese que sea igual o mayor al TOTAL): "))
                cambio = monto - total
                print("Su cambio es de: $", cambio)
                ticket = input("Desea inprimir su ticket.?: S / N: ")
                if ticket == "S":
                    while 1:
                        print("\ningrese  Productos para la imprecion de ticket, cuando termine  solo escriba 'fin'")
                        productos = input("Producto: ")
                        if productos == "fin":
                            print("************** Ticket de Compra *************")
                            break
                        lista.append(productos)
                    for i in range(len(lista)):
                        print(str(lista[i]))
                print("\nGracia por Comprar En Tiendas KUEPA, Vuelva Pronto....")
                break
            else:
                print("\nOPCION NO VALIDA: Vuelva a digitar Su metodo de Pago.\n")
        break
    else:
        precio = inventario.get(codigo, "No Encontrado")
        print("Codigo", codigo, "$", precio)
        if precio == "No Encontrado":
            print("Por favor Vulava a digitar un codigo.")
        else:
            total = total + float(precio)
            print("Total de: $", total)