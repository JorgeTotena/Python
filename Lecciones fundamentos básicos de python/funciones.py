#def imprimir_mensaje():
 ##  print("Estoy aprendiendo a usar funciones ")

#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

"""
opcion = int(input("Elige una opción: 1, 2, 3 "))
def conversacion(mensaje):
    print("Hola soy maria de los angeles")
    print(mensaje)
if opcion == 1:
   conversacion("Elegiste la opción 1")
elif opcion ==2:
    conversacion("Elegiste la opción 2")
elif opcion ==3:
    conversacion("Elegiste la opción 3")
else:
    print("Choose a valid option") 
"""

# def suma(a, b):
#     resultado = a + b
#     return resultado

# resultado_suma = suma(3,4)
# print(resultado_suma)

def suma(a, b):
    resultado = a + b
    return resultado

numero1 = int(input('Ingrese un numero'))
numero2 = int(input('Ingrese otro numero'))
resultado_suma = suma(numero1, numero2)
print("el resultado de su suma es", resultado_suma)