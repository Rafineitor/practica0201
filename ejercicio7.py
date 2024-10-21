#Ejercicio7

peso = input("Introduce tu peso en kilogramos: ")
estatura = input("Introduce tu estatura en metros: ")
peso = float(peso)
estatura = float(estatura)
imc = peso/(estatura**2)
print ("Tu índice de masa corporal es", round(imc,2))