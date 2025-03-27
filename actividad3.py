import math

'''
    Actividad 3: Escribir un programa que calcule el salario neto (el salario neto es el sueldo del trabajador después de descontarle los impuestos) 
    de un trabajador, el programa debe pedir el salario bruto del trabajador y el porcentaje de impuestos que se le descuenta. 
    El programa debe mostrar el salario neto del trabajador.
    
    => Inicialmente, el programa debe solicitar el tipo de trabajador: 
    
    A. Contrato a término indefinido 
    B. Contrato por prestación de servicios 
    C. Contrato de aprendizaje
    D. Jornal
    
    => Jornal:
    Se calcula como se debe solicitar:
    - El tipo de unidad a pagar 
    - El numero de unidades hechas
    - El valor de la unidad 
    
    * El salario del jornalero se calcula multiplicando el numero_unidades * valor_unidad 
    * Si el múmero de unidades es mayor a 100 
    * Se le da la bonificación del 10%
    
    => Contrato de Aprendizaje:

    
    
    
    => Contrato por prestación de Servicios:
    Se debe solicitar:
    
    - Valor del contrato
    - Número de meses trabajados
    - Antiguedad en la empresa
    
    * Se calcula dividiendo el valor de contrato sobre el número de meses trabajados
    * Si la antiguedad es menor a 2 años,
    * Se le hará una bonificación del 2% al salario mensual
    * Por el contrario si la antiguedad está entre 2 y 5 años 
    * Se le aumenta el 5% al salario mensual
    * Si la antiguedad es es mayor a 5 años 
    * Se le aumenta el 10% al salario mensual
    
    --- Descuento de ley ---  
    * 8% de Salud
    * 10% de pensión 
    * 1% de caja de pensión 
    
    
    => Contrato a término indefinido prestación de Servicios:
    El salario mínimo se calcula:
    
    - Con base en la siguiente tabla de escalafones o grados:
    
    * 1: El salario mensual es 1.5 veces el SMLV
    * 2: El salario mensual es 1.7 veces el SMLV
    * 3: El salario mensual es 2 veces el SMLV
    * 4: El salario mensual es 2.5 veces el SMLV
    * 5: El salario mensual es 3 veces el SMLV
    
    El programa debe solicitar el escalafón o grado del empleado
    
    - Las bonificaciones y descuentos de ley son las mismas que en el caso B

'''

# Variable global
# Variable que puede ser reconocida
# Y asignada en cualquier parte del
# programa

# NOTA: Se recomienda inicializar 
# definir y dar valor
# inicial a las variables globales al principio
# del programa

# Ejemplo de esto:
# Son las variables para almacenar resultados finales 

salario_neto = 0

tipo_trabajador = input("Ingrese el tipo de trabajador (A, B, C, D): ")
if tipo_trabajador.upper() == "A":
    print("Ha ingresado contrato a término indefinido")
    smlv = 1400000
    escalafon = int(input("Ingrese el escalafón (1, 2, 3, 4 o 5): "))    
    antiguedad_empresa = int(input("Ingrese el número años en la empresa: "))
    
    if escalafon == 1:
        salario_mensual = smlv * 1.5
    elif escalafon == 2:
        salario_mensual = smlv * 1.7
    elif escalafon == 3:
        salario_mensual = smlv * 2
    elif escalafon == 4:
        salario_mensual = smlv * 2.5
    elif escalafon == 5:
        salario_mensual = smlv * 3
        
    # Bonificación : elif anidados 
    
    bonificacion = 0
    
    if math.isnan(antiguedad_empresa) or antiguedad_empresa < 0:
        print("No es un valor válido")
    elif antiguedad_empresa < 2:
        bonificacion = salario_mensual + salario_mensual * 0.02
    elif antiguedad_empresa >= 2 and antiguedad_empresa <= 5: 
        bonificacion = salario_mensual + (salario_mensual * 0.05)
    elif antiguedad_empresa > 5:
        bonificacion = salario_mensual + (salario_mensual * 0.1)
   
    # Refactorización 

    salario_neto = salario_mensual + bonificacion
    
    # Descuentos 
    
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.1
    descuento_caja_pension = salario_mensual * 0.01
    
    salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja_pension + bonificacion
elif tipo_trabajador.upper() == "B":
    print("Ha ingresado contrato por prestación de servicios")
    valor_contrato = int(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese el número de meses trabajados: "))
    antiguedad_empresa = int(input("Ingrese el número años en la empresa: "))

    salario_mensual = valor_contrato/numero_meses
    
    # Bonificación : elif anidados 
    
    bonificacion = 0
    
    if math.isnan(antiguedad_empresa) or antiguedad_empresa < 0:
        print("No es un valor válido")
    elif antiguedad_empresa < 2:
        bonificacion = salario_mensual + (salario_mensual * 0.02)
    elif antiguedad_empresa >= 2 and antiguedad_empresa <= 5: 
        bonificacion = salario_mensual + (salario_mensual * 0.05)
    elif antiguedad_empresa > 5:
        bonificacion = salario_mensual + (salario_mensual * 0.1)
   
    # Refactorización 

    salario_mensual = salario_mensual + bonificacion
        
    # Descuentos 
    
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.1
    descuento_caja_pension = salario_mensual * 0.01
    
    salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja_pension + bonificacion
elif tipo_trabajador.upper() == "C":
    print("Ha ingresado contrato de aprendizaje")
    smlv = 1400000
    # Variables locales:
    # Solo pueden ser reconocidas y asignadas
    # En un bloque de código específico
    
    descuento = smlv * 0.25
        
    # Calculo del salario neto del trabajador de aprendizaje
    salario_neto = smlv - descuento
    print("El salario neto del trabajador es: ", salario_neto)
elif tipo_trabajador.upper() == "D":
    print("Ha ingresado Jornal")
    # Variables locales:
    # Solo pueden ser reconocidas y asignadas
    # En un bloque de código específico
    
    tipo_unidad = input("Ingrese el tipo de unidad: ")
    numero_de_unidades = int(input("Ingrese el número de unidades " + tipo_unidad + " hechas: "))
    valor_unidad = int(input("Ingrese el valor de " + tipo_unidad))
    porcentaje_impuestos = float(input("Ingrese el porcentaje de impuestos que se le descuenta: "))
    
    salario_bruto = (numero_de_unidades * valor_unidad)
    
    if numero_de_unidades > 100:
        salario_bruto = (salario_bruto + salario_bruto * 0.10)
        # Calculo del salario neto del trabajador jornal
        salario_neto = salario_bruto - (salario_bruto * porcentaje_impuestos / 100)
        print("El salario neto del trabajador es: ", salario_neto)
    else:
        # Calculo del salario neto del trabajador jornal
        salario_neto = salario_bruto - (salario_bruto * porcentaje_impuestos / 100)
        print("El salario neto del trabajador es: ", salario_neto)
else:
    print("Tipo de trabajador no valido")
    
print("El salario del empleado es de ", salario_neto)    

"""
    def calcular_salario_neto():
    tipo_trabajador = input("Ingrese el tipo de trabajador (A, B, C, D): ").upper()
    
    if tipo_trabajador in ["A", "B", "C", "D"]:
        salario_bruto = float(input("Ingrese el salario bruto del trabajador: "))
        porcentaje_impuestos = float(input("Ingrese el porcentaje de impuestos que se le descuenta: "))
        
        # Cálculo del salario neto
        salario_neto = salario_bruto - (salario_bruto * porcentaje_impuestos / 100)
        
        # Mostrar el resultado
        print(f"El salario neto del trabajador ({tipo_trabajador}) es: {salario_neto}")
    else:
        print("Tipo de trabajador no válido")

# Llamar a la función
calcular_salario_neto()
    
"""