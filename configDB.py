import mysql.connector

def conectarDB():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="admin",
        database="skyroute"  # Si querés usar una base directamente
    )