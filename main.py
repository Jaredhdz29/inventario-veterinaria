import csv
from datetime import date

import mysql.connector

from config import DB_CONFIG

STOCK_MINIMO = 5


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


def registrar_movimiento(conexion, tipo):
    id_producto = pedir_entero("Ingresa el id del producto: ")
    cantidad = pedir_entero("Ingresa la cantidad: ")

    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero para que el movimiento sea válido")
        return
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, nombre, cantidad
        FROM productos
        WHERE id = %s AND activo = TRUE
    """, (id_producto,))
    producto = cursor.fetchone()
    if producto is None:
        print("No existe un producto activo con ese id.")
        cursor.close()
        return
    if tipo == "salida" and cantidad > producto["cantidad"]:
        print(f"No hay suficiente stock. Disponible: {producto['cantidad']} unidades.")
        cursor.close()
        return

    if tipo == "entrada":
        cambio = cantidad
    else:
        cambio = -cantidad

    try:
        cursor.execute("""
            INSERT INTO movimientos (id_producto, tipo, cantidad)
            VALUES (%s, %s, %s)
        """, (id_producto, tipo, cantidad))

        cursor.execute("""
            UPDATE productos
            SET cantidad = cantidad + %s
            WHERE id = %s
        """, (cambio, id_producto))
        conexion.commit()
        print(f"Movimiento registrado. Stock actual: {producto['cantidad'] + cambio} unidades.")
    except mysql.connector.Error as e:
        conexion.rollback()
        print(f"No se registró el movimiento: {e}")

    cursor.close()


def ver_movimientos(conexion):
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT m.fecha, p.nombre, m.tipo, m.cantidad
        FROM movimientos AS m
        INNER JOIN productos AS p ON m.id_producto = p.id
        ORDER BY m.fecha DESC, m.id_movimiento DESC
    """)
    movimientos = cursor.fetchall()

    if not movimientos:
        print("No se encontraron movimientos")
    else:
        for movimiento in movimientos:
            print(f'{movimiento["fecha"]:%Y-%m-%d %H:%M} | {movimiento["nombre"]} | {movimiento["tipo"]} | {movimiento["cantidad"]} unidades')

    cursor.close()


def exportar_stock_bajo(productos):
    nombre_archivo = f"stock_bajo_{date.today()}.csv"

    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["id", "nombre", "marca", "categoria", "cantidad"])
            escritor.writeheader()
            escritor.writerows(productos)
            print(f"Reporte exportado: {nombre_archivo}")
    except OSError:
        print("No se pudo crear el archivo. Si está abierto en Excel, ciérralo e intenta de nuevo.")


def reporte_stock_bajo(conexion):
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.id, p.nombre, p.marca, c.nombre AS categoria, p.cantidad
        FROM productos AS p
        INNER JOIN categorias AS c ON p.id_categoria = c.id_categoria
        WHERE p.cantidad < %s AND p.activo = TRUE
        ORDER BY p.cantidad ASC
    """, (STOCK_MINIMO,))
    productos = cursor.fetchall()
    cursor.close()

    if not productos:
        print("Todo el inventario tiene stock suficiente.")
        return

    print(f"\nProductos con menos de {STOCK_MINIMO} unidades:")
    for producto in productos:
        print(f'{producto["id"]} | {producto["nombre"]} | {producto["marca"]} | {producto["categoria"]} | {producto["cantidad"]} unidades')

    respuesta = input("¿Exportar a CSV? (s/n): ").strip().lower()
    if respuesta == "s":
        exportar_stock_bajo(productos)


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
            print("6. Registrar entrada")
            print("7. Registrar salida")
            print("8. Ver movimientos")
            print("9. Reporte de stock bajo")
            print("10. Salir")
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
                registrar_movimiento(conexion, "entrada")
            elif opcion == "7":
                registrar_movimiento(conexion, "salida")
            elif opcion == "8":
                ver_movimientos(conexion)
            elif opcion == "9":
                reporte_stock_bajo(conexion)
            elif opcion == "10":
                conexion.close()
                print("¡Hasta luego!")
                break
            else:
                print("Ingresaste una opción no válida, ingresa un número del 1 - 10")

    except mysql.connector.Error as e:
        print(f"Error de MySQL: {e}")


main()