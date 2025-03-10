'''
operadores logicos
 
 Aquellos que operan unicamente 
 con valores booleanos (v f)
 Acorde a las tablas de Verdad
'''

#Ejemplo 1 Operador not:
y = not True
print ("el valor o resultado de operar con not es", y) 
 
 # ejemplo: 2 operador and
y = False and True
print ("el resultado de operar con and es", y)


#ejemplo 3 :operador or 
y = False or True
print ("El resultado de operar con or es", y)

'''
Jerarquia de precedencia de operadores 
(logicos inclusive)
1             ()
2             **
3             *, /, %
4             +,-
5             >,<, >=, <=, !=, ==
6             not
7             and
8             or
9             =
'''
 # ejemplo 4 : jerarquia de operadores
y = False and not True or False
print( "el resultado de operar con jerarquia de operadores es" , y)

#ejemplo 5 : operadores relacionales y logicos 
y = not 3 > 4 and 4 == 4 or 3 < 2
print( "el resultado de operar con relacionales y logicos es" , y)


# ejemplo 6 : operadores aritmeticos
# relacionales y logicos
y = 3 + 5 * 2 > 3 and 4 == 4 or 3 < 2
print( "el resultado de operar con operadores aritmeticos es" , y)

#ejemplo 7 con parentesis
y = (3 + 5 != 2 > 3) and 4 == 4 or not 3 < 2
print("el resultado con parentesis es", y)

#ejemplo 8 : todo junto
y =4 ** 2 * 3 < 6 /(7 - 5) and 7 * 2 + 1 == 14 or not 3 + 5 > 2 
print("el resultado de operar todo junto es", y)