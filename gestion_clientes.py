# gestion_clientes.py
# Alta, baja, modificación, listado de clientes

from crudDB import insertar_cliente, actualizar_cliente, eliminar_cliente, listar_clientes,buscar_cliente, buscar_venta_cliente
from valida import valida_cuit, valida_mail

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
            
            # pide el numero de CUIT, debe ser ingresado segun  formato indicado  
            while True:
                cuitCliente = input("Ingrese el CUIT con el siguiente formato (99-99999999-9): ")
                if valida_cuit(cuitCliente):
                    print("CUIT valido.")
                    break
                else:
                    print("CUIT invalido. Intente de nuevo.")
 
            #mail del cliente, valida

            while True:
                mailCliente = input("Ingrese su correo electrónico: ")
                if not mailCliente:
                    break
                if valida_mail(mailCliente):
                    print("El mail es válido.")
                    break
                else:
                    print("Email invalido. Intente nuevamente.")
            
            #hacer insert del nuevo cliente
            mensaje=insertar_cliente(nombreCliente, cuitCliente, mailCliente)
            print(mensaje)

        # Modifica Cliente    
        elif opcion == "3":
            #Solicita el id del cliente, para validar que exista y asi poder modificar
            print("\n** Has elegido la opción: Modificar Cliente")
            idCliente = int(input("Ingrese el ID Cliente a modificar: "))
           
           #Se busca si existe el cliente
            clienteEncontrado= buscar_cliente(idCliente)
            
            if clienteEncontrado:
                print(clienteEncontrado)
                #Solicitar los datos a modificar y hacer update 
                nombreCliente = input("\nIngrese el nuevo nombre del Cliente: ")
                
                # pide el numero de CUIT, debe ser ingresado segun  formato indicado  
                while True:
                    cuitCliente = input("Ingrese el CUIT con el siguiente formato (99-99999999-9): ")
                    if valida_cuit(cuitCliente):
                        print("CUIT valido.")
                        break
                    else:
                        print("CUIT invalido. Intente de nuevo.")
    
                #mail del cliente, valida

                while True:
                    mailCliente = input("Ingrese su correo electrónico: ")
                    if not mailCliente:
                        break
                    if valida_mail(mailCliente):
                        print("El mail es válido.")
                        break
                    else:
                        print("Email invalido. Intente nuevamente.")
                

                mensaje=actualizar_cliente(idCliente, nombreCliente, cuitCliente, mailCliente)
                print(mensaje)
            else:
                print("Cliente no encontrado por favor intente nuevamente")

        #Elimina Cliente 
        elif opcion == "4":
            #Se solicita el ID del cliente a Eliminar
            print("\n** Has elegido la opción: Eliminar Cliente")
            idCliente = int(input("Ingrese el ID Cliente a eliminar: "))
            
            #se busca el cliente, solicita la confirmacion que es el cliente correcto y se elimina
            #Se busca si existe el cliente
            clienteEncontrado= buscar_cliente(idCliente)
            
            if clienteEncontrado:
                 
                # Si existe el cliente busca que no tenga ventas para poder eliminar

                ventaEncontrado= buscar_venta_cliente(id_Cliente=idCliente)
                
                print(ventaEncontrado)
                
                if not ventaEncontrado:

                    print("\n Detalle de Cliente: ")
                    print(clienteEncontrado)
                    print("\n")
 
                     # Preguntar al usuario si confirma la eliminacion
                    respuesta = input("\n ¿Estás seguro que quieres eliminar el cliente? (s/n): ").lower()

                    if respuesta == "s" or respuesta == "sí":
                    
                        # Se elimina el cliente
                        mensaje=eliminar_cliente(idCliente)
                        print(mensaje)          
                    else:
                        print("\n Cancelo la eliminacion del cliente")       
               
                     
                else:
                    print("\n Detalle de Cliente: ")
                    print(clienteEncontrado)
                    print("\n No se puede eliminar el cliente porque tiene ventas asignadas.")
                    
            else:
                print("Cliente no encontrado por favor intente nuevamente")

       
        #Volver al menu principal
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")