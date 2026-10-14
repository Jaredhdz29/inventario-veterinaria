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
    cursor.execute("""
        SELECT id, nombre, marca, precio, cantidad
        FROM productos
        WHERE activo = TRUE
        ORDER BY id
    """)
    productos = cursor.fetchall()

    if not productos:
        print("No hay productos en el inventario.")
    else:
        for producto in productos:
            print(f'{producto["id"]} | {producto["nombre"]} | {producto["marca"]} | ${producto["precio"]:.2f} | {producto["cantidad"]} unidades')

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


def buscar_producto(conexion):
    nombre_producto = input("Escribe parte del nombre a buscar: ").strip()
    busqueda = f"%{nombre_producto}%"

    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, nombre, marca, precio, cantidad
        FROM productos
        WHERE nombre LIKE %s AND activo = TRUE
        ORDER BY id
    """, (busqueda,))
    productos = cursor.fetchall()

    if not productos:
        print("No se encontraron productos con ese nombre.")
    else:
        for producto in productos:
            print(f'{producto["id"]} | {producto["nombre"]} | {producto["marca"]} | ${producto["precio"]:.2f} | {producto["cantidad"]} unidades')

    cursor.close()


def editar_producto(conexion):
    id_modificar = pedir_entero("Ingresa el id del producto a modificar: ")
    precio = pedir_numero("Ingresa el nuevo precio del producto: ")
    cantidad = pedir_entero("Ingresa la nueva cantidad del producto: ")

    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE productos
        SET precio = %s, cantidad = %s
        WHERE id = %s AND activo = TRUE
    """, (precio, cantidad, id_modificar))
    conexion.commit()

    if cursor.rowcount == 0:
        print("No se actualizó: el id no existe, está desactivado o los datos son iguales.")
    else:
        print("Producto actualizado.")

    cursor.close()


def desactivar_producto(conexion):
    id_producto = pedir_entero("Ingresa el id del producto a desactivar: ")
    confirmacion = input("¿Estás seguro de desactivar el producto? (s/n): ").strip().lower()

    if confirmacion == "s":
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE productos
            SET activo = FALSE
            WHERE id = %s AND activo = TRUE
        """, (id_producto,))
        conexion.commit()

        if cursor.rowcount == 0:
            print("No se desactivó: el id no existe o está desactivado")
        else:
            print("Producto desactivado.")
        cursor.close()
    else:
        print("Operación cancelada.")




def main():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        print("Conexión exitosa a la base de datos veterinaria")

        while True:
            print("\n--- Inventario Veterinaria ---")
            print("1. Ver inventario")
            print("2. Agregar producto")
            print("3. Buscar producto")
            print("4. Editar producto")
            print("5. Desactivar producto")
            print("6. Salir")
            opcion = input("Ingresa la opción que deseas elegir: ").strip()

            if opcion == "1":
                mostrar_inventario(conexion)
            elif opcion == "2":
                agregar_producto(conexion)
            elif opcion == "3":
                buscar_producto(conexion)
            elif opcion == "4":
                editar_producto(conexion)
            elif opcion == "5":
                desactivar_producto(conexion)
            elif opcion == "6":
                conexion.close()
                print("¡Hasta luego!")
                break
            else:
                print("Ingresaste una opción no válida, ingresa un número del 1 - 6")

    except mysql.connector.Error as e:
        print(f"Error de MySQL: {e}")


main()