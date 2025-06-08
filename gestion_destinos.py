# gestion_destinos.py
# Alta, baja, modificación, listado de destinos

from crudDB import insertar_destino, actualizar_destino, eliminar_destino, listar_destinos,buscar_destino,buscar_venta_cliente

def menu_gestion_destinos():
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
            listar_destinos()

        #Agrega Destino
        elif opcion == "2":
            print("\n ** Has elegido la opción: Agregar Destino")
            #Se piden los datos del Pais, ciudad y costo
            paisDestino = input("\nIngrese el nombre del Pais: ")
            ciudadDestino = input("Ingrese el nombre de la Ciudad : ")
            costoDestino = input(f"Ingrese el costo para el Destino: {ciudadDestino}-{paisDestino}: ")
            
            mensaje=insertar_destino(paisDestino, ciudadDestino, costoDestino)
            print(mensaje)

        # Modifica Destino    
        elif opcion == "3":
            #Solicita el id del destino, para validar que exista y asi poder modificar
            print("\n** Has elegido la opción: Modificar Destino")
            idDestino = int(input("Ingrese el ID Destino a modificar: "))
            
            # se busca el Destino con el id indicado y se procede a solicitar los atributos a modificar (pais, ciudad o costo)
            destinoEncontrado= buscar_destino(idDestino)
             
            if destinoEncontrado:
                print(destinoEncontrado)
                #Solicitar los datos a modificar(PAIS - CIUDAD o COSTO) y hacer update 
                paisDestino = input("\nIngrese el nuevo nombre del Pais: ")
                ciudadDestino = input("Ingrese el nuevo nombre de la Ciudad: ")
                costoDestino = input(f"Ingrese el nuevo costo para el Destino: {ciudadDestino}-{paisDestino}: ")
                mensaje=actualizar_destino(idDestino, paisDestino, ciudadDestino, costoDestino)
                print(mensaje)
        #Elimina Destino 
        elif opcion == "4":
            #Se solicita el ID del Destino a Eliminar
            print("\n** Has elegido la opción: Eliminar Destino")
            idDestino = int(input("Ingrese el ID Destino a eliminar: "))
            #se busca el Destino, solicita la confirmacion que es el Destino correcto y se elimina

            destinoEncontrado= buscar_destino(idDestino)
            
            if destinoEncontrado:
                 
                # Si existe el destino busca que no tenga ventas para poder eliminar

                ventaEncontrado= buscar_venta_cliente(id_Destino=idDestino)
                
                if not ventaEncontrado:

                    print("\n Detalle del Destino: ")
                    print(destinoEncontrado)
                    print("\n")
                    # Eliminacion del destino
                    # Preguntar al usuario si confirma la eliminacion
                    respuesta = input("\n ¿Estás seguro que quieres eliminar el cliente? (s/n): ").lower()

                    if respuesta == "s" or respuesta == "sí":
                    
                        # Se elimina el cliente
                        mensaje=eliminar_destino(idDestino)
                        print(mensaje)          
                    else:
                        print("\n Cancelo la eliminacion del cliente")       
                else:
                    print("\n Detalle de Cliente: ")
                    print(destinoEncontrado)
                    print("\n No se puede eliminar el cliente porque tiene ventas asignadas.")
                    
            else:
                print("Cliente no encontrado por favor intente nuevamente")

            
        
        #Volver al menu principal
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")