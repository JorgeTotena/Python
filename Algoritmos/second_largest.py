# def second_largest():
#     numbers = [13, 4, 5, 8, 7]
#     numbers.sort()
#     numbers.insert(-1: 4)
#     print(numbers)
# second_largest()

def second_largest(numeros): #it's necessary to define the parameters for numeros and the list
    if isinstance(numeros, list): #isinstance is used to check if an object is from a specific type of field
        if len(numeros) < 2: #Because if the list has less than 2 elements, it wouldn't be a list
            return None

        if len(numeros) == 2 and numeros[0] == numeros[1]: # si hay dos números en la lista y sus posiciones son iguales, return none
            return None
        
        duplicados = set() # set es para establecer un conjunto, aqui se encuentran los elementos duplicados de la lista
        unicos = [] #aqui van los elementos vacios con los números únicos de la lista
        
        for n in numeros:
            if n not in duplicados: #Si la variable de interacción no está en duplicados
                duplicados.add(n) #se agrega el elemento a la variable duplicados
                unicos.append(n)
        #en los conjuntos no existe el concepto de orden, sin embargo en las listas si, por eso se toman los valores unicos en vez de los duplicados
        
        unicos.sort() #se ordenan de menor a mayor para poder hayar la posicion que necesitamos 

        return unicos[-2] #devuelve la posición penuntilma posición)

    raise TypeError("El parametro numeros debe ser una lista")

numeros = [1, 3, 7, 9, 11, 13, -5, -1, 8, 16, 14 ]

print(second_largest(numeros))






    


