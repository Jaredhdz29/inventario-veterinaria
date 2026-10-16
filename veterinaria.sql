CREATE DATABASE IF NOT EXISTS veterinaria;
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

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL DEFAULT 'sin marca',
    precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    cantidad INT NOT NULL DEFAULT 0 CHECK (cantidad >= 0),
    id_categoria INT NOT NULL,
    id_proveedor INT,
    activo BOOLEAN NOT NULL DEFAULT TRUE,

    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
);

CREATE TABLE IF NOT EXISTS movimientos (
    id_movimiento INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('entrada', 'salida') NOT NULL,
	cantidad INT NOT NULL CHECK (cantidad > 0),
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_producto INT NOT NULL,

    FOREIGN KEY (id_producto) REFERENCES productos(id)
);
