# ✈️ SkyRoute - Sistema de Gestión de Pasajes

## 👥 Autores

- Castellano, Carmen
- Darwich, Lucas Javier
- Rodriguez, Ivana Noemi
- Solana, Francisco
- Zoto, Eduardo

## 📌 Descripción del Proyecto

**SkyRoute** es una aplicación de consola desarrollada en Python que permite la gestión modular de ventas de pasajes aéreos, registro de clientes y administración de destinos, utilizando una base de datos MySQL. Este proyecto fue realizado en el marco del módulo Programador de la Tecnicatura en Ciencia de Datos e Inteligencia Artificial

## 🔧 Requisitos

- Python 3.10 o superior
- MySQL Server (local o remoto)
- Conexión establecida y credenciales válidas en el archivo de conexión (condigDB.py)
- Instalar dependencias:

```bash
pip install mysql-connector-python
```

## 💻 Clonar y Ejecutar

1. Abrí una terminal.
2. Cloná el repositorio con:

```bash
git clone https://github.com/lucasdarwich/ispc-programador.git
```

## 🚀 Cómo ejecutar

1. Asegurate de tener **Python 3** instalado.
2. Descargá o cloná este repositorio.
3. Abrí una terminal o consola y ejecutá el programa con:

```bash
python main.py
```

## 📁 Estructura del Proyecto

```bash
skyroute/
│
├── ABP/                       # Documento de Proyecto, Poster ABP y Video del Grupo.
├── Base de Datos/             # Entregables Base de Datos
├── Etica y Deontologia/       # Entregable Ética y Deontología
│
├── acerca_sistema.py          # Información general del sistema
├── configDB.py                # Configuración de conexión a la base de datos
├── crudDB.py                  # Funciones CRUD generales
├── gestion_clientes.py        # Gestión de datos de clientes
├── gestion_destinos.py        # Gestión de destinos y sus atributos
├── gestion_ventas.py          # Gestión de ventas y botón de arrepentimiento
├── main.py                    # Menú principal e integración del sistema
├── reportes.py                # Generación de reportes
├── valida.py                  # Validaciones de datos
└── README.md                  # Documentación principal del sistema
```

## 🧠 Funcionalidades Principales

- **Gestión de Clientes**  
  Alta, baja, modificación y consulta de datos de clientes.

- **Gestión de Destinos**  
  Administración completa de los destinos ofrecidos.

- **Gestión de Ventas**  
  Registro de nuevas ventas y listado de operaciones realizadas.

- **Reportes**  
  Ventas por fecha, ventas canceladas, listado de clientes y destinos.

- **Botón de Arrepentimiento**  
  Permite cancelar una venta, bajo condiciones especificadas por normativa ANAC.

- **Información del Sistema**  
  Datos del equipo de desarrollo y versión del sistema.

## 🧭 Normas éticas y legales aplicadas

Este sistema integra principios de:

- **Protección de datos personales (Ley 25.326):** la información de clientes es válida, no duplicada, y se respetan las reglas de integridad.

- **Defensa del consumidor (Ley 24.240):** el botón de arrepentimiento garantiza el derecho de anulación de venta en tiempo.

- **Régimen de propiedad intelectual (Ley 11.723):** todo el código está desarrollado por el equipo, respetando derechos de autor.

- **Ética profesional y seguridad de la información:** validaciones, controles y estructura modular pensada para mantener datos consistentes y seguros.
