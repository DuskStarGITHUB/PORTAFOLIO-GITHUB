

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('6', 'Diego', 'Alvarez Carranza', '0000072681', '+67632508937952') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('7', 'Jose', 'Andres Ramirez', '0000088710', '+101645095156713') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('8', 'Arensio', 'Gordo', '0000084114', '+5707503966987113') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('9', 'Francisca', 'Castillo', '0000085102', '+595571524972689') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('10', 'Alquilino', 'Vergarara', '0000026106', '+9581858962521') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('11', 'Zaira', 'Reig', '0000087742', '+79870237496415') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('12', 'Itziar', 'Lora', '0000097862', '+74827249760947') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('13', 'Brahim', 'Sierra', '0000026934', '+252762566721464') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('14', 'Pelayo', 'Carbonell', '0000093450', '+92169308787039') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('15', 'Delfina', 'Portela', '0000073218', '+13320922496898') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('16', 'Adelaida', 'Sainz', '0000058678', '+552575076997') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('17', 'Mohamed', 'Miralles', '0000031409', '+551741794854') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('18', 'Anas', 'Herrero', '0000044043', '+552710636329') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('19', 'Norma', 'Aliaga', '0000097144', '+550497086828') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('20', 'Alexandru', 'Guevara', '0000057526', '+557936412875') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('21', 'Xavi', 'Paez', '0000075070', '+559522254145') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('22', 'Javi', 'Rios', '0000060347', '+554263945702') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('23', 'Khalid', 'Hidalgo', '0000040933', '+553915102652') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('24', 'Sabela', 'Manrique', '0000060877', '+558554079533') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('25', 'Minerva', 'Maroto', '0000080167', '+559774354538') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('26', 'Soledad', 'De la Fuente', '0000053420', '+558308457826') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('27', 'Jose', 'Ferrero', '0000084343', '+559547788403') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('28', 'Rut', 'Romman', '0000072404', '+559481643372') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('29', 'Mari', 'Estevez', '0000032397', '+557123816565') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('30', 'Aaron', 'Velasco', '0000083096', '+551280120550') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('31', 'Alvaro', 'del Moral', '0000058476', '+554168506884') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('32', 'Ana Belen', 'Rey', '0000065100', '+550771328930') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('33', 'Ayman', 'San Jose', '0000011812', '+552035181285') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('34', 'Orlando', 'Cardona', '0000014816', '+555495073464') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('35', 'Humberto', 'Zheng', '0000036248', '+554656440563') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('36', 'Jacinto', 'Palau', '0000081175', '+553120848246') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('37', 'Candida', 'Real', '0000095302', '+550334111564') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('38', 'Melanie', 'Ariza', '0000049659', '+552369887331') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('39', 'Antia', 'Ribas', '0000038616', '+555239154755') ;

insert into cliente (id_cliente, nombre, apellido, identificador, telefono) Values
('40', 'Gerard', 'Montes', '0000022546', '+558920177689') ;

-- comandos de agrupacion o registro.
SELECT * FROM hotel_dreamstar.cliente;
SELECT id_cliente FROM hotel_dreamstar.cliente;

SELECT * FROM cliente;

select *from cliente where id_cliente order by nombre;
select *from cliente where id_cliente order by apellido;

Select *from cliente where identificador>86320;
Select *from cliente where identificador>=86320;

Select *from cliente where identificador <60000;

select *from cliente where id_cliente between 20 and 27;

select *from cliente where nombre Like 'S%';
select *from cliente where apellido Like '%ez';

Select *from cliente where id_cliente IN (6,40,20,15,7);


