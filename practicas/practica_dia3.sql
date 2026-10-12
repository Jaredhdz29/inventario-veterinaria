USE veterinaria;

SELECT * FROM productos;

-- DELETE FROM productos
-- WHERE id IN (11,12,13);

SELECT COUNT(*) AS total_productos
FROM productos;
SELECT SUM(precio * cantidad) AS total
FROM productos;

-- UPDATE productos
-- SET cantidad = cantidad + 6
-- WHERE id = 10;

-- UPDATE productos
-- SET precio = 160.00
-- WHERE marca = 'Bayer';

START TRANSACTION;
DELETE FROM productos
WHERE id = 6;
ROLLBACK;

UPDATE productos
SET nombre = 'Correa para perro amarilla'
WHERE id = 8;
UPDATE productos
SET marca = 'Kong'
WHERE id = 8;

UPDATE productos
SET precio = 70.00,
	cantidad = cantidad + 2
WHERE id = 8;

SELECT * FROM productos
WHERE nombre LIKE '%perro%';

START TRANSACTION;
UPDATE productos
SET precio = precio * 1.1
WHERE id IN (1,3,4,5,6,7,8,14);
COMMIT;

SELECT * FROM productos
WHERE cantidad >= 2;
START TRANSACTION;
UPDATE productos
SET cantidad = cantidad - 2
WHERE id IN (1,2,3,4,5,6,7,8,9,10,14) AND cantidad >= 2;
COMMIT;