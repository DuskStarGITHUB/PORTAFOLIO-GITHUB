create database HOTEL_PALACE;
use hotel_dreamstar;

-- Tablas con llaves primarias (unicamente)

Create Table Perfil (
id_perfil int primary key auto_increment NOT NULL,
nombre varchar(20) NOT NULL,
apellido_paterno varchar (20) NOT NULL,
apellido_materno varchar (20) NOT NULL,
membresia int (15) NOT NULL,
telefono varchar (25) NOT NULL,
genero char(1) NOT NULL,
direccion varchar (100),
notas varchar(100)
);

Create Table receptor (
identificador int (15) primary key auto_increment NOT NULL,
nombre varchar(20) NOT NULL,
apellido_paterno varchar(25) NOT NULL,
apellido_materno varchar(20) NOT NULL,
telefono varchar(30) NOT NULL,
turno varchar (25) NOT NULL,
notas varchar (200)
);

create table catalogo (
num_categoria int primary key auto_increment NOT NULL,
tipo varchar(15) NOT NULL,
nombre varchar (15) NOT NULL,
descripcion varchar(100) NOT NULL,
Precio int(20) NOT NULL
);

create table metodo_de_pago (
met_pago int primary key auto_increment NOT NULL,
tipo varchar(25) NOT NULL
);

create table paquetes (
id_paquete int primary key auto_increment NOT NULL,
nombre varchar (30) NOT NULL,
costo_paquete int(11) NOT NULL,
descripcion varchar(100) NOT NULL,
Valoracion varchar(30) NOT NULL,
num_noches int(3) NOT NULL
);

-- Tablas con llaves foraneas

create table habitaciones(
num_habitacion int(2) primary key auto_increment NOT NULL,
planta Varchar (2) NOT NULL,
costo int(7) NOT NULL,
disponibilidad varchar(20) NOT NULL,
detalle varchar (100)NOT NULL,
num_categoria int NOT NULL,
foreign key (num_categoria) references catalogo (num_categoria)
);

create table reservaciones (
id_reserva int(10) primary key auto_increment NOT NULL,
id_perfil int NOT NULL,
identificador int NOT NULL,
id_paquete int NOT NULL,
foreign key (id_perfil) references perfil (id_perfil),
foreign key (identificador) references receptor (identificador),
foreign key (id_paquete) references paquetes (id_paquete),
fecha datetime NOT NULL,
no_noches int (3) NOT NULL,
comentario varchar (200) NULL,
num_habitacion int NOT NULL,
foreign key (num_habitacion) references habitaciones (num_habitacion)
);

create table Pagos(
id_pago int (10) primary key auto_increment NOT NULL,
id_reserva int,
id_perfil int,
met_pago int,
total int (7),
fecha datetime NOT NULL,
foreign key (id_reserva) references reservaciones (id_reserva),
foreign key (id_perfil) references perfil (id_perfil),
foreign key (met_pago) references metodo_de_pago (met_pago)
);

create table huesped (
id_huesped int primary key auto_increment NOT NULL,
id_perfil int,
num_habitacion int,
foreign key (id_perfil) references perfil (id_perfil),
foreign key (num_habitacion) references habitaciones (num_habitacion)
);
