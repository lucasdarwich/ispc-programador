# conexion_base_datos.py
# Conexión y operaciones con MySQL

from config import DB_CONFIG
import mysql.connector

def conectar_db():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

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
    pass