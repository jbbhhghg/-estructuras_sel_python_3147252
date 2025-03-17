'''elabore un programa
en python que determine si usted puede:
a)casarse
b)comprometerse
c)quedarse soltero
can base a las siguientes 
caracteristicas(variantes):
- estado_civil (string=
               "soltero", "casado", "comprometido",) 
- edad(int)
- temperamento(string=
                "buena persona", "mala persona")
- fisico (string
                 "lindo/a", "feo/a")                
'''
estado_civil = input("Ingresa tu estado civil (soltero, casado, comprometido):")
edad = int(input("Ingresa tu edad:"))
temperamento =input("Ingresa tu temperamento:(buena persona/mala persona):")
fisico = input("Ingresa tu fisico:(lindo/a, feo/a):")
salario = int(input("ingresa tu dinero actual:"))
if estado_civil == "casado" or estado_civil == "comprometido":
    print("No puedes acercarte a esa persona")
elif edad < 18:
    print("No puedes acercarte a esa persona, porque no tines la edad suficiente")
elif temperamento == "mala persona":
    print("No puedes acercarte aesa persona, porque te generaria estres")
elif fisico == "feo":
    print("No puedes acercarte a esa persona, porque no te atrae fisicamente")
elif salario < 100000:
    print("no puedes acercarte a esa persona porque no tienes suficiente dinero")
else:
    print("Puedes acercarte a esa persona")
print("fin del programa")