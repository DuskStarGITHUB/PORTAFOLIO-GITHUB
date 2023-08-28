-- Crear BD
CREATE DATABASE mensajeria;
USE mensajeria;

-- Crear tabla Usuarios
CREATE TABLE usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    telefono VARCHAR(20)
);

-- Crear tabla Mensajes
CREATE TABLE mensajes (
    mensaje_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    mensaje TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);

-- Insertar registros en la tabla Usuarios
INSERT INTO Usuarios (nombre, correo, telefono)
VALUES
    ('Juan', 'juan@email.com', '123-456-7890'),
    ('Maria', 'maria@email.com', '987-654-3210');

-- Insertar registros en la tabla Mensajes
INSERT INTO Mensajes (usuario_id, mensaje)
VALUES
    (1, 'Hola, estoy interesado en tu trabajo...'),
    (2, 'Quisiera discutir una posible colaboración.');

