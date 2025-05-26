
"""
SISTEMA GESTION DE VUELOS PARA SKYROUTER SRL
Fecha: 23/05/2025
Autores: Grupo 26 - ISPC- Ciencia de Datos
  Solana Francisco
  Ivana Rodriguez
  Lucas Drawich
  Eduardo Zoto
  Carmen Castellano

Este sistema gestiona la administracion de vuelos a distintos destinos, tanto para Empresas como Persona, 
para la empresa SkyRoute

Cómo ejecutar:
Ejecutar este archivo con Python 3: python Main.py
"""

while True:

    #menu principal de opciones del sistema
    print("\n Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("\n 1. Gestionar Clientes")
    print(" 2. Gestionar Destinos")
    print(" 3. Gestionar Ventas")
    print(" 4. Reportes")
    print(" 5. BOTON ARREPENTIMIENTO")
    print(" 6. Acerca del Sistema")
    print(" 7. Salir")

    opcion = input("Seleccione una opción: ")

    # 1.Gestion Clientes
    if opcion == "1":

        print("\nIngresaste al Submenu Gestion Clientes...")
        # MENU CLIENTES. e presenta Submenu de la gestion de clientes
        while True:
            print("\n--- Gestión de Clientes ---")
            print("1. Consulta Clientes")
            print("2. Agregar Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")
            
            #Consulta Cliente
            if opcion == "1":
                # Realiza un listado de todos los clientes
                print("\n** Has elegido la opción: Consulta Clientes")
                print("Se listan todos los clientes")

            #Agrega CLiente
            elif opcion == "2":
                print("\n ** Has elegido la opción: Agregar Cliente")
                #Se piden los datos del cliente (nombre, cuil y mail) y solicita confirmacion 
                nombreCliente=input("\nIngrese el nombre del Cliente: ")
                
                # pide el numero de CUIT, debe ser int y 11 digitos 
                while True:
                    cuitCliente=input("Ingrese el CUIT (11 dígitos, sin guiones y solo numeros): ")
                    if len(cuitCliente)==11:
                        if cuitCliente.isdigit():
                            print("Es un número de CUIT válido.")
                            break
                        else:
                            print("No es un número entero.")
                    else:
                        print("El numero de CUIT debe ser de 11 digitos")

                mailCliente=input("Ingrese el mail de cliente: ")
                print("\n----------------------------------------------------------------")
                print(f"Ingreso la siguiente informacion para el CLIENTE: \n    Nombre: {nombreCliente} - CUIT: {cuitCliente} - Mail: {mailCliente}")          
                print("----------------------------------------------------------------")
                #hacer insert del nuevo cliente

            # Modifica Cliente    
            elif opcion == "3":
                #Solicita el id  del ciente, para validar que exista y asi poder modificar
                print("\n** Has elegido la opción: Modificar Cliente")
                idCliente=int(input("Ingrese el ID Cliente a modificar: "))
             
                # se busca el cliente con el id indicado y se procede a solicitar los atributos a modificar (nombre o cuit o mail)
                
                print(f"Has elegido el cliente con ID {idCliente} para modificar ")
                #Solicitar los datos a modificar y hacer update 

            #Elimina Cliente 
            elif opcion == "4":
                #Se solicita el ID del cliente a Eliminar
                print("\n** Has elegido la opción: Eliminar Cliente")
                
                idCliente=int(input("Ingrese el ID Cliente a eliminar: "))
                #se busca el cliente, solicita la confirmacion que es el cliente correcto y se elimina
                
                print(f"\nHas elegido el cliente con ID {idCliente}  para eliminar")
                #Proceso de delete del cliente
          
           
            #Volver al menu principal
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    # 2.Gestion Destinos   
    elif opcion == "2": 
        # MENU DESTINOS. Submenu de la gestion de destinos
        print("\nIngresaste al Submenu Gestion Destinos...")
        while True:
            print("\n--- Gestión de Destino ---")
            print("1. Consulta Destinos")
            print("2. Agregar Destino")
            print("3. Modificar Destino")
            print("4. Eliminar Destino")
            print("5. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")
            
            #Consulta Destino
            if opcion == "1":
                # Realiza un listado de todos los Destinos
                print("\n** Has elegido la opción: Consulta Destinos")
                print("Se listan todos los Destinos")

            #Agrega Destino
            elif opcion == "2":
                print("\n ** Has elegido la opción: Agregar Destino")
                #Se piden los datos del Pais, ciudad y costo
                
                paisDestino=input("\nIngrese el nombre del Pais: ")
                ciudadDestino=input("Ingrese el nombre de la Ciudad : ")
                costoDestino=input(f"Ingrese el costo para el Destino: {ciudadDestino}-{paisDestino}: ")
                
                print("\n----------------------------------------------------------------")
                print(f"Ingreso la siguiente informacion para el Destino: \n Ciudad: {ciudadDestino} - Pais: {paisDestino} - COSTO: {costoDestino}")          
                print("----------------------------------------------------------------")

            # Modifica Destino    
            elif opcion == "3":
                #Solicita el id  del destino, para validar que exista y asi poder modificar
                print("\n** Has elegido la opción: Modificar Destino")
                
                idDestino=int(input("Ingrese el ID Destino a modificar: "))
                
                # se busca el Destino con el id indicado y se procede a solicitar los atributos a modificar (nombre o cuit o mail)
                print(f"Has elegido el destino con ID {idDestino} para modificar ")
                #Solicitar los datos a modificar(PAIS - CIUDAD o COSTO) y hacer update 
                

            #Elimina Destino 
            elif opcion == "4":
                #Se solicita el ID del Destino a Eliminar
                print("\n** Has elegido la opción: Eliminar Destino")
                
                idDestino=int(input("Ingrese el ID Destino a eliminar: "))
                #se busca el Destino, solicita la confirmacion que es el Destino correcto y se elimina
                 
            #Volver al menu principal
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

 # 3.Gestion Ventas   
    elif opcion == "3": 
        # MENU VENTAS. Submenu de la gestion de Ventas
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

            #Agrega Venta
            elif opcion == "2":
                print("\n ** Has elegido la opción: Agregar Venta")

                #Se piden los datos del Venta (destino, cliente, fecha) 
                idDestinoVenta=input("\nIngrese el Destino de Viaje: ")
                #nombreDestino = función para encontrar nombre destino según el idDestinoVenta y costo del destino para informar al usuario
                nombreDestino="Pais-Ciudad Prueba"
                costoDestino = 9999999.99

                idClienteVenta=input("Ingrese el Cliente del viaje: ")
                #nombreCliente = función de búsqueda del nombre según idClienteVenta ingresado
                nombreCliente="Nombre Cliente Prueba"

                fechaVenta=input("Ingrese la fecha de viaje (DD/MM/AAAA): ")

                print("\n----------------------------------------------------------------")
                print(f"Ingreso la siguiente informacion para esta Venta: \n    Destino: {nombreDestino} - Cliente: {nombreCliente} - Fecha: {fechaVenta} ")
                print(f"Costo a ese destino: {costoDestino}")          
                print("----------------------------------------------------------------")

            #Volver al menu principal
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    # Reportes
    elif opcion == "4":
        print("\nIngresaste al Submenu Reportes...")
       # SUBMENU REPORTES
        while True: 
            print("\n--- Reportes del Sistema  ---")
            print("1. Ventas por fecha")
            print("2. Ventas Canceladas")
            print("3. Clientes de SkyRoute ")
            print("4. Destinos de viajes ")
            print("5. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")
             
            if opcion == "1":
                print("Se listan todas las ventas del dia ")
            elif opcion == "2":        
                print("Se listan todas las ventas ANULADAS del dia")
            elif opcion == "3":        
                print("Se listan los clientes ")
            elif opcion == "4":        
                print("Se listan todas lo destinos de ventas.")
            #Volver al menu principal
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    # BOTON ARREPENTIMIENTO     
    elif opcion == "5":
        
        print("\n** Has elegido la opción: BOTON ARREPENTIMIENTO")
        print("\nDe acuerdo al derecho de arrepentimiento, podés cancelar tu compra dentro de los 60 días corridos de haberla realizado.\n* Según Resolución 329/2020 ANAC el derecho de arrepentimiento no aplica para vuelos y estos se rigen por la política de devolución informada en tu voucher.")

        #Solicita el id  de la Venta, para validar que exista y que este entre los 60 dias habiles 
        idVenta=input("Ingrese el ID Venta (comprobante de venta) -- SOLO NUMEROS: ")

        #Valida que el comprobante sea un numero
        if idVenta.isdigit():
            idVenta=int(idVenta)

            ventaEncontrada = False
            
            #En este punto se implementa un bucle para realizar la busqueda de la venta segun el comprobante ingresado

            if  ventaEncontrada:
                print("\n__________________________________________________")
                print(f"No se encontraron ventas con ese comprobante: {idVenta}.")
                print("__________________________________________________")
            else:
                # Se verifica que este en los 60 dias de la fecha de venta y se actualiza el estado de la venta como ANULADA
                print("\n__________________________________________________")
                print(f"\nSe ha ANULADO la venta del comprobate ({idVenta}) exitosamente.")
                print("__________________________________________________")

        else:
            print("El numero de comprobante debe ser un número entero.")
        # se busca el Venta con el id indicado y se controla los 60 dias habiles y en caso de ser exitoso cambiar el estado de la Venta a ANULADA 
           
    # acerca sistema
    elif opcion == "6":
        print("Has elegido la opción: Acerca del Sistema")
        print("\nSistema de Gestión de Viajes SKyRoute v1.0 desarrollado como práctica de programación estructurada.")
        print("Autores:")
        print("• Castellano, Carmen")
        print("• Darwich, Lucas Javier")
        print("• Rodriguez, Ivana Noemi")
        print("• Solana, Francisco")
        print("• Zoto, Eduardo")
    #Salir
    elif opcion == "7":
        print("Has elegido la opción: Salir")
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

