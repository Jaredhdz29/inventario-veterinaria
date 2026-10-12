
import csv

inventario = [
    {"nombre": "Antipulgas para perro", "marca": "Frontline", "precio": 275.00, "cantidad": 3},
    {"nombre": "Desparasitante para perros", "marca": "Bayer", "precio": 132.00, "cantidad": 8},
    {"nombre": "Jabón antipulgas para perro", "marca": "Asuntol", "precio": 82.50, "cantidad": 2},
    {"nombre": "Correa para perro amarilla", "marca": "Kong", "precio": 77.00, "cantidad": 9},
]


def exportar_csv(inventario, ruta):
    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "marca", "precio", "cantidad"])
        escritor.writeheader()
        escritor.writerows(inventario)     


def importar_csv(ruta):
    productos = []
    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["precio"] = float(fila["precio"])
            fila["cantidad"] = int(fila["cantidad"])
            productos.append(fila) 
    return productos


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


def mostrar_inventario(inventario):
    for producto in inventario:
        print(f'{producto["nombre"]} | {producto["marca"]} | ${producto["precio"]:.2f} | {producto["cantidad"]} unidades') 
        
    print(f'Cantidad de productos: {len(inventario)}')


def agregar_producto(inventario, nombre, marca, precio, cantidad):
    producto = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "cantidad": cantidad,
    }
    inventario.append(producto)


def buscar_producto(inventario, nombre):
    for producto in inventario:
        if nombre.lower() in producto["nombre"].lower():
            return producto
        
    return None


def valor_inventario(inventario):
    total = 0
    for producto in inventario:
        valor_por_producto = producto["precio"] * producto["cantidad"]
        total += valor_por_producto
    return total

exportar_csv(inventario, "practicas/productos.csv")

inventario_importado = importar_csv("practicas/productos.csv")

mostrar_inventario(inventario)


valor = valor_inventario(inventario)
print(f'El valor total del inventario es: ${valor:.2f}')

valor_importado = valor_inventario(inventario_importado)
print(f'El valor total del inventario importado es: ${valor_importado:.2f}')


nombre = input("Ingresa el nombre del producto: ").strip()
marca = input("Ingresa la marca del producto: ").strip()
precio = pedir_numero("Ingresa el precio del producto: ")
cantidad = pedir_entero("Ingresa la cantidad de productos: ")

agregar_producto(inventario, nombre, marca, precio, cantidad)
mostrar_inventario(inventario)


nombre = input("Ingresa el nombre del producto que deseas buscar: ").strip()
resultado_busqueda = buscar_producto(inventario, nombre)
if resultado_busqueda is None:
    print("Producto no encontrado")
else: 
    print(f'Producto encontrado: {resultado_busqueda["nombre"]} | {resultado_busqueda["marca"]} | ${resultado_busqueda["precio"]:.2f} | {resultado_busqueda["cantidad"]} unidades')


