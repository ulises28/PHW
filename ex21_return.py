def suma(a,b):
    print(f"Suma de {a} + {b}")
    return a + b

def resta(a,b):
    print(f"Resta de {a} - {b}")
    return a - b

def multiplicacion(a,b):
    print(f"Multiplicacion de {a} * {b}")
    return a * b

def division(a,b):
    print(f"Division de {a} / {b}")
    return a / b

edad = resta (2019, 1990)
peso = suma (69,2)
altura = division(175,100)
iq = multiplicacion(60,2)

print(f"La edad del individuo es {edad}, tiene un peso de {peso}, una altura de {altura}cm y un IQ de {iq}")

print("Ejercicio extra")

conjuntoFunciones = suma(edad, resta(altura, multiplicacion(peso, division(iq,2))))

print(f"El conjunto de funciones equivale a {conjuntoFunciones}, donde se utilizaron funciones como argumentos")
