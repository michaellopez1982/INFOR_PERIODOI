while True:
    print("Convertidor de Hectareas")
    print("""
1 - Hectarea a metro cuadrado
    \n2 - Hectarea a centimetro cubico
    \n3 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Hectarea a metro cuadrado")
        entrada = float(input("Ingresa la cantidad en Hectareas: "))
        resultado = round(entrada*10000)
    elif opcion == 2:
        print("Hectarea a centimetro cubico")
        entrada = float(input("Ingresa la cantidad en Hectareas: "))
        resultado = round(entrada/100000000)
    elif opcion == 3:
        break
    print("El resultado de la conversión es: {} ".format(resultado))
