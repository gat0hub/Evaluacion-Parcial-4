
compradores = []
funciones = []


stock1 = 50
stock2 = 60

def comprar_entrada():
    global stock1, stock2

    print("-- comprar entrada --")
    nombre = input("nombre del comprador: ").strip()

    if nombre in compradores:
        print("error: comprador ya registrado.")
        return

    print("1. movimiento origen con los tripulantes shamanes ({} entradas)".format(stock1))
    print("2. movimiento origen con sonrisa mc ({} entradas)".format(stock2))
    funcion = input("funcion (1 o 2): ").strip()

    if funcion == "1":
        if stock1 > 0:
            compradores.append(nombre)
            funciones.append(1)
            stock1 -= 1
            print("entrada registrada en funcion 1! stock restantes:")
        else:
            print("no quedan entradas disponibles para funcion 1.")
    elif funcion == "2":
        if stock2 > 0:
            compradores.append(nombre)
            funciones.append(2)
            stock2 -= 1
            print("entrada registrada en funcion 2! stock restantes:")
        else:
            print("no quedan entradas disponibles para funcion 2.")
    else:
        print("error: opción de funcion invalida.")
        return

    print("funcion 1: {}".format(stock1))
    print("funcion 2: {}".format(stock2))

def cambiar_show():
    global stock1, stock2

    print("-- cambiar show --")
    nombre = input("nombre del comprador: ").strip()

    if nombre not in compradores:
        print("error: comprador no existe.")
        return

    i = compradores.index(nombre)
    actual = funciones[i]
    nueva = 2 if actual == 1 else 1

    respuesta = input("cambiar de funcion {} a {}? (s/n): ".format(actual, nueva)).strip().lower()
    if respuesta != "s":
        print("cambio cancelado.")
        return

    if nueva == 1 and stock1 > 0:
        funciones[i] = 1
        stock1 -= 1
        stock2 += 1
        print("cambio exitoso. ahora esta en funcion 1.")
    elif nueva == 2 and stock2 > 0:
        funciones[i] = 2
        stock2 -= 1
        stock1 += 1
        print("cambio exitoso. ahora esta en funcion 2.")
    else:
        print("no hay stock disponible para el cambio.")

def mostrar_stock():
    print("-- totales de entradas --")
    print("función 1: disponibles {}, vendidas {}".format(stock1, 50 - stock1))
    print("función 2: disponibles {}, vendidas {}".format(stock2, 60 - stock2))

def menu():
    while True:
        print("\nmenu principal concierto movimiento origen")
        print("1.- comprar entrada.")
        print("2.- cambiar show.")
        print("3.- mostrar stock.")
        print("4.- salir.")
        opcion = input("seleccione una opcion: ").strip()

        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            cambiar_show()
        elif opcion == "3":
            mostrar_stock()
        elif opcion == "4":
            print("programa terminado...")
            break
        else:
            print("debe ingresar una opcion valida!!")


if __name__ == "__main__":
    menu()

