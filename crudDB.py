# conexion_base_datos.py
# Conexión y operaciones con MySQL
from datetime import datetime
from configDB import conectarDB

# Funciones para operaciones CRUD (esqueleto)
def insertar_cliente(nombre, cuit, mail):
    # Implementar lógica de inserción
    pass

def actualizar_cliente(id_cliente, nombre, cuit, mail):
    # Implementar lógica de actualización
    pass

def eliminar_cliente(id_cliente):
    # Implementar lógica de eliminación
    pass

def listar_clientes():
    # Implementar lógica de listado
    pass    

def listar_clientes():
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("SELECT cuit,nombre,mail FROM cliente")
        resultados = cursor.fetchall()

        print("\n--- Listado de todos los Clientes ---")
        print("-" * 85)
        print(f"{'CUIT'.ljust(15)}{'Razón Social'.ljust(30)}{'Domicilio'.ljust(40)}")
        print("-" * 85)

        for cliente in resultados:
            cuit,nombre,mail = cliente
            print(f"{cuit.ljust(15)}{nombre.ljust(30)}{mail.ljust(40)}") 
       
    except Exception as e:
        print(f"Error al listar clientes: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def insertar_destino(pais, ciudad, costo):
    # Implementar lógica de inserción
    pass

def actualizar_destino(id_destino, pais, ciudad, costo):
    # Implementar lógica de actualización
    pass

def eliminar_destino(id_destino):
    # Implementar lógica de eliminación
    pass

def listar_destinos():
    # Implementar lógica de listado
    pass

def insertar_venta(id_destino, id_cliente, fecha):
    # Implementar lógica de inserción
    pass

def listar_ventas():
    # Implementar lógica de listado
    pass

def anular_venta(id_venta):
    # Implementar lógica de anulación
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "UPDATE VENTA SET ESTADO='ANULADA' WHERE ID_VENTA = %s"

        cursor.execute(query, (id_venta,))   

        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Venta {id_venta} anulada correctamente."
        else:
            resultado = f"No se encontró ninguna venta con ID {id_venta}."

        return resultado
    
    except Exception as e:
        print(f"Error al inentar anular la venta: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def buscar_venta(id_venta):
    # Se hace select en la tabla ventas buscando por el id_venta y chequeando que el tiempo es menor a 60 dias
    # La escala que tomamos para la prueba es : 5 minutos (60 dias)
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        query = """
        SELECT ID_VENTA, ID_CLIENTE, ID_DESTINO, FECHA 
        FROM VENTA 
        WHERE FECHA >= DATE_SUB(NOW(), INTERVAL 5 MINUTE) 
        AND ESTADO = 'ACTIVA' 
        AND ID_VENTA = %s
        """
        cursor.execute(query, (id_venta,))
        resultado = cursor.fetchone()
        return  resultado 
       
    except Exception as e:
        print(f"Error al listar venta: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            