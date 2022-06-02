def tiquete():
    ciudad_origen = input('Ingrese ciudad de origen')
    ciudad_destino = input('Ingrese ciudad de destino')
    fecha_compra = input('Ingrese fecha de compra')
    hora_compra = input('Ingrese hora de compra')
    cantidad_puestos = 24
    contador = 0
    nombre_pasajero = input('Ingrese nombre del pasajero')
    cedula = input('Ingrese cedula de ciudadania del pasajero')
    informe = print("""      TICKET BUSES TOTE LTDA   
    
    """, 'Ciudad origen: ', ciudad_origen, """
    """, 'Ciudad destino:', ciudad_destino, """
    """, 'Fecha compra:', fecha_compra, """
    """, 'Hora compra:', hora_compra, """
    """, 'Nombre pasajero: ', nombre_pasajero, """
    """, 'Cedula: ', cedula, """  
    """, 'Cupos disponibles: ', cantidad_puestos, """
    """, """
     El presente tiquete es valido por 30 dias
      no olvidar entregarlo para sello """,)
    return cantidad_puestos and contador
       
while cantidad_puestos > 0:
    contador = contador - 1
    cantidad_puestos = cantidad_puestos - contador
    tiquete()
        
        
        
        
        

  
        
  

      

     

