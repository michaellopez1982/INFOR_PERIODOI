while True:
    print("Convertidor de volumen")
    print("""
1 - Kilómetro cúbico a Metro Cubico
    \n2 - Hectómetro cúbico a Metro Cubico
    \n3 - Decametro cubico a Metro Cubico
    \n4 - Metro Cubico a Kilometro cubico
    \n5 - Metro Cubico a Hectometro cubico
    \n6 - Metro Cubico a Decametro cubico
    \n7 - Decimetro cubico a Metro Cubico
    \n8 - Centimetro cubico a Metro Cubico
    \n9 - Milimetro cubico a Metro Cubico
    \n11 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Kilómetro cúbico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Kilometros cubicos: "))
        resultado = round(entrada*1000000000)
    elif opcion == 2:
        print("Hectómetro cúbico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Hectometro cubico: "))
        resultado = round(entrada*1000000)
    elif opcion == 3:
        print("Decametro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Decametros cubicos: "))
        resultado = round(entrada*1000)
    elif opcion == 4:
        print("Metro Cubico a Kilometro cubico")
        entrada = float(input("Ingresa la cantidad en Metro cubico: "))
        resultado = round(entrada/1000000000)
    elif opcion == 5:
        print("Metro Cubico a Hectometro cubico")
        entrada = float(input("Ingresa la cantidad en Metros Cubicos: "))
        resultado = round(entrada/1000000)
    elif opcion == 6:
        print("Metro Cubico a Decametro cubico")
        entrada = float(input("Ingresa la cantidad en Metros cubicos: "))
        resultado = round(entrada/1000)
    elif opcion == 7:
        print("Decimetro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Decimetros cubicos: "))
        resultado = round(entrada*0.001)
    elif opcion == 8:
        print("Centimetro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Centimetros cubicos: "))
        resultado = round(entrada*0.000001)
    elif opcion == 9:
        print("Milimetro cubico a Metro Cubico")
        entrada = float(input("Ingresa la cantidad en Milimetros cubicos: "))
        resultado = round(entrada*0.000000001)
    elif opcion == 11:
        break
    print("El resultado de la conversión es: {} ".format(resultado))
