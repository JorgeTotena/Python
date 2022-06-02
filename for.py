""" contador = 1
print(contador) 
while contador < 1000:
    contador += 1
    print(contador) """
""" 
for contador in range(1, 1001): #para la variable contador en el rango de 1000, range hace un ciclo que va desde el 0 al número antes del rango
    print(contador)
 """
 
""" for i in range(10):
     print('su valor de tabla es ' + str(11 * i)) """

numero_tabla = input("Ingrese un número")
print("Esta es la tabla del" + numero_tabla)
numero_tabla = int(numero_tabla)
 
def tabla(numero_tabla):
       
    for resultado in range(1, 11):
        tablatotal = resultado * numero_tabla
        print(tablatotal)      
        
tabla(numero_tabla)
     