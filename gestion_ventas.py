# gestion_ventas.py
# Registrar ventas y botón de arrepentimiento
from datetime import datetime
from crudDB import insertar_venta, listar_ventas, anular_venta, buscar_venta, buscar_cliente,buscar_destino
def menu_gestion_ventas():
    print("\nIngresaste al Submenu Gestion Ventas...")
    while True:
        print("\n--- Gestión de Venta ---")
        print("1. Consulta Venta")
        print("2. Nueva Venta")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        #Consulta Venta
        if opcion == "1":
            # Realiza un listado de todos los Ventas
            print("\n** Has elegido la opción: Consulta Ventas")
            print("Se listan todos los Ventas")
            listar_ventas()

        #Agrega Venta
        elif opcion == "2":
            print("\n ** Has elegido la opción: Agregar Venta")
            #Se piden los datos del Venta (destino, cliente, fecha) 
            
            idClienteVenta = input("Ingrese el Cliente del viaje: ")
            clienteEncontrado= buscar_cliente(idClienteVenta)
            
            if clienteEncontrado:
                print(clienteEncontrado)
                idDestinoVenta = input("\nIngrese el Destino de Viaje: ") 
                # se busca el Destino con el id indicado y se procede a solicitar los atributos a modificar (pais, ciudad o costo)
                destinoEncontrado= buscar_destino(idDestinoVenta)
                
                if destinoEncontrado:

                    print(destinoEncontrado)
                    #Solicitar los datos a modificar(PAIS - CIUDAD o COSTO) y hacer update 
                    mensaje = insertar_venta(idDestinoVenta, idClienteVenta)
                    print(mensaje)
                else: 
                    print("No encontro el destino. Intente nuevamente.")
            else:
                print("No se encontró el cliente.Intente nuevamente")
        #Volver al menu principal
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def boton_arrepentimiento():
    print("\n** Has elegido la opción: BOTON ARREPENTIMIENTO")
    print("\nDe acuerdo al derecho de arrepentimiento, podés cancelar tu compra dentro de los 60 días corridos de haberla realizado.\n* Según Resolución 329/2020 ANAC el derecho de arrepentimiento no aplica para vuelos y estos se rigen por la política de devolución informada en tu voucher.")

    #Solicita el id de la Venta, para validar que exista y que este entre los 60 dias habiles 
    idVenta = input("Ingrese el ID Venta (comprobante de venta) -- SOLO NUMEROS: ")

    #Valida que el comprobante sea un numero
    if idVenta.isdigit():
        idVenta = int(idVenta)
         
         #Busca en la tabla si existe algun registro con ese id
        ventaEncontrada = buscar_venta(idVenta)  
        
        #En este punto se implementa un bucle para realizar la busqueda de la venta segun el comprobante ingresado
        if not ventaEncontrada:
            print("\n__________________________________________________")
            print(f"No se encontraron ventas para anular con ese comprobante: {idVenta}.")
            print("__________________________________________________")
        else:
            # Muestra los detalles de la venta y se actualiza el estado a ANULADA
            print("\n--- DETALLE DE LA VENTA A ANULAR ---")
            print("-" * 90)
            print(ventaEncontrada)  
            print("-" * 90) 
            # Preguntar al usuario si confirma la ANULACION
            respuesta = input("\n ¿Estás seguro  ANULAS el viaje? (s/n): ").lower()

            if respuesta == "s" or respuesta == "sí":
                    
                # Se hace update a ANULADA
                mensaje = anular_venta(idVenta)
                print(mensaje)          
            else:
                print("\n Cancelo la anulacion de la venta")           
    else:
        print("El numero de comprobante debe ser un número entero.")