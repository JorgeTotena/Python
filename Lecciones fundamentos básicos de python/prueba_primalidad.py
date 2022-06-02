def es_primo(numero):
    contador = 0
   
    for i in range(1, numero + 1): #Para la variable i en rango de 1 a numero, haga lo siguiente (tener en cuenta que se le suma 1 a número porque no cuenta el últuimo valor)
        if i == 1 or i == numero:
            continue #rompe el código si el contador llega a ser 1 o alcanza el numero que fue ingresado, sigue con las demás lineaas  de codigo
        if numero % i == 0: # si el modulo llega a ser cero, es decir no es numero primo, sigue contando hasta que llegue al mismo numero
            contador += 1
    if contador == 0:
        return True #Si el contador no se incremento, significa que el número si es primo
    else:
        return False #Si el contador se incremento porque su modular era 0, entonces procesa que no es primo

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero) == True:  #Se puede omitir el == True ya que python lo puede entender de por si mismo
        print('es primo')
    else:
        print('No es primo')
    

if __name__ == '__main__':
    run()