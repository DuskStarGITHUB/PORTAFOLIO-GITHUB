-- comando selet de las tablas con todas las columnas
SELECT * FROM hotel_palace.catalogo;
SELECT * FROM hotel_palace.habitaciones;
SELECT * FROM hotel_palace.huesped;
SELECT * FROM hotel_palace.metodo_de_pago;
SELECT * FROM hotel_palace.pagos;
SELECT * FROM hotel_palace.paquetes;
SELECT * FROM hotel_palace.perfil;
SELECT * FROM hotel_palace.receptor;
SELECT * FROM hotel_palace.reservaciones;

-- comando select para ver columnas fijas
SELECT nombre, precio FROM hotel_palace.catalogo;
SELECT membresia, nombre, apellido_paterno, apellido_materno FROM hotel_palace.perfil;


-- manipulacion de registros --


-- Comando (=)
Select *from perfil where membresia=87931;
Select *from perfil where nombre='Speencer';

-- Comando (and)
SELECT * FROM reservaciones WHERE fecha='2022-02-21 00:00:00' And id_reserva='3301';

SELECT * FROM hotel_palace.reservaciones;
SELECT * FROM reservaciones WHERE fecha='2022-02-21 00:00:00' And id_reserva='3631';

-- Comando (OR)

SELECT * FROM reservaciones WHERE fecha='2022-02-21 00:00:00' or id_reserva='3631';
SELECT * FROM reservaciones WHERE no_noches='7' or id_perfil='8';

-- Comando (<=>)

Select *from perfil where membresia<50877;
Select id_perfil, nombre, membresia from perfil where membresia<50877;

Select *from perfil where membresia<19190;
Select *from perfil where membresia<=19190;

Select *from perfil where membresia=87931;

Select *from perfil where membresia>87931;
Select *from perfil where membresia>=87931;

-- Comando (BEETWEEN__AND_)

select *from perfil where id_perfil between 20 and 27;
select *from perfil where id_perfil between 5 and 8;

-- Comando (Like)

SELECT * FROM pagos WHERE met_pago LIKE '1%'; 
SELECT * FROM pagos WHERE met_pago LIKE '5'; 

select *from perfil where nombre Like 'S%';
select *from perfil where apellido_paterno Like'%ez';

-- Comando (IN)

SELECT * FROM perfil WHERE apellido_paterno IN ('pulido');
SELECT * FROM perfil WHERE apellido_paterno IN ('pulido','ramirez','sanchez');
SELECT * FROM perfil WHERE genero IN ('M');
SELECT * FROM perfil WHERE genero IN ('F');
Select *from perfil where id_perfil IN (6,40,20,15,7);


-- Comnados de Ordenamiento --

-- Comando (Grup BY)

Select id_perfil,nombre,apellido_paterno,apellido_materno from perfil order by apellido_paterno;
Select id_perfil,nombre,apellido_paterno,apellido_materno from perfil order by nombre;
-- DESC o ASC para definir si acendente o decente no hace falta poner asc si querenos ascendete
Select id_perfil,nombre,apellido_paterno,apellido_materno from perfil order by nombre DESC;
SELECT * FROM hotel_palace.reservaciones;
Select id_reserva, id_perfil, num_habitacion from reservaciones order by num_habitacion ASC;
Select id_reserva, id_perfil, num_habitacion from reservaciones order by num_habitacion DESC;


-- Comandos de Agregacion --


-- Comando (count)

Select count(*) as Habitaciones_Disponibles from habitaciones where disponibilidad =('Disponible');
Select count(disponibilidad) as Habitaciones_Disponibles from habitaciones where disponibilidad =('Disponible');
Select count(*) as Habitaciones_Disponibles from habitaciones where disponibilidad =('Ocupado');
Select count(*) as Habitaciones_Disponibles from habitaciones where disponibilidad =('Reservado');

-- Comando (SUM)

SELECT * FROM hotel_palace.pagos;
Select sum(total) as Total from pagos where total='1700';
Select sum(total) as Total from pagos where total;

-- Comando (Max)

SELECT * FROM hotel_palace.habitaciones;
select max(costo) as Mas_Alto_Precio from habitaciones;

-- Comando (MIN)

SELECT * FROM hotel_palace.habitaciones;
select min(costo) as Precio_Minimo from habitaciones;

-- Comando (AVG)

select avg(costo) as Promedio from habitaciones;
select avg(total) as Promedio from pagos;
select avg(costo_paquete) as Promedio from paquetes;


-- Comandos de Uniones --


-- Comando (INNE JOIN)

Select * FROM perfil INNER JOIN reservaciones ON perfil.id_perfil < reservaciones.id_reserva;
Select * FROM perfil INNER JOIN paquetes ON perfil.id_perfil = paquetes.id_paquete;
Select * FROM paquetes INNER JOIN habitaciones ON paquetes.costo_paquete < habitaciones.costo;
Select * FROM paquetes INNER JOIN habitaciones ON paquetes.costo_paquete > habitaciones.costo;

-- Comando (Left Join)

SELECT reservaciones.* , paquetes.id_paquete,costo_paquete FROM reservaciones LEFT JOIN paquetes ON reservaciones.id_paquete = paquetes.id_paquete;

-- Comando (Right Join)

SELECT reservaciones.id_reserva,id_perfil , paquetes.* FROM reservaciones RIGHT JOIN paquetes ON reservaciones.id_paquete=paquetes.id_paquete;


-- Mi propia linea de comando

SELECT * FROM perfil INNER JOIN pagos ON perfil.id_perfil = pagos.id_perfil;
SELECT * FROM perfil INNER JOIN reservaciones ON perfil.id_perfil = reservaciones.id_perfil;

-- Comando que muestra de forma mas simplificada quien hizo una compra

SELECT membresia,nombre,id_reserva,met_pago,total,fecha FROM perfil INNER JOIN pagos ON perfil.id_perfil = pagos.id_perfil;
SELECT membresia,nombre,apellido_paterno,apellido_materno,id_reserva,num_habitacion,no_noches,id_paquete,fecha FROM perfil INNER JOIN reservaciones ON perfil.id_perfil = reservaciones.id_perfil;