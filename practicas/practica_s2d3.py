
inventario = [
    {"nombre": "Antipulgas para perro", "marca": "Frontline", "precio": 275.00, "cantidad": 3},
    {"nombre": "Desparasitante para perros", "marca": "Bayer", "precio": 132.00, "cantidad": 8},
    {"nombre": "Jabón antipulgas para perro", "marca": "Asuntol", "precio": 82.50, "cantidad": 2},
    {"nombre": "Correa para perro amarilla", "marca": "Kong", "precio": 77.00, "cantidad": 9},
]

def mostrar_inventario(inventario):
    for producto in inventario:
        print(f'{producto["nombre"]} | {producto["marca"]} | ${producto["precio"]:.2f} | {producto["cantidad"]} unidades') 
        
    print(f'Cantidad de productos: {len(inventario)}')

mostrar_inventario(inventario)

def agregar_producto(inventario, nombre, marca, precio, cantidad):
    producto = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "cantidad": cantidad,
    }
    inventario.append(producto)

nombre = input("Ingresa el nombre del producto: ").strip()
marca = input("Ingresa la marca del producto: ").strip()
precio = float(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad de productos: "))

agregar_producto(inventario, nombre, marca, precio, cantidad)
mostrar_inventario(inventario)

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if nombre.lower() in producto["nombre"].lower():
            return producto
        
    return None

nombre = input("Ingresa el nombre del producto que deseas buscar: ").strip()
resultado_busqueda = buscar_producto(inventario, nombre)
if resultado_busqueda is None:
    print("Producto no encontrado")
else: 
    print(f'Producto encontrado: {resultado_busqueda["nombre"]} | {resultado_busqueda["marca"]} | ${resultado_busqueda["precio"]:.2f} | {resultado_busqueda["cantidad"]} unidades')

def valor_inventario(inventario):
    total = 0
    for producto in inventario:
        valor_por_producto = producto["precio"] * producto["cantidad"]
        total += valor_por_producto
    return total

valor = valor_inventario(inventario)
print(f'El valor total del inventario es: ${valor:.2f}')