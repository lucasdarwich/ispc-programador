# reportes.py
# Generación de reportes

from crudDB import listar_clientes, listar_destinos, listar_ventas, ventas_del_mes,ventas_totales_por_mes_anio,ventas_anuladas,total_anuladas_por_mes_anio, todas_ventas_anuladas
def menu_reportes():
    print("\nIngresaste al Submenu Reportes...")
    while True: 
        print("\n--- Reportes del Sistema  ---")
        
        print("1. Listado de Clientes ")
        print("2. Listado de Destinos")
        print("3. Listado de Ventas del mes")
        print("4. Ventas totales por MES/AÑO")
        print("5. Ventas ANULADAS en el dia")
        print("6. Todas las Ventas ANULADAS")
        print("7. Total de ventas ANULADAS por MES/AÑO")
        print("8. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
         
        if opcion == "1":
            listar_clientes()
        elif opcion == "2":
            listar_destinos()
        elif opcion == "3":
            ventas_del_mes()
        elif opcion == "4":
            ventas_totales_por_mes_anio()
        elif opcion == "5":
            ventas_anuladas()            
        elif opcion == "6":
            todas_ventas_anuladas()            
        elif opcion == "7":
            total_anuladas_por_mes_anio()
        #Volver al menu principal
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente nuevamente.")