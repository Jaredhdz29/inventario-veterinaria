# Inventario Veterinaria

Sistema de inventario en consola para una veterinaria, hecho con **Python** y **MySQL**. Permite administrar productos, registrar entradas y salidas de mercancía con historial, y generar un reporte de productos con stock bajo exportable a CSV.

## Funcionalidades

- Ver, agregar, buscar y editar productos.
- Desactivar productos sin borrarlos (borrado lógico), para conservar su historial.
- Registrar entradas y salidas de inventario. Cada movimiento actualiza el stock dentro de una **transacción**: si algo falla, no se guarda nada.
- Validación de stock: no permite salidas mayores a lo disponible.
- Historial de movimientos con fecha y nombre del producto.
- Reporte de productos con menos de 5 unidades, exportable a CSV para abrirlo en Excel.
- Gráfica de barras del stock por producto, con los productos bajo el mínimo en rojo.

## Tecnologías

- Python 3.10 o superior
- MySQL 8.0 o superior
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)
- [matplotlib](https://matplotlib.org/)

## Estructura del proyecto

| Archivo | Descripción |
| --- | --- |
| `main.py` | Programa principal con el menú |
| `veterinaria.sql` | Estructura de la base de datos (tablas, llaves y restricciones) |
| `datos.sql` | Datos de ejemplo |
| `config.ejemplo.py` | Plantilla de configuración de la conexión |
| `requirements.txt` | Dependencias de Python |
| `practicas/` | Ejercicios de SQL y Python que hice antes del proyecto |

## Instalación

1. Clona el repositorio:
```
   git clone https://github.com/Jaredhdz29/inventario-veterinaria.git
   cd inventario-veterinaria
```
2. En MySQL (por ejemplo, desde MySQL Workbench), ejecuta primero `veterinaria.sql` y después `datos.sql`.
3. Copia `config.ejemplo.py` con el nombre `config.py` y escribe tu contraseña de MySQL.
4. Instala las dependencias:
```
   pip install -r requirements.txt
```
5. Ejecuta el programa:
```
   python main.py
```

## Qué aprendí

- Conectar Python con MySQL y proteger las credenciales fuera del repositorio.
- Usar consultas parametrizadas (`%s`) para evitar inyección SQL.
- Manejar transacciones con `commit()` y `rollback()` para que el inventario y el historial siempre coincidan.
- Actualizar el stock en SQL (`cantidad = cantidad + %s`) para evitar condiciones de carrera.
- Diseñar tablas con llaves foráneas, restricciones `CHECK` y borrado lógico.

## Autor

**Jared Nathan Hernández Garibaldi**, estudiante de Ingeniería en Tecnología de Software, FIME UANL.
GitHub: [@Jaredhdz29](https://github.com/Jaredhdz29)