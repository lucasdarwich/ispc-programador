# gestion_ventas.py
# Registrar ventas y botón de arrepentimiento

from conexion_base_datos import insertar_venta, listar_ventas, anular_venta

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
            idDestinoVenta = input("\nIngrese el Destino de Viaje: ")
            #nombreDestino = función para encontrar nombre destino según el idDestinoVenta y costo del destino para informar al usuario
            nombreDestino = "Pais-Ciudad Prueba"  # Placeholder
            costoDestino = 9999999.99  # Placeholder

            idClienteVenta = input("Ingrese el Cliente del viaje: ")
            #nombreCliente = función de búsqueda del nombre según idClienteVenta ingresado
            nombreCliente = "Nombre Cliente Prueba"  # Placeholder

            fechaVenta = input("Ingrese la fecha de viaje (DD/MM/AAAA): ")

            print("\n----------------------------------------------------------------")
            print(f"Ingreso la siguiente informacion para esta Venta: \n    Destino: {nombreDestino} - Cliente: {nombreCliente} - Fecha: {fechaVenta} ")
            print(f"Costo a ese destino: {costoDestino}")          
            print("----------------------------------------------------------------")
            insertar_venta(idDestinoVenta, idClienteVenta, fechaVenta)

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
        ventaEncontrada = False  # Placeholder para la búsqueda

        #En este punto se implementa un bucle para realizar la busqueda de la venta segun el comprobante ingresado
        if not ventaEncontrada:
            print("\n__________________________________________________")
            print(f"No se encontraron ventas con ese comprobante: {idVenta}.")
            print("__________________________________________________")
        else:
            # Se verifica que este en los 60 dias de la fecha de venta y se actualiza el estado de la venta como ANULADA
            print("\n__________________________________________________")
            print(f"\nSe ha ANULADO la venta del comprobate ({idVenta}) exitosamente.")
            print("__________________________________________________")
            anular_venta(idVenta)
    else:
        print("El numero de comprobante debe ser un número entero.")