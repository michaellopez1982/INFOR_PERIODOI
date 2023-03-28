while True:
    print("Convertidor de area")
    print("""
    1 - kilómetro cuadrado a Hectómetro cuadrado	
    \n2 - Hectómetro cuadrado a kilómetro cuadrado
    \n3 - Decámetro cuadrado a Hectómetro cuadrado
    \n4 - Hectómetro cuadrado a Decámetro cuadrado
    \n5 - Decámetro cuadrado a Metro cuadrado
    \n6 - Metro cuadrado a Decámetro cuadrado
    \n7 - Decámetro cuadrado a Metro cuadrado
    \n8 - Metro cuadrado a Decámetro cuadrado
    \n9 - Decímetro cuadrado a Centímetro cuadrado
    \n10 - Centímetro cuadrado a Decímetro cuadrado
    \n11 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("kilómetro cuadrado a Hectómetro cuadrado	")
        entrada = float(input("Ingresa la cantidad en kilómetro cuadrado: "))
        resultado = round(entrada*100)
    elif opcion == 2:
        print("Hectómetro cuadrado a kilómetro cuadrado")
        entrada = float(input("Ingresa la cantidad en Hectómetro cuadrado: "))
        resultado = round(entrada/100)
    elif opcion == 3:
        print("Decámetro cuadrado a Hectómetro cuadrado")
        entrada = float(input("Ingresa la cantidad en Decámetro cuadrado: "))
        resultado = round(entrada/100)
    elif opcion == 4:
        print("Hectómetro cuadrado a Decámetro cuadrado")
        entrada = float(input("Ingresa la cantidad en Hectómetro cuadrado: "))
        resultado = round(entrada*100)
    elif opcion == 5:
        print("Decámetro cuadrado a Metro cuadrado")
        entrada = float(input("Ingresa la cantidad en Decámetro cuadrado: "))
        resultado = round(entrada*100)
    elif opcion == 6:
        print("Metro cuadrado a Decámetro cuadrado")
        entrada = float(input("Ingresa la cantidad en Metro cuadrado: "))
        resultado = round(entrada/100)
    elif opcion == 7:
        print("Decámetro cuadrado a Metro cuadrado")
        entrada = float(input("Ingresa la cantidad en Decámetro cuadrado: "))
        resultado = round(entrada*100)
    elif opcion == 8:
        print("Metro cuadrado a Decámetro cuadrado")
        entrada = float(input("Ingresa la cantidad en hectogramos: "))
        resultado = round(entrada/100)
    elif opcion == 9:
        print("Decímetro cuadrado a Centímetro cuadrado")
        entrada = float(input("Ingresa la cantidad en Decímetro cuadrado: "))
        resultado = round(entrada*100)
    elif opcion == 10:
        print("Centímetro cuadrado a Decímetro cuadrado")
        entrada = float(input("Ingresa la cantidad en Centímetro cuadrado: "))
        resultado = round(entrada/100)
    elif opcion == 11:
        break
    print("El resultado de la conversión es: {} ".format(resultado))

