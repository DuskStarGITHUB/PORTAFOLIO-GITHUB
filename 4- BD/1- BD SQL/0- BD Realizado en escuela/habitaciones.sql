-- comandos de agregacion.

SELECT * FROM hotel_dreamstar.habitaciones;

Select count(*) as Habitaciones_Disponibles from habitaciones where id_categoria =10;

Select sum(costo) as Precios from habitaciones where costo =764;
select max(costo) as Gran_Precio from habitaciones;
select min(costo) as Gran_Precio from habitaciones;
select avg(costo) as Promedio from habitaciones;

Select id_categoria, count(*) from habitaciones id_categoria group by id_categoria;

