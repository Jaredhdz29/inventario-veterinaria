USE veterinaria;
SELECT * FROM productos;

-- INSERT INTO productos (nombre, cantidad, marca, precio)
-- VALUES ('Juguete pelota', -2, 'Pets', 100.00);

SELECT nombre,precio FROM productos;

SELECT * FROM productos
WHERE cantidad = 0;

SELECT * FROM productos
WHERE precio > 200
ORDER BY precio desc;

SELECT * FROM productos
WHERE marca = 'sin marca';

SELECT * FROM productos
WHERE precio BETWEEN 100 AND 500
AND cantidad > 0;

SELECT nombre, (precio * cantidad) AS valor_total
FROM productos;

SELECT COUNT(*) AS total_productos
FROM productos;

SELECT SUM(precio * cantidad) AS total
FROM productos;