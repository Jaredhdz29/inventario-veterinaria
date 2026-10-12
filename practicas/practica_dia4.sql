USE veterinaria;

CREATE TABLE IF NOT EXISTS categorias (
	id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS proveedores (
	id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(100)
);

DESCRIBE proveedores;
DESCRIBE categorias;
SELECT * FROM proveedores;

INSERT INTO categorias (nombre)
VALUES ('Alimento'),
	('Medicamento'),
    ('Higiene'),
    ('Accesorio');
    
INSERT INTO proveedores (nombre,telefono,correo)
VALUES ('Distribuidora Veterinaria del Norte', '8181234567', 'contacto@divetenorte.com'),
	('Pet Supplies Monterrey', '8182345678', 'ventas@petsuppliesmty.com'),
    ('Comercializadora Animal MX', '8183456789', NULL);
    
ALTER TABLE productos
ADD id_categoria INT;
ALTER TABLE productos
ADD id_proveedor INT;
DESCRIBE productos;

ALTER TABLE productos
ADD FOREIGN KEY (id_categoria)
REFERENCES categorias(id_categoria);

ALTER TABLE productos
ADD FOREIGN KEY (id_proveedor)
REFERENCES proveedores(id_proveedor);

SHOW CREATE TABLE productos;
SELECT * FROM proveedores;

START TRANSACTION;
UPDATE productos
SET id_categoria = 1
WHERE id IN (1,2,10);
UPDATE productos
SET id_categoria = 2
WHERE id IN (3,4);
UPDATE productos
SET id_categoria = 3
WHERE id IN (5,6,9,14);
UPDATE productos
SET id_categoria = 4
WHERE id IN (7,8);

UPDATE productos
SET id_proveedor = 1
WHERE id IN (1,3,4,9);
UPDATE productos
SET id_proveedor = 2
WHERE id IN (2,6,8);
UPDATE productos
SET id_proveedor = 3
WHERE id IN (5,7,10,14);

SELECT id,nombre,id_categoria,id_proveedor FROM productos
WHERE id_categoria = null;
COMMIT;

ALTER TABLE productos
MODIFY COLUMN id_categoria INT NOT NULL;
DESCRIBE productos;
INSERT INTO productos (nombre, marca, precio, cantidad, id_categoria, id_proveedor)
VALUES ('Alimento para animal', 'Dog Chow', 170.00, 1, 10, 1);

DELETE FROM categorias
WHERE id_categoria = 1;

SELECT * FROM proveedores;

SELECT id_categoria, COUNT(*) AS total_por_categoria
FROM productos
GROUP BY id_categoria;



