def tiquete():
    ciudad_origen = input('Ingrese ciudad de origen')
    ciudad_destino = input('Ingrese ciudad de destino')
    fecha_compra = input('Ingrese fecha de compra')
    hora_compra = input('Ingrese hora de compra')
    cantidad_puestos = 24
    nombre_pasajero = input('Ingrese nombre del pasajero')
    cedula = input('Ingrese cedula de ciudadania del pasajero')
    informe = print("""      TICKET BUSES TOTE LTDA 
    
    """, 'Ciudad origen: ', ciudad_origen, """
    """, 'Ciudad destino:', ciudad_destino, """
    """, 'Fecha_compra:', fecha_compra, """
    """, 'Hora_compra:', hora_compra, """
    """ )
tiquete() 
