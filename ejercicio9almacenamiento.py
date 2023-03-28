while True:
    print("Convertidor de almacenamiento")
    print("""
1 - Kilobyte a Bytes
    \n2 - Megabyte a Kilobyte
    \n3 - Gigabyte a Megabyte
    \n4 - Terabyte a Gigabyte
    \n5 - Petabyte a Terabyte
    \n6 - Exabyte a Petabyte
    \n7 - Zettabyte a Exabyte
    \n8 - Yottabyte a Zetabyte
    """)

    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    resultado = 0

    if opcion == 1:
        print("Kilobyte a Bytes")
        entrada = float(input("Ingresa la cantidad en kilobyte: "))
        resultado = round(entrada*1024)
    elif opcion == 2:
        print("Megabyte a Kilobyte")
        entrada = float(input("Ingresa la cantidad en Megabytes: "))
        resultado = round(entrada*1024)
    elif opcion == 3:
        print("Gigabyte a Megabyte")
        entrada = float(input("Ingresa la cantidad en Gigabytes: "))
        resultado = round(entrada*1024)
    elif opcion == 4:
        print("Terabyte a Gigabyte")
        entrada = float(input("Ingresa la cantidad en Terabytes: "))
        resultado = round(entrada*1024)
    elif opcion == 5:
        print("Petabyte a Terabyte")
        entrada = float(input("Ingresa la cantidad en Petabytes: "))
        resultado = round(entrada*1024)
    elif opcion == 6:
        print("Exabyte a Petabyte")
        entrada = float(input("Ingresa la cantidad en Exabytes: "))
        resultado = round(entrada*1024)
    elif opcion == 7:
        print("Yottabyte a Zetabyte")
        entrada = float(input("Ingresa la cantidad en Yottabytes: "))
        resultado = round(entrada*1024)
    elif opcion == 8:
        break
    print("El resultado de la conversión es: {} ".format(resultado))
