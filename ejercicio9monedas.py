
print("Convertidor de monedas")
print("1 - USD a Euro\n2 - USD a Libra esterlina\n3 - USD a Yen japonés\n4 - USD a Peso argentino\n5 - USD a Real brasileño\n6 - USD a Peso colombiano\n7 - USD a Quetzal guatemalteco\n8 - USD a Won surcoreano\n9 -USD a Lira turca \n10 - USD a Rupia india")
opcion = float(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = float(0)
 
if opcion == 1:
    print("USD a Euro")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*0.93348)
elif opcion == 2:
    print("USD a Libra esterlina")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*0.82452)
elif opcion == 3:
    print("USD a Yen japonés")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*133.584)
elif opcion == 4:
    print("USD a Peso argentino")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*199.985)
elif opcion == 5:
    print("USD a Real brasileño")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*5.2305)
elif opcion == 6:
    print("USD a Peso colombiano")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*4728.77)
elif opcion == 7:
    print("USD a Quetzal guatemalteco")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*7.60357)
elif opcion == 8:
    print("USD a Won surcoreano")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*1302.2)
elif opcion == 9:
    print("USD a Lira turca")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*18.9655)
elif opcion == 10:
    print("USD a Rupia india")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*82.1366)

 
print("El resultado de la conversión es: {0:.2f} ".format(resultado))
