#Ejercicio9

capital_inicial = input("Ingrese el capital inicial: ")
interes_anual = input("Ingrese tasa de interes anual: ")
años = input("Ingrese la cantidad de años: ")
capital_inicial = float(capital_inicial)
interes_anual = float(interes_anual)
años = float(años)
capital_obtenido = capital_inicial*((1 + interes_anual)**años)

print ("El capital obtenido en la inversión es de ",capital_obtenido)