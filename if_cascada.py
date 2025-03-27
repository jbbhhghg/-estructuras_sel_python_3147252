'''
if en casada:
Estructura de control que permite 
evaluar varias condiciones en,
casada es decir si la primera 
condicion no se cumple,
se evalua la siguiente y asi sucesivamente.
'''
# ejemplo 1:
# modificar el programa de votacion 
# para que considere la edades de 17 
# años

edad = int(input("Ingresa tu edad:"))

if edad > 18:
    print("puedes votar")
elif edad ==18:
    print("bienvenido ciudadano, puedes votar")
elif edad == 17:
    print("puedes votar el proximo año")
elif edad >= 10 :
    print("eres muy menor, tienes registro civil")
elif edad < 17:
    print("no puedes votar aun")

print("fin del programa")