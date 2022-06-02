def palindromo(palabra):
    palabra = palabra.replace(' ', '') #Para hacer el palindromo, es necesario remplazar los espacios de la variable por no espacios, para que cuente la misma cantidad de caracteres
    palabra = palabra.lower() #porque los caracteres del palindromo necesitan ser iguales, no algunos en mayúsculas y otros en minúsculas 
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True #me devuelve el valor true si efectivamente es palindromo para usarlo en otra función"
    else:
        return False

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra) #me conviernte a la función palindromo en lo que el usuario ingrese por teclado
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()