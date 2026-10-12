USE veterinaria;

 SELECT productos.nombre AS producto, categorias.nombre AS categoria FROM productos
 JOIN categorias;

SELECT * FROM categorias;

SELECT p.nombre AS producto, pr.nombre AS proveedor, pr.telefono 
FROM productos AS p
JOIN proveedores AS pr ON p.id_proveedor = pr.id_proveedor
ORDER BY pr.nombre, producto;

SELECT p.nombre AS producto, p.marca, p.precio, c.nombre AS categoria, pr.nombre AS proveedor 
FROM productos AS p
JOIN categorias AS c ON p.id_categoria = c.id_categoria
JOIN proveedores AS pr ON p.id_proveedor = pr.id_proveedor
WHERE c.nombre LIKE '%Higiene%';

START TRANSACTION;
INSERT INTO categorias (nombre)
VALUES ('Juguetes');
INSERT INTO proveedores (nombre,telefono,correo)
VALUES ('Distribuidora BCS', '6241643253', 'contacto@BCS.com');
INSERT INTO productos (nombre, marca, precio, cantidad, id_categoria)
VALUES ('Pelota apachurrable', 'dogkids', 108.00, 10, 4);

SELECT p.nombre AS producto, c.nombre AS categoria, pr.nombre AS proveedor 
FROM productos AS p
JOIN categorias AS c ON p.id_categoria = c.id_categoria
LEFT JOIN proveedores AS pr ON p.id_proveedor = pr.id_proveedor;

SELECT * FROM proveedores;
SELECT c.nombre, p.nombre AS producto
FROM categorias AS c
LEFT JOIN productos AS p ON c.id_categoria = p.id_categoria
AND p.precio > 100;
ROLLBACK;

SELECT pr.*
FROM proveedores AS pr
LEFT JOIN productos AS p
	ON pr.id_proveedor = p.id_proveedor
WHERE p.id IS NULL;

