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

