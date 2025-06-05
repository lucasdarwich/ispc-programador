-- Listado de clientes
SELECT * FROM cliente;

-- Listar todos los destinos con que contengan Y en la descripcion
SELECT pais, ciudad, costo FROM destino WHERE pais LIKE '%Y%';

-- Listar todos los paises de destinos posibles

 SELECT pais FROM destino GROUP BY pais;

-- Cantidad total de ciudades por cada pais  
SELECT des.pais, COUNT(*) FROM destino des GROUP BY pais;

-- Todas las ventas Anuladas para el año en curso
SELECT  
cli.NOMBRE,des.PAIS,des.CIUDAD,vta.FECHA 
FROM venta AS vta INNER JOIN  cliente AS cli ON vta.ID_CLIENTE = cli.ID_CLIENTE INNER JOIN 
 destino AS des ON vta.ID_DESTINO = des.ID_DESTINO  WHERE vta.ESTADO = 'ANULADA' AND YEAR(vta.FECHA)= YEAR(NOW()) ;
 
 -- Mostrar todas las ventas del mes de abril
 SELECT 
 cli.NOMBRE,des.PAIS,des.CIUDAD,vta.FECHA
 FROM venta AS vta INNER JOIN cliente AS cli ON vta.ID_CLIENTE = cli.ID_CLIENTE INNER JOIN
 destino AS des ON vta.ID_DESTINO = des.ID_DESTINO WHERE MONTH (vta.FECHA) = 4 