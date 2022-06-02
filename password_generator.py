import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolo = ['!', '#', '$', '&', '/', '(',')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    """Caracteres de diferente tipo que luego seran unidos por una suma de string en una lista"""

    caracteres = mayusculas + minusculas + simbolo + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres) #random.choice escoge un caracter random de una variable ya establecida
        contrasena.append(caracter_random)
            
    contrasena = "".join(contrasena)
    return contrasena """los returns se ponen por fuera de los ciclos en linea con la indentación de las funciones""" 
    """convertir una lista en un string"""

def run():
    contrasena = generar_contrasena()
    print('your new password is: ' + contrasena)

if __name__ == '__main__':
    run()
