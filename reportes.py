# reportes.py
# Generación de reportes

def menu_reportes():
    print("\nIngresaste al Submenu Reportes...")
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