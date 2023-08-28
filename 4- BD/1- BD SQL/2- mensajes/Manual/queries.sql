-- QUERIES (Consultas)

-- Tabla Usuarios
SELECT * FROM usuarios;

-- Tabla Mensajes
SELECT * FROM mensajes;

-- Consulta Completa
SELECT
    u.usuario_id,
    u.nombre,
    u.correo,
    u.telefono,
    m.mensaje_id,
    m.mensaje
FROM usuarios u JOIN mensajes m ON u.usuario_id = m.usuario_id;


-- Consulta Parcial
SELECT ROW_NUMBER() OVER (ORDER BY u.usuario_id) AS id,
    u.nombre,
    m.mensaje
FROM Usuarios u JOIN Mensajes m ON u.usuario_id = m.usuario_id;
