while True:
    print("Convertidor de tiempo")
    print("""
    1 - Minuto a Segundos
    \n2 - Segundos a Minutos
    \n3 - Horas a Minutos
    \n4 - Horas a Segundos
    \n5 - Minutos a Horas
    \n6 - Segundos a Horas
    \n7 - Horas a Dias
    \n8 - Dias a Meses
    \n9 - Meses a Dias
    \n10 - Años a Dias
    \n11 - apagar convertidor
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Minuto a Segundos")
        entrada = float(input("Ingresa la cantidad en Minutos: "))
        resultado = round(entrada*60)
    elif opcion == 2:
        print("Segundos a Minutos")
        entrada = float(input("Ingresa la cantidad en Segundos: "))
        resultado = round(entrada/60)
    elif opcion == 3:
        print("Horas a Minutos")
        entrada = float(input("Ingresa la cantidad en Horas: "))
        resultado = round(entrada*60)
    elif opcion == 4:
        print("Horas a Segundos")
        entrada = float(input("Ingresa la cantidad en Horas: "))
        resultado = round(entrada/3600)
    elif opcion == 5:
        print("Minutos a Horas")
        entrada = float(input("Ingresa la cantidad en Minutos: "))
        resultado = round(entrada/60)
    elif opcion == 6:
        print("Segundos a Horas")
        entrada = float(input("Ingresa la cantidad en Segundos: "))
        resultado = round(entrada/3600)
    elif opcion == 7:
        print("Horas a Dias")
        entrada = float(input("Ingresa la cantidad en Horas: "))
        resultado = round(entrada/24)
    elif opcion == 8:
        print("Dias a Meses")
        entrada = float(input("Ingresa la cantidad en Dias: "))
        resultado = round(entrada/30.417)
    elif opcion == 9:
        print("Meses a Dias")
        entrada = float(input("Ingresa la cantidad en Meses: "))
        resultado = round(entrada*30.417)
    elif opcion == 10:
        print("Años a Dias")
        entrada = float(input("Ingresa la cantidad en Años: "))
        resultado = round(entrada*365)
    elif opcion == 11:
        break
    print("El resultado de la conversión es: {} ".format(resultado))
