bisiesto = int(input("Ingresa el año para saber si es bisiesto: "))
if (bisiesto % 4 == 0 and bisiesto % 100 != 0) or bisiesto % 400 == 0:
    print("El año :", bisiesto, " es bisiesto")
else:
    print("El año: ", bisiesto, "no es bisiesto")
