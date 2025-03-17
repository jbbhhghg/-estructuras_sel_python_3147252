'''
estructura de control if
se utiliza para tomar decisiones
basadas en expresioines condicionales
'''
  #ejemplo 1 : if  SIMPLE
edad = int(input("ingresa tu edad:"))

documento = input("Tienes documento?(si/no):")
    #condicional: si la edad es mayor o igual a 18
if edad >= 18 and documento== 'si':
    #codigo para cuando es mayor a 18
 print("eres mayor de edad, puedes votar")     
else:
    #codigo cuando eres menor a 18
 print("eres menor de edad o no tienes documento ,no puedes votar")  
#codigo que se ejecuta siempre
print("fin del programa")
 