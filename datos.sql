USE veterinaria;

INSERT INTO categorias (nombre)
VALUES ('Alimento'),
	('Medicamento'),
    ('Higiene'),
    ('Accesorio');
    
INSERT INTO proveedores (nombre,telefono,correo)
VALUES ('Distribuidora Veterinaria del Norte', '8181234567', 'contacto@divetenorte.com'),
	('Pet Supplies Monterrey', '8182345678', 'ventas@petsuppliesmty.com'),
    ('Comercializadora Animal MX', '8183456789', NULL);
    
INSERT INTO productos (nombre, marca, precio, cantidad, id_proveedor, id_categoria)
VALUES ('Alimento para perro adulto 2 kg', 'Dog Chow', 198.00, 10, 1,1),
	('Alimento para gato adulto 1.5 kg', 'Whiskas', 160.00, 6, 2, 1),
    ('Antipulgas para perro', 'Frontline', 275.00, 3, 1, 2),
    ('Desparasitante para perros', 'Bayer', 132.00, 8, 1, 2),
    ('Shampoo para perro 250 ml', 'Fancy Pets', 104.50, 5, 3, 3),
    ('Jabón antipulgas para perro', 'Asuntol', 82.5, 2, 2, 3),
    ('Collar para perro mediano', 'Pet''s Care', 93.50, 4, 3, 4),
    ('Correa para perro amarilla', 'Kong', 77.00, 9, 2, 4),
    ('Arena para gato 5 kg', 'Minino', 110.00, 1, 1, 3),
    ('Alimento húmedo para gato 85 g', 'Félix', 22.00, 4, 3, 1),
    ('Pasta dental para perros 70 g', 'Virbac', 198.00, 2, 3, 3);
    
