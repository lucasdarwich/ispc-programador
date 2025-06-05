-- Sentencias DML para datos de ejemplo

INSERT INTO CLIENTE (nombre,cuit,mail) VALUES ('GABRIEL PEREZ','20-16999888-0','gabiperez@gmail.com'); 
INSERT INTO CLIENTE (nombre,cuit,mail) VALUES ('GONZALO FERNANDEZ','20-22356778-0','fer@gmail.com'); 
INSERT INTO CLIENTE (nombre,cuit,mail) VALUES ('BLANCAYCELESTE SA','33-45666870-9','bc@hotmail.com'); 

INSERT INTO DESTINO (pais,ciudad,costo) VALUES ('ARGENTINA', 'SALTA', 300000); 
INSERT INTO DESTINO (pais,ciudad,costo) VALUES ('ARGENTINA', 'USHUAIA',150000); 
INSERT INTO DESTINO (pais,ciudad,costo) VALUES ('BRASIL','RIO DE JANEIRO', 500000); 
INSERT INTO DESTINO (pais,ciudad,costo) VALUES ('URUGUAY', 'MONTEVIDEO',350000); 
 
INSERT INTO venta (id_cliente,id_destino,fecha) VALUES(2,3,NOW()); 
INSERT INTO venta (id_cliente,id_destino,fecha) VALUES (1,2,'2025-01-25 08:45:10'); 
INSERT INTO venta (id_cliente,id_destino,fecha) VALUES (3,4,'2025-05-22 11:18:32'); 
INSERT INTO venta (id_cliente,id_destino,fecha) VALUES (3,1,'2025-06-03 12:05:50'); 
INSERT INTO venta (id_cliente,id_destino,fecha) VALUES (3,1,'2025-04-16 12:00:10'); 
INSERT INTO venta (id_cliente,id_destino,fecha) VALUES (3,1,'2025-04-09 14:24:02'); 
INSERT INTO venta (id_cliente,id_destino,fecha, estado, fecha_anula, motivo_anula)
VALUES (3,2,'2025-04-09 12:14:22','ANULADA','2025-04-09 13:44:22','Cambio de destino'); 
