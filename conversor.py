def conversor(tipo_pesos, valor_dolar):
    pesos = input( "¿Cuántos pesos " + tipo_pesos + " tienes?")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
menu = """
Bienvenido al conversor de monedas 😍🤑

1. Pesos Colombianos
2. Pesos Mexicanos
3. Pesos Chilenos 

Elige una opcion en números:
"""
opcion = input(menu)
if opcion == "1":
    conversor("colombianos", 3794)
elif opcion == "2":
    conversor("mexicanos", 19.88)
elif opcion == "3":
    conversor("chilenos", 766.57)
else:
    print("Usted no escogió una opción en números")
