def prenda():
    nombre_cliente = input("nombre cliente")
    contador = input('ingrese numero de comprobante')
    cantidad_prendas = int(input("Ingrese la cantidad de prendas"))
    valor_unitario = int(input("Ingrese el valor unitario de la prenda"))
    tipo_prenda = input(""" Escoja el tipo de prenda:
    1. Pantalon
    2. Camisa
    3. Ropa interior
    Ingrese su elección:  """)
    if tipo_prenda == '1':
        tipo_prenda = "Pantalon"
    elif tipo_prenda == '2':
        tipo_prenda = "Camisa"
    elif tipo_prenda == '3':
        tipo_prenda = "Ropa interior"
    else:
        print("el numero ingresado no es correcto")
    valor_total = valor_unitario * cantidad_prendas
    valor_pagar = valor_total
    print('Comprobante de Egreso numero', contador )
    print('Tipo de prenda: ', tipo_prenda)
    print('Cantidad de prendas: ', cantidad_prendas)
    print('Valor unitario: ',valor_unitario)
    print('Valor total', valor_pagar)
    print('Total a pagar: ', valor_total)
    print('Revise por favor este formulario, despues de dejar el establecimiento, no se aceptan reclamos')
      

def run():
    cuenta_cobro = prenda()

if __name__ == '__main__':
    run()
