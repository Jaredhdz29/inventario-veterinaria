import mysql.connector
from config import DB_CONFIG

try:
    conexion = mysql.connector.connect(**DB_CONFIG)
    print("Conexión exitosa a la base de datos veterinaria")
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT nombre, marca, precio, cantidad FROM productos")
    productos = cursor.fetchall()

    for producto in productos:
        print(f'{producto["nombre"]} | {producto["marca"]} | ${producto["precio"]:.2f} | {producto["cantidad"]} unidades')

    cursor.close()
    conexion.close()
except mysql.connector.Error as e:
    print(f"Error de MySQL: {e}")