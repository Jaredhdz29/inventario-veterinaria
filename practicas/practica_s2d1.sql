USE veterinaria;

SELECT c.nombre, COUNT(p.id) AS cantidad
FROM categorias AS c
INNER JOIN productos AS p ON c.id_categoria = p.id_categoria
WHERE COUNT(p.id) > 2
GROUP BY c.nombre;

SELECT pr.nombre, SUM(p.cantidad * p.precio) AS valor_inventario
FROM proveedores AS pr
INNER JOIN productos AS p
ON pr.id_proveedor = p.id_proveedor
GROUP BY pr.id_proveedor
HAVING valor_inventario > 1000
ORDER BY valor_inventario DESC;

SELECT c.nombre AS categoria, COUNT(p.id) AS productos_totales
FROM productos AS p
INNER JOIN categorias AS c ON p.id_categoria = c.id_categoria
WHERE p.precio > 100
GROUP BY c.id_categoria
HAVING COUNT(p.id) >= 2;



