def run():
    contador = 0 
    numero_ingreso = int(input('Ingrese un número: '))
    operacion_número = numero_ingreso * contador
    while operacion_número <= 1000:
        print (operacion_número)
        contador = contador + 1
        operacion_número = numero_ingreso * contador
        if operacion_número >= 100:
            break

    
  
if __name__ == '__main__':
    run()