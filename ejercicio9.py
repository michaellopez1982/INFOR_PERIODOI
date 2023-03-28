while True:
    print("""
1 - Centrímetros a Decímetros
    \n2 - Decímetros a Centrímetros
    \n3 - Decímetros a Metros
    \n4 - Metros a Decímetros
    \n5 - Metros a Decámetros
    \n6 - Decámetros a Metros
    \n7 - Decámetros a Hectómetros
    \n8 - Hectómetros a Decámetros
    \n9 - Hectómetros a Kilómetros
    \n10 - Kilómetros a Hectómetros """)
  
    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))

 
    if opcion == 1:
        print("Centrímetros a Decímetros")
        entrada = float(input("Ingresa la cantidad en Centrímetros: "))
        resultado = round(entrada/10)
    
    elif opcion == 2:
        print("Decímetros a Centímetros")
        entrada = float(input("Ingresa la cantidad en Decímetros: "))
        resultado = round(entrada*10)

    if opcion == 3:
     print("Decímetros a Metros")
     entrada = float(input("Ingresa la cantidad en Decímetros "))
     resultado = round(entrada/10)

    if opcion == 4:
     print("Metros a Decímetros")
     entrada = float(input("Ingresa la cantidad en Metros "))
     resultado = round(entrada*10)

    if opcion == 5:
      print("Metros a Decámetros")
      entrada = float(input("Ingresa la cantidad en Metros "))
      resultado = round(entrada/10)

    if opcion == 6:
      print("Decámetros a Metros")
      entrada = float(input("Ingresa la cantidad en Decámetros "))
      resultado = round(entrada*10)

    if opcion == 7:
      print("Decámetros a Hectómetro")
      entrada = float(input("Ingresa la cantidad en Decámetros "))
      resultado = round(entrada/10)

    if opcion == 8:
      print("Hectómetro a Decámetros")
      entrada = float(input("Ingresa la cantidad en Hectómetro "))
      resultado = round(entrada*10)

    if opcion == 9:
      print("Hectómetro a Kilómetro")
      entrada = float(input("Ingresa la cantidad en Hectómetro "))
      resultado = round(entrada/10)

    if opcion == 10:
      print("Kilómetro a Hectómetro")
      entrada = float(input("Ingresa la cantidad en Kilómetro "))
      resultado = round(entrada/10)


      

    print("El resultado de la conversión es: {} ".format(resultado))
