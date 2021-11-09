def conversorSoles (valorDollar):
    soles = int(input("Cuantos soles tienes "))
    soles = float(soles)
    dolares = soles / valorDollar
    dolares = round(dolares,2)
    dolares = str(dolares)

    print("Tienes $ ", str(dolares ) + " dolares"  )

def conversorPesos (tipoPesos, valorDollar ):
    pesos = int(input("Cuantos pesos " + tipoPesos +  "tienes "))
    pesos = float(pesos)
    dolares = pesos / valorDollar
    dolares = round(dolares,2)
    dolares = str(dolares)

    print("Tienes $ ", str(dolares ) + " dolares"  )



menu = """
Escoge moneda a convertir

1 - Soles Peruanos
2 - Pesos Colombianos
3 - Pesos Mexicanos
4 - Pesos Argentinos
5 - Pesos Chilenos
6 - Pesos Uruguayos
7 - Pesos Dominicanos
"""

print(menu)
opcion = int(input("Escoge la opcion"))

if opcion == 1:
    conversorSoles(4.01)
    
if opcion == 2:
    conversorPesos("colombianos ", 3772.77 )
    

if opcion == 3:
    conversorPesos("mexicanos ", 20.80)
    

if opcion == 4:
    conversorPesos("argentinos ", 99.83)
   
if opcion == 5:
    conversorPesos("chilenos ", 813.01)
   
if opcion == 6:
    conversorPesos("uruguayos ", 44.19)
   
if opcion == 7:
    conversorPesos("dominicanos ", 56.45)
   




