from datetime import datetime #importar diccionario para fechas y horas
cantidad_puestos = 24 #hay que definir la función por fuera si la quieres usar luego en un ciclo while porque las variables dentro de funciones son inservibles en el ambito global
puesto_pasajero = 0
def tiquete(): 
    ciudad_origen = input('Ingrese ciudad de origen')
    ciudad_destino = input('Ingrese ciudad de destino')
    puestos_restantes = cantidad_puestos #para lograr su modificación se debe definir otra función
    puesto = puesto_pasajero
    nombre_pasajero = input('Ingrese nombre del pasajero')
    cedula = input('Ingrese cedula de ciudadania del pasajero') 
    informe = print("""      TICKET BUSES TOTE LTDA   
    
    """, 'Ciudad origen: ', ciudad_origen, """
    """, 'Ciudad destino:', ciudad_destino, """
    """, 'Fecha compra:', datetime.today() , """ 
    """, 'Nombre pasajero: ', nombre_pasajero, """
    """, 'Cedula: ', cedula, """  
    """, 'Cupos disponibles: ', puestos_restantes , """
    """, 'Puesto asignado: ', puesto , """
    """, """
     El presente tiquete es valido por 30 dias
      no olvidar entregarlo para sello """,)
    
while cantidad_puestos > 0:
    cantidad_puestos = cantidad_puestos - 1
    puesto_pasajero += 1
    tiquete()    
        