# gestion_clientes.py
# Alta, baja, modificación, listado de clientes

from conexion_base_datos import insertar_cliente, actualizar_cliente, eliminar_cliente, listar_clientes

def menu_gestion_clientes():
    print("\nIngresaste al Submenu Gestion Clientes...")
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
            listar_clientes()

        #Agrega Cliente
        elif opcion == "2":
            print("\n ** Has elegido la opción: Agregar Cliente")
            #Se piden los datos del cliente (nombre, cuil y mail) y solicita confirmacion 
            nombreCliente = input("\nIngrese el nombre del Cliente: ")
            
            # pide el numero de CUIT, debe ser int y 11 digitos 
            while True:
                cuitCliente = input("Ingrese el CUIT (11 dígitos, sin guiones y solo numeros): ")
                if len(cuitCliente) == 11:
                    if cuitCliente.isdigit():
                        print("Es un número de CUIT válido.")
                        break
                    else:
                        print("No es un número entero.")
                else:
                    print("El numero de CUIT debe ser de 11 digitos")

            mailCliente = input("Ingrese el mail de cliente: ")
            print("\n----------------------------------------------------------------")
            print(f"Ingreso la siguiente informacion para el CLIENTE: \n    Nombre: {nombreCliente} - CUIT: {cuitCliente} - Mail: {mailCliente}")          
            print("----------------------------------------------------------------")
            #hacer insert del nuevo cliente
            insertar_cliente(nombreCliente, cuitCliente, mailCliente)

        # Modifica Cliente    
        elif opcion == "3":
            #Solicita el id del cliente, para validar que exista y asi poder modificar
            print("\n** Has elegido la opción: Modificar Cliente")
            idCliente = int(input("Ingrese el ID Cliente a modificar: "))
         
            # se busca el cliente con el id indicado y se procede a solicitar los atributos a modificar (nombre o cuit o mail)
            print(f"Has elegido el cliente con ID {idCliente} para modificar ")
            #Solicitar los datos a modificar y hacer update 
            nombreCliente = input("\nIngrese el nuevo nombre del Cliente: ")
            cuitCliente = input("Ingrese el nuevo CUIT (11 dígitos, sin guiones y solo numeros): ")
            mailCliente = input("Ingrese el nuevo mail de cliente: ")
            actualizar_cliente(idCliente, nombreCliente, cuitCliente, mailCliente)

        #Elimina Cliente 
        elif opcion == "4":
            #Se solicita el ID del cliente a Eliminar
            print("\n** Has elegido la opción: Eliminar Cliente")
            idCliente = int(input("Ingrese el ID Cliente a eliminar: "))
            #se busca el cliente, solicita la confirmacion que es el cliente correcto y se elimina
            print(f"\nHas elegido el cliente con ID {idCliente} para eliminar")
            #Proceso de delete del cliente
            eliminar_cliente(idCliente)
       
        #Volver al menu principal
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")