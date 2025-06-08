# conexion_base_datos.py
# Conexión y operaciones con MySQL
from datetime import datetime
from configDB import conectarDB

# Funciones para operaciones CRUD (esqueleto)
def insertar_cliente(nombre, cuit, mail):
    # Implementar lógica de inserción
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "INSERT INTO cliente (nombre,cuit,mail) VALUES (%s,%s,%s); "

        cursor.execute(query, (nombre,cuit,mail,))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Cliente insertado correctamente"
        else:
            resultado = f"Hubo un error no se pudo insertar al cliente."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar dar de alta un cliente: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close() 

def actualizar_cliente(id_cliente, nombre, cuit, mail):
    # Implementar lógica de actualización
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "UPDATE cliente SET nombre = %s,cuit =%s, mail =%s WHERE ID_CLIENTE = %s ; "

        cursor.execute(query, (nombre,cuit,mail,id_cliente,))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Cliente actualizado correctamente"
        else:
            resultado = f"Hubo un error no se pudo actualizar al cliente."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar modificar el cliente: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def eliminar_cliente(id_cliente):
    # Implementar lógica de eliminación
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "DELETE from cliente WHERE ID_CLIENTE = %s ; "

        cursor.execute(query, (id_cliente,))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Cliente elimnado correctamente"
        else:
            resultado = f"Hubo un error no se pudo eliminar al cliente."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar modificar el cliente: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
    


def listar_clientes():
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("SELECT id_cliente,cuit,nombre,mail FROM cliente")
        resultados = cursor.fetchall()

        print("\n-------- Listado de todos los Clientes ---------")
        print("-" * 85)
        print(f"{'ID'.ljust(6)}{'CUIT'.ljust(15)}{'Razón Social'.ljust(30)}{'Domicilio'.ljust(40)}")
        print("-" * 85)

        for cliente in resultados:
            id,cuit,nombre,mail = cliente
            print(f"{id}    {cuit.ljust(15)}{nombre.ljust(30)}{mail.ljust(40)}") 
       
    except Exception as e:
        print(f"Error al listar clientes: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def insertar_destino(pais, ciudad, costo):
    # Implementar lógica de inserción
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "INSERT INTO destino (pais,ciudad,costo) VALUES (%s,%s,%s); "

        cursor.execute(query, (pais,ciudad,costo,))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Destino insertado correctamente"
        else:
            resultado = f"Hubo un error no se pudo insertar el destino."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar dar de alta un destino: {e}")


def actualizar_destino(id_destino, pais, ciudad, costo):
    # Implementar lógica de actualización
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "UPDATE destino SET pais = upper(%s),ciudad =upper(%s), costo =%s WHERE ID_DESTINO = %s ; "

        cursor.execute(query, (pais, ciudad, costo,id_destino, ))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Destino actualizado correctamente"
        else:
            resultado = f"Hubo un error no se pudo actualizar el destino."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar modificar el destino: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def eliminar_destino(id_destino): 
    # Implementar lógica de eliminación
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "DELETE from destino WHERE ID_DESTINO = %s ; "

        cursor.execute(query, (id_destino,))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Destino elimnado correctamente"
        else:
            resultado = f"Hubo un error no se pudo eliminar Destino."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar modificar el destino: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
    

def listar_destinos():
    # Implementar lógica de listado
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("SELECT id_destino, pais, ciudad, costo FROM destino")
        resultados = cursor.fetchall()

        print("\n-------- Listado de todos los Destinos ---------")
        print("-" * 85)
        print(f"{'ID'.ljust(6)}{'País'.ljust(30)}{'Ciudad'.ljust(35)}{'Costo'.rjust(10)}")
        print("-" * 85)

        for destino in resultados:
            id,pais,ciudad,costo = destino
            print(f"{str(id)}     {pais.ljust(30)}{ciudad.ljust(35)}{str(costo).rjust(10)}")       
    except Exception as e:
        print(f"Error al listar destinos: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def insertar_venta(id_destino, id_cliente):
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "INSERT INTO venta (id_cliente, id_destino, fecha) VALUES (%s,%s,NOW()) "

        cursor.execute(query, (id_destino, id_cliente,))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Venta insertada correctamente"
        else:
            resultado = f"Hubo un error no se pudo insertar la venta."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar dar de alta una Venta: {e}")

def listar_ventas():
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("""
        SELECT 
            id_venta, cli.nombre, des.PAIS, des.CIUDAD, des.COSTO, 
            vta.FECHA, vta.ESTADO, vta.FECHA_ANULA
        FROM venta AS vta
        INNER JOIN cliente AS cli ON vta.ID_CLIENTE = cli.ID_CLIENTE
        INNER JOIN destino AS des ON vta.ID_DESTINO = des.ID_DESTINO
        ORDER BY vta.FECHA DESC
        """)

        resultados = cursor.fetchall()

        print("\n-------- Listado de Ventas con Cliente y Destino ---------")
        print("-" * 140)
        print(f"{'ID'.ljust(5)}{'Cliente'.ljust(25)}{'País'.ljust(20)}{'Ciudad'.ljust(20)}"
            f"{'Costo'.rjust(10)}{'Fecha'.rjust(22)}{'Estado'.rjust(12)}{'Anulada'.rjust(20)}")
        print("-" * 140)

        for fila in resultados:
            id_venta, nombre_cliente, pais, ciudad, costo, fecha, estado, fecha_anula = fila
            fecha_str = fecha.strftime("%d/%m/%Y %H:%M") if fecha else ""
            fecha_anula_str = fecha_anula.strftime("%d/%m/%Y %H:%M") if fecha_anula else "—"
            
            print(f"{str(id_venta).ljust(5)}{nombre_cliente.ljust(25)}{pais.ljust(20)}{ciudad.ljust(20)}"
                f"{str(round(costo, 2)).rjust(10)}{fecha_str.rjust(22)}{estado.rjust(12)}{fecha_anula_str.rjust(20)}")

    except Exception as e:
        print(f"Error al listar destinos: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def anular_venta(id_venta):
    # Implementar lógica de anulación
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        
        query = "UPDATE VENTA SET ESTADO='ANULADA', FECHA_ANULA=NOW() WHERE ID_VENTA = %s"

        cursor.execute(query, (id_venta,))   
        connection.commit() 

        if cursor.rowcount > 0:
            resultado = f"Venta anulada correctamente."
        else:
            resultado = f"No se encontró ninguna venta con ID {id_venta}."
        return resultado
    
    except Exception as e:
        print(f"Error al intentar anular la venta: {e}")

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
        SELECT 
        CONCAT('Vendido a:  ',
            cli.NOMBRE, ' con Destino: ',
            des.PAIS, '-',
            des.CIUDAD, '.',
            ' Fecha de viaje: ', vta.FECHA
        ) AS resultado
        FROM venta AS vta
        INNER JOIN cliente AS cli ON vta.ID_CLIENTE = cli.ID_CLIENTE
        INNER JOIN destino AS des ON vta.ID_DESTINO = des.ID_DESTINO
        WHERE FECHA >= DATE_SUB(NOW(), INTERVAL 5 DAY) 
        AND ESTADO = 'ACTIVA' 
        AND ID_VENTA = %s
        """
        cursor.execute(query, (id_venta,))
        resultado = cursor.fetchone()

        return  resultado 
       
    except Exception as e:
        print(f"Error al buscar la venta: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def buscar_cliente(id_cliente):
    
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        query = """
        SELECT 
        CONCAT('CLIENTE: ',
        cli.NOMBRE, ' CUIT: ',cli.CUIT,' MAIL: ',cli.mail
        ) AS resultado
        FROM cliente AS cli
        WHERE id_cliente = %s
        """
        cursor.execute(query, (id_cliente,))
        resultado = cursor.fetchone()

        return  resultado 
       
    except Exception as e:
        print(f"Error al buscar el cliente: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def buscar_destino(id_destino):
    
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        query = """
        SELECT 
        CONCAT('PAIS: ',PAIS, ' - CIUDAD: ',CIUDAD,'- COSTO: ',costo
        ) AS resultado
        FROM destino
        WHERE id_destino = %s
        """
        cursor.execute(query, (id_destino,))
        resultado = cursor.fetchone()

        return  resultado 
       
    except Exception as e:
        print(f"Error al buscar el destino: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def buscar_venta_cliente(id_Cliente=None, id_Destino=None):
    
    connection = None
    cursor = None
    try:
        connection = conectarDB()
        cursor = connection.cursor()

        if id_Cliente is not None:
            
            query = """
            SELECT ID_VENTA, ID_CLIENTE, ID_DESTINO, FECHA
            FROM VENTA
            WHERE ID_CLIENTE = %s 
            LIMIT 1
            """
            cursor.execute(query, (id_Cliente,))
            resultado = cursor.fetchone()
            
        elif id_Destino is not None:
            query = """
            SELECT ID_VENTA, ID_CLIENTE, ID_DESTINO, FECHA
            FROM VENTA
            WHERE ID_DESTINO = %s 
            LIMIT 1
            """
            cursor.execute(query, (id_Destino,))
            resultado = cursor.fetchone()
            
        else:
            query = """
            SELECT null from dual
            """
            cursor.execute(query, )
            resultado = cursor.fetchone()       
        return  resultado 
       
    except Exception as e:
        print(f"Error al buscar las ventas por  cliente: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

# REPORTES
def ventas_del_mes():
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id_venta, id_cliente, id_destino, fecha
            FROM venta
            WHERE MONTH(fecha) = MONTH(NOW()) AND YEAR(fecha) = YEAR(NOW())
        """)
        resultados = cursor.fetchall()

        print("\n-------- Ventas del Mes ---------")
        print("-" * 100)
        print(f"{'ID Venta'.ljust(10)}{'ID Cliente'.ljust(15)}{'ID Destino'.ljust(15)}{'Fecha'.ljust(25)}")
        print("-" * 100)

        for venta in resultados:
            id_venta, id_cliente, id_destino, fecha = venta
            fecha_str = fecha.strftime("%d/%m/%Y %H:%M")
            print(f"{str(id_venta).ljust(10)}{str(id_cliente).ljust(15)}{str(id_destino).ljust(15)}{fecha_str.ljust(25)}")
    except Exception as e:
        print(f"Error al listar ventas del mes: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def ventas_totales_por_mes_anio():
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT YEAR(fecha), MONTH(fecha), COUNT(*) as total
            FROM venta
            WHERE estado = 'ACTIVA'
            GROUP BY YEAR(fecha), MONTH(fecha)
            ORDER BY YEAR(fecha), MONTH(fecha)
        """)
        resultados = cursor.fetchall()

        print("\n-------- Ventas Totales por Mes/Año ---------")
        print("-" * 50)
        print(f"{'Año'.ljust(10)}{'Mes'.ljust(10)}{'Total Ventas'.ljust(20)}")
        print("-" * 50)

        for fila in resultados:
            anio, mes, total = fila
            print(f"{str(anio).ljust(10)}{str(mes).ljust(10)}{str(total).ljust(20)}")
    except Exception as e:
        print(f"Error al listar ventas por mes/año: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def ventas_anuladas():
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id_venta, id_cliente, fecha
            FROM venta
            WHERE estado = 'ANULADA' AND DATE(fecha) = CURDATE()
        """)
        resultados = cursor.fetchall()

        print("\n-------- Ventas ANULADAS del Día ---------")
        print("-" * 80)
        print(f"{'ID Venta'.ljust(10)}{'ID Cliente'.ljust(20)}{'Fecha'.ljust(25)}")
        print("-" * 80)

        for fila in resultados:
            id_venta, id_cliente, fecha = fila
            print(f"{str(id_venta).ljust(10)}{str(id_cliente).ljust(20)}{fecha.strftime('%d/%m/%Y %H:%M').ljust(25)}")
    except Exception as e:
        print(f"Error al listar ventas anuladas: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def todas_ventas_anuladas():
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id_venta, id_cliente, fecha, fecha_anula
            FROM venta
            WHERE estado = 'ANULADA'  order by fecha
        """)
        resultados = cursor.fetchall()

        print("\n-------- Todas las Ventas ANULADAS    ---------")
        print("-" * 80)
        print(f"{'ID Venta'.ljust(10)}{'ID Cliente'.ljust(20)}{'Fecha'.ljust(25)}{'Fecha Anula'.ljust(25)}")
        print("-" * 80)

        for fila in resultados:
            id_venta, id_cliente, fecha , fecha_anula= fila
            print(f"{str(id_venta).ljust(10)}{str(id_cliente).ljust(20)}{fecha.strftime('%d/%m/%Y %H:%M').ljust(25)}{fecha_anula.strftime('%d/%m/%Y %H:%M').ljust(25)}")
    except Exception as e:
        print(f"Error al listar ventas anuladas: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def total_anuladas_por_mes_anio():
    try:
        connection = conectarDB()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT YEAR(fecha), MONTH(fecha), COUNT(*) as total
            FROM venta
            WHERE estado = 'ANULADA'
            GROUP BY YEAR(fecha), MONTH(fecha)
            ORDER BY YEAR(fecha), MONTH(fecha)
        """)
        resultados = cursor.fetchall()

        print("\n-------- Total Anuladas por Mes/Año ---------")
        print("-" * 50)
        print(f"{'Año'.ljust(10)}{'Mes'.ljust(10)}{'Total Anuladas'.ljust(20)}")
        print("-" * 50)

        for fila in resultados:
            anio, mes, total = fila
            print(f"{str(anio).ljust(10)}{str(mes).ljust(10)}{str(total).ljust(20)}")
    except Exception as e:
        print(f"Error al listar anuladas por mes/año: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
