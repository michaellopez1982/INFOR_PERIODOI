
print("Convertidor de Manzanas")
print("1 - Manzanas a Varas Cuadradas\n2 - Manzanas a Metros Cuadrados \n3 - Manzanas a Pies\n4 - Manzanas a  Acres\n5 - Manzanas a Hectarea\n6 - Varas cuadradas a Manzanas\n7 - Metros Cuadrados a Manzanas\n8 - Pies a Manzanas\n9 - Acres a Manzanas\n10 - Hectarea a Manzanas")
opcion = float(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = float(0)
 
if opcion == 1:
    print("Manzanas a Varas Cuadradas")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*10000)
elif opcion == 2:
    print("Manzanas a Metros Cuadrados")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*6988)
elif opcion == 3:
    print("Manzanas a Pies")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*75220.68)
elif opcion == 4:
    print("Manzanas a  Acres")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*1.72677)
elif opcion == 5:
    print("Manzanas a Hectarea")
    entrada = float(input("Ingresa la cantidad en Manzanas: "))
    resultado = float(entrada*0.6988)
elif opcion == 6:
    print("Varas cuadradas a Manzanas")
    entrada = float(input("Ingresa la cantidad en Varas cuadradas: "))
    resultado = float(entrada/10000)
elif opcion == 7:
    print("Metros Cuadrados a Manzanas")
    entrada = float(input("Ingresa la cantidad en Metros Cuadrados: "))
    resultado = float(entrada/6988)
elif opcion == 8:
    print("Pies a Manzanas")
    entrada = float(input("Ingresa la cantidad en Pies: "))
    resultado = float(entrada/75220.68)
elif opcion == 9:
    print("Acres a Manzanas")
    entrada = float(input("Ingresa la cantidad en Acres: "))
    resultado = float(entrada/1.72677)
elif opcion == 10:
    print("Hectarea a Manzanas")
    entrada = float(input("Ingresa la cantidad en Hectarea: "))
    resultado = float(entrada/0.6988)


 
print("El resultado de la conversión es: {0:.4f} ".format(resultado))
