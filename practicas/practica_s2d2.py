
# nombre = input("Ingresa el nombre del producto: ")
# precio = float(input("Ingresa el precio del producto: "))
# cantidad = int(input("Ingresa la cantidad del producto: "))

# total = precio * cantidad
# print(f"{nombre}: {cantidad} x ${precio:.2f} = ${total:.2f}")
        
        
gran_total = 0
productos_cobrados = 0

while True:
    nombre = input("Ingresa el nombre del producto: ")
    if nombre.strip().lower() == "fin":
        break
    
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad del producto: "))

    if precio < 0 or cantidad <= 0:
        print("Cantidad y/o precio inválido")
    else: 
        productos_cobrados += 1
        total = precio * cantidad
        if total > 500:
            descuento = total * 0.10
            total_descuento = total - descuento
            gran_total += total_descuento
            print(f"{nombre}: {cantidad} x ${precio:.2f}")
            print(f"total original = ${total:.2f}")
            print(f"descuento aplicado = ${descuento:.2f}")
            print(f"total final = ${total_descuento:.2f}")
        else:
            gran_total += total
            print(f"{nombre}: {cantidad} x ${precio:.2f} = ${total:.2f}")
print(f"productos cobrados: {productos_cobrados}")
print(f"gran total: ${gran_total:.2f}")
