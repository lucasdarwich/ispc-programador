# SkyRoute - Sistema de Gestión de Pasajes
# Autores:
# • Castellano, Carmen
# • Darwich, Lucas Javier
# • Rodriguez, Ivana Noemi
# • Solana, Francisco
# • Zoto, Eduardo
# Cómo ejecutar:
# Ejecutar este archivo con Python 3: python main.py

from datetime import datetime

clientes = [
    {"id": "C1", "nombre": "Carmen Castellano", "dni": "11111111"},
    {"id": "C2", "nombre": "Lucas Javier Darwich", "dni": "22222222"},
    {"id": "C3", "nombre": "Ivana Noemi Rodriguez", "dni": "33333333"},
    {"id": "C4", "nombre": "Francisco Solana", "dni": "44444444"},
    {"id": "C5", "nombre": "Eduardo Zoto", "dni": "55555555"}
]

provincias = ["Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos",
              "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén",
              "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero",
              "Tierra del Fuego", "Tucumán"]

destinos = []
for i, provincia in enumerate(provincias):
    destinos.append({"id": f"D{i+1}", "nombre": provincia})

ventas = []
ventas_canceladas = []

contador_clientes = len(clientes)
contador_destinos = len(destinos)
contador_ventas = 0

while True:
    print("\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Acerca del Sistema")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            print("\n-- GESTIONAR CLIENTES --")
            print("1. Ver Clientes")
            print("2. Agregar Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")
            subop = input("Seleccione una opción: ")
            if subop == "1":
                print("\nLista de clientes:")
                if len(clientes) == 0:
                    print("No hay clientes cargados en el sistema.")
                else:
                    for c in clientes:
                        print(f"ID: {c['id']} | Nombre: {c['nombre']} | DNI: {c['dni']}")
            elif subop == "2":
                nombre = input("Ingrese nombre completo: ")
                dni = input("Ingrese DNI: ")
                contador_clientes += 1
                clientes.append({"id": f"C{contador_clientes}", "nombre": nombre, "dni": dni})
                print("Cliente agregado correctamente.")
            elif subop == "3":
                id_mod = input("Ingrese el ID del cliente a modificar (ej: C1): ")
                for c in clientes:
                    if c["id"] == id_mod:
                        c["nombre"] = input("Nuevo nombre: ")
                        c["dni"] = input("Nuevo DNI: ")
                        print("Cliente modificado.")
                        break
                else:
                    print("Cliente no encontrado.")
            elif subop == "4":
                id_elim = input("Ingrese el ID del cliente a eliminar (ej: C1): ")
                clientes = [c for c in clientes if c["id"] != id_elim]
                print("Cliente eliminado si existía.")
            elif subop == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "2":
        while True:
            print("\n-- GESTIONAR DESTINOS --")
            print("1. Ver Destinos")
            print("2. Agregar Destino")
            print("3. Modificar Destino")
            print("4. Eliminar Destino")
            print("5. Volver al Menú Principal")
            subop = input("Seleccione una opción: ")
            if subop == "1":
                if len(destinos) == 0:
                    print("No hay destinos cargados en el sistema.")
                else:
                    for d in destinos:
                        print(f"ID: {d['id']} | Destino: {d['nombre']}")
            elif subop == "2":
                nombre = input("Ingrese nombre del destino: ")
                contador_destinos += 1
                destinos.append({"id": f"D{contador_destinos}", "nombre": nombre})
                print("Destino agregado.")
            elif subop == "3":
                id_mod = input("Ingrese el ID del destino a modificar (ej: D1): ")
                for d in destinos:
                    if d["id"] == id_mod:
                        d["nombre"] = input("Nuevo nombre: ")
                        print("Destino modificado.")
                        break
                else:
                    print("Destino no encontrado.")
            elif subop == "4":
                id_elim = input("Ingrese el ID del destino a eliminar (ej: D1): ")
                destinos = [d for d in destinos if d["id"] != id_elim]
                print("Destino eliminado si existía.")
            elif subop == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "3":
        print("\n-- GESTIONAR VENTAS --")
        cliente_id = input("Ingrese ID del cliente (ej: C1): ")
        destino_id = input("Ingrese ID del destino (ej: D1): ")
        fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fecha_partida = input("Ingrese fecha y hora de partida (YYYY-MM-DD HH:MM): ")
        try:
            datetime.strptime(fecha_partida, "%Y-%m-%d %H:%M")
            contador_ventas += 1
            ventas.append({
                "id": f"V{contador_ventas}",
                "cliente_id": cliente_id,
                "destino_id": destino_id,
                "fecha_venta": fecha_venta,
                "fecha_partida": fecha_partida
            })
            print("Venta registrada correctamente.")
        except ValueError:
            print("Formato de fecha inválido.")

    elif opcion == "4":
        while True:
            print("\n-- CONSULTAR VENTAS --")
            print("1. Ver todas las ventas")
            print("2. Ver ventas canceladas")
            print("3. Buscar ventas por DNI (ej: 11111111)")
            print("4. Volver al Menú Principal")
            subop = input("Seleccione una opción: ")
            if subop == "1":
                if len(ventas) == 0:
                    print("No hay ventas registradas.")
                else:
                    for v in ventas:
                        print(f"ID: {v['id']} | Cliente: {v['cliente_id']} | Destino: {v['destino_id']} | Fecha venta: {v['fecha_venta']} | Partida: {v['fecha_partida']}")
            elif subop == "2":
                if len(ventas_canceladas) == 0:
                    print("No hay ventas canceladas.")
                else:
                    for v in ventas_canceladas:
                        print(f"ID: {v['id']} | Cliente: {v['cliente_id']} | Destino: {v['destino_id']} | Fecha venta: {v['fecha_venta']} | Partida: {v['fecha_partida']} | Cancelada: {v.get('fecha_cancelacion', 'N/A')}")
            elif subop == "3":
                dni_buscar = input("Ingrese DNI a buscar: ")
                for v in ventas:
                    for c in clientes:
                        if v["cliente_id"] == c["id"] and c["dni"] == dni_buscar:
                            print(f"ID: {v['id']} | Cliente: {c['nombre']} | Destino: {v['destino_id']} | Venta: {v['fecha_venta']}")
            elif subop == "4":
                break
            else:
                print("Opción inválida.")

    elif opcion == "5":
        print("\nDe acuerdo al derecho de arrepentimiento, podés cancelar tu compra dentro de los 10 días corridos de haberla realizado.\n* Según Resolución 329/2020 ANAC el derecho de arrepentimiento no aplica para vuelos y estos se rigen por la política de devolución informada en tu voucher.")
        dni = input("Ingrese DNI para buscar ventas a cancelar: ")
        venta_encontrada = False
        for v in ventas[:]:
            for c in clientes:
                if v["cliente_id"] == c["id"] and c["dni"] == dni:
                    print(f"Venta encontrada: ID {v['id']} | Cliente: {c['nombre']} | Destino: {v['destino_id']}")
                    confirmacion = input("¿Desea cancelar esta venta? (s/n): ")
                    if confirmacion.lower() == "s":
                        ventas.remove(v)
                        v["fecha_cancelacion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        ventas_canceladas.append(v)
                        print("Venta cancelada.")
                        venta_encontrada = True
                        break
        if not venta_encontrada:
            print("No se encontraron ventas con ese DNI.")

    elif opcion == "6":
        print("\n-- REPORTE GENERAL --")
        print(f"Total de clientes: {len(clientes)}")
        print(f"Total de destinos: {len(destinos)}")
        print(f"Ventas realizadas: {len(ventas)}")
        print(f"Ventas canceladas: {len(ventas_canceladas)}")

    elif opcion == "7":
        print("\nSkyRoute es un sistema de gestión de pasajes desarrollado como práctica de programación estructurada.")
        print("Autores:")
        print("• Castellano, Carmen")
        print("• Darwich, Lucas Javier")
        print("• Rodriguez, Ivana Noemi")
        print("• Solana, Francisco")
        print("• Zoto, Eduardo")

    elif opcion == "8":
        print("Gracias por usar SkyRoute. ¡Hasta la próxima!")
        break

    else:
        print("Opción inválida. Por favor, intente nuevamente.")
