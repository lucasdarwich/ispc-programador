# main.py
# Archivo principal con menú de opciones

from gestion_clientes import menu_gestion_clientes
from gestion_destinos import menu_gestion_destinos
from gestion_ventas import menu_gestion_ventas, boton_arrepentimiento
from reportes import menu_reportes
from acerca_sistema import mostrar_acerca_sistema

def main():
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

        if opcion == "1":
            menu_gestion_clientes()
        elif opcion == "2":
            menu_gestion_destinos()
        elif opcion == "3":
            menu_gestion_ventas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            boton_arrepentimiento()
        elif opcion == "6":
            mostrar_acerca_sistema()
        elif opcion == "7":
            print("Has elegido la opción: Salir")
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()