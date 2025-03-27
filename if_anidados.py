import unicodedata

'''
If anidados estructuras selectivas 
que se encuentran dentro de otro if

Syntax:

if condicion1:
    if condicion:
        bloque de código (Instrucción)
    else:
        bloque de código (Instrucción)
else:
    bloque de código (Instrucción)
'''

# Ejemplo 1
# Modificación del ejercicio de votación,
# ahora solo puede votar si el votante es mayor de edad
# pero si tiene su documento
# mostrar explicaciones en los otros casos

def normalizar_texto(texto):
    # Elimina tildes y convierte a minúsculas
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    documento = input("¿Tiene su documento? (si/no): ")
    documento_normalizado = normalizar_texto(documento)
    if documento_normalizado == "si":
        print("Usted puede votar")
        if edad >= 70:
            print("Usted puede votar y es de la tercera edad")
        if edad > 100:
            print("Usted puede votar y es un sobreviviente")
    elif documento_normalizado == "no":
        print("Usted no puede votar, no tiene su documento")
        print("Vuelva cuando tenga su documento")
    else:
        print("Respuesta no valida")
else: 
    print("Usted no puede votar, es menor de edad")
    print("Vuelva cuando cumpla 18 años")