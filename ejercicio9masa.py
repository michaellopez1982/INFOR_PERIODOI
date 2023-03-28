while True:
    print("Convertidor de masas")
    print("""
    1 - Kilogramos a Gramos
    \n2 - Gramos a Kilogramos
    \n3 - libras a gramos
    \n4 - gramos a libras
    \n5 - libras a kilogramos
    \n6 - kilogramos a libras
    \n7 - kilogramos a hectogramos
    \n8 - hectogramos a kilogramos
    \n9 - decagramo a gramo
    \n10 - gramo a decagramo
    \n11 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Kilogramos a Gramos")
        entrada = float(input("Ingresa la cantidad en kilogramos: "))
        resultado = round(entrada*1000)
    elif opcion == 2:
        print("Gramos a Kilogramos")
        entrada = float(input("Ingresa la cantidad en Gramos: "))
        resultado = round(entrada/1000)
    elif opcion == 3:
        print("libras a gramos")
        entrada = float(input("Ingresa la cantidad en libras: "))
        resultado = round(entrada*453.6)
    elif opcion == 4:
        print("gramos a libras")
        entrada = float(input("Ingresa la cantidad en gramos: "))
        resultado = round(entrada/453.6)
    elif opcion == 5:
        print("libras a kilogramos")
        entrada = float(input("Ingresa la cantidad en libras: "))
        resultado = round(entrada/2.205)
    elif opcion == 6:
        print("kilogramos a libras")
        entrada = float(input("Ingresa la cantidad en Kilogramos: "))
        resultado = round(entrada*2.205)
    elif opcion == 7:
        print("kilogramos a hectogramos")
        entrada = float(input("Ingresa la cantidad en Kilogramos: "))
        resultado = round(entrada*10)
    elif opcion == 8:
        print("Hectogramos a kilogramos")
        entrada = float(input("Ingresa la cantidad en hectogramos: "))
        resultado = round(entrada/10)
    elif opcion == 9:
        print("decagramo a gramo")
        entrada = float(input("Ingresa la cantidad en decagramo: "))
        resultado = round(entrada*10)
    elif opcion == 10:
        print("gramo a decagramo")
        entrada = float(input("Ingresa la cantidad en gramo: "))
        resultado = round(entrada/10)
    elif opcion == 11:
        break
    print("El resultado de la conversión es: {} ".format(resultado))

