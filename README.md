# SkyRoute - Sistema de Gestión de Pasajes

## Autores

- Castellano, Carmen
- Darwich, Lucas Javier
- Rodriguez, Ivana Noemi
- Solana, Francisco
- Zoto, Eduardo

## Descripción

**SkyRoute** es un sistema de gestión de pasajes desarrollado como práctica de programación estructurada. Permite administrar clientes, destinos y ventas de pasajes, así como gestionar cancelaciones de compras mediante el derecho de arrepentimiento.

El sistema se ejecuta en consola, sin modularización ni funciones, respetando los lineamientos de la Evidencia II.

## Cómo ejecutar

1. Asegurate de tener **Python 3** instalado.
2. Descargá o cloná este repositorio.
3. Abrí una terminal o consola y ejecutá el programa con:

```bash
python main.py
```

## Funcionalidades

### 1. Gestión de Clientes

- Ver clientes existentes
- Agregar nuevos clientes
- Modificar clientes por ID (ej: C1)
- Eliminar clientes por ID

### 2. Gestión de Destinos

- Visualizar todos los destinos (incluye todas las provincias argentinas por defecto)
- Agregar destinos personalizados
- Modificar y eliminar destinos por ID (ej: D1)

### 3. Gestión de Ventas

- Registrar nuevas ventas usando ID de cliente y destino
- Se registra automáticamente:
  - Fecha y hora de la venta
  - Fecha y hora de partida ingresada por el usuario
- Cada venta tiene un ID único (ej: V1)

### 4. Consultas de Ventas

- Ver todas las ventas activas
- Ver ventas canceladas
- Buscar ventas por DNI del cliente

### 5. Botón de Arrepentimiento

- Mensaje informativo sobre el derecho de arrepentimiento
- Permite cancelar una venta por DNI
- Se solicita confirmación
- Al cancelar:
  - La venta se elimina de las activas
  - Se registra fecha y hora de cancelación
  - Se guarda en "Ventas Canceladas"

### 6. Reporte General

- Total de clientes
- Total de destinos
- Total de ventas activas
- Total de ventas canceladas

### 7. Acerca del Sistema

- Muestra información sobre los autores

### 8. Salir

- Cierra el sistema de forma segura

## Librerías utilizadas

### `datetime`

Se utiliza la clase `datetime` de la librería estándar `datetime` para registrar:

- Fecha y hora de cada venta
- Fecha y hora de partida del viaje
- Fecha y hora de cancelación en caso de arrepentimiento

```python
from datetime import datetime
```

