import mysql.connector
from config import DB_CONFIG


def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Ingresa un número válido por favor")


def pedir_entero(mensaje):
    while True:
        try:
            numero_entero = int(input(mensaje))
            return numero_entero
        except ValueError:
            print("Ingresa un número entero válido por favor")


def mostrar_inventario(conexion):
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT nombre, marca, precio, cantidad FROM productos")
    productos = cursor.fetchall()

    if not productos:
        print("No hay productos en el inventario.")
    else:
        for producto in productos:
            print(f'{producto["nombre"]} | {producto["marca"]} | ${producto["precio"]:.2f} | {producto["cantidad"]} unidades')

    cursor.close()


def agregar_producto(conexion):
    nombre = input("Ingresa el nombre del producto: ")
    marca = input("Ingresa la marca del producto: ")
    precio = pedir_numero("Ingresa el precio del producto: ")
    cantidad = pedir_entero("Ingresa la cantidad del producto: ")
    id_categoria = pedir_entero("Ingresa el id de la categoría del producto: ")

    cursor = conexion.cursor()

    sql = """
        INSERT INTO productos (nombre, marca, precio, cantidad, id_categoria)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (nombre, marca, precio, cantidad, id_categoria)
    cursor.execute(sql, valores)

    conexion.commit()
    print(f"Producto agregado con id {cursor.lastrowid}.")

    cursor.close()


def main():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        print("Conexión exitosa a la base de datos veterinaria")

        while True:
            print("--- Inventario Veterinaria ---")
            print("1. Ver inventario")
            print("2. Agregar producto")
            print("3. Salir")
            opcion = input("Ingresa la opción que deseas elegir: ").strip()

            if opcion == "1":
                mostrar_inventario(conexion)
            elif opcion == "2":
                agregar_producto(conexion)
            elif opcion == "3":
                conexion.close()
                print("¡Hasta luego!")
                break
            else:
                print("Ingresaste una opción no válida, ingresa un número del 1 - 3")

    except mysql.connector.Error as e:
        print(f"Error de MySQL: {e}")


main()