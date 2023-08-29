-- Datos de catalogo
INSERT INTO catalogo  VALUES ('1', 'Comun', 'Individual', 'una habitación asignada a una persona. Puede tener una o más camas.');
INSERT INTO catalogo  VALUES ('2', 'Comun', 'Doble', 'una habitación asignada a dos personas. Puede tener una o más camas.');
INSERT INTO catalogo  VALUES ('3', 'Comun', 'Triple', 'una habitación asignada a tres personas. Puede tener dos o más camas.');
INSERT INTO catalogo  VALUES ('4', 'Comun', 'Quad', 'una sala asignada a cuatro personas. Puede tener dos o más camas.');
INSERT INTO catalogo  VALUES ('5', 'Comun', 'Queen', 'una habitación con una cama de matrimonio. Puede ser ocupado por una o más personas.');
INSERT INTO catalogo  VALUES ('6', 'Comun', 'King', 'una habitación con una cama king-size. Puede ser ocupado por una o más personas.');
INSERT INTO catalogo  VALUES ('7', 'Comun', 'Twin', 'una habitación con dos camas. Puede ser ocupado por una o más personas.');
INSERT INTO catalogo  VALUES ('8', 'Comun', 'Doble-Doble', 'una habitación con dos camas dobles (o tal vez queen). Puede ser ocupado por una o más personas.');
INSERT INTO catalogo  VALUES ('9', 'Comun', 'Estudio', 'una habitación con una cama de estudio, un sofá que se puede convertir en una cama. También puede tener una cama adicional.');
INSERT INTO catalogo  VALUES ('10', 'Suite', 'Master Suite', 'Un salón o sala de estar conectada a uno o más dormitorios.');
INSERT INTO catalogo  VALUES ('11', 'Suite', 'Junior Suite', 'Una habitación individual con una cama y una sala de estar. A veces, el área para dormir está en un dormitorio separado del salón o la sala de estar.');
INSERT INTO catalogo  VALUES ('12', 'Extra', 'Habitacion comunicada', 'habitaciones con puertas de entrada individuales desde el exterior y una puerta de conexión entre ellas. Los huéspedes pueden moverse entre habitaciones sin pasar por el pasillo.');
INSERT INTO catalogo  VALUES ('13', 'Extra', 'Habitaciones contiguas', 'habitaciones con una pared común, pero sin puerta de conexión.');
INSERT INTO catalogo  VALUES ('14', 'Extra', 'Habitaciones adyacente', ' habitaciones cercanas, tal vez al otro lado del pasillo.');
INSERT INTO catalogo  VALUES ('15', 'Extra', 'Habitaciones adyacente', ' habitaciones cercanas, tal vez al otro lado del pasillo.');

SELECT * FROM hotel_palace.catalogo;

-- Datos de metodos de pago
INSERT INTO metodo_de_pago (`met_pago`, `tipo`) VALUES ('1', 'Efectivo.');
INSERT INTO metodo_de_pago (`met_pago`, `tipo`) VALUES ('2', 'En Linea.');
INSERT INTO metodo_de_pago (`met_pago`, `tipo`) VALUES ('3', 'Tarjeta de credito.');
INSERT INTO metodo_de_pago (`met_pago`, `tipo`) VALUES ('4', 'Cheque.');
INSERT INTO metodo_de_pago (`met_pago`, `tipo`) VALUES ('5', 'Tarjeta de debito.');
INSERT INTO metodo_de_pago (`met_pago`, `tipo`) VALUES ('6', 'Cuenta Bancaria.');

SELECT * FROM hotel_palace.metodo_de_pago;

-- Datos de perfiles

INSERT INTO perfil VALUES ('1', 'Speencer', 'Pulido', 'Romero', '25736', '+738106391141', 'M', 'Lago Cuitzeo MZ.35 LT-70 B CDMX Ixtapaluca San Buenaventura.', 'NA');
INSERT INTO perfil VALUES ('2', 'Cesar Eduardo', 'Jimenez', 'Maza', '36926', '+60489141542407', 'M', 'L\' Conde 81893 Camiño Abril, 68, 8º F', 'NA');
INSERT INTO perfil VALUES ('3', 'Hector Eduardo', 'Vazquez', 'Zambrano', '31723', '+0483040341592', 'M', 'Plaça Alex, 746, Ático 9º', 'NA');
INSERT INTO perfil VALUES ('4', 'Emiliano', 'Momoa', 'Peiro', '52055', '+6209954109459', 'M', 'Camino Segura, 8, 79º D', 'NA');
INSERT INTO perfil VALUES ('5', 'Rick', 'Sanchez', 'Valiente', '54900', '+100490994419', 'M', 'Ronda Vega, 6, Entre suelo 0º', 'NA');
INSERT INTO perfil VALUES ('6', 'Diego', 'Carranza', 'Navas', '66596', '+3404453095089', 'M', '2291 Rudy Road Apt. 473 - Wilmington, SD / 25410', 'NA');
INSERT INTO perfil VALUES ('7', 'Jose', 'Ramirez', 'Carlos Nicolas', '50877', '+8076735735186', 'M', '06692 Murray Station Suite 295 - Albuquerque, IN / 74602', 'NA');
INSERT INTO perfil VALUES ('8', 'Arensio', 'Gordo', 'Millan', '88897', '+202606146197', 'M', '1674 Glover Plaza Suite 158 - Midwest City, MA / 47550', 'NA');
INSERT INTO perfil VALUES ('9', 'Francisca', 'Castillo', 'Prados', '92272', '+838165801636', 'F', '931 Carlos Roads Apt. 844 - Cicero, TN / 32846', 'NA');
INSERT INTO perfil VALUES ('10', 'Alquilino', 'Vergarara', 'Julian', '31562', '+13935606220930', 'M', '810 Greenholt Cliff Suite 166 - Nashua, TX / 53895', 'NA');
INSERT INTO perfil VALUES ('11', 'Zaira', 'Reig', 'Chaves', '86286', '+47643902434831', 'F', '9024 Howell Avenue Suite 575 - Danbury, VT / 77914', 'NA');
INSERT INTO perfil VALUES ('12', 'Itziar', 'Lora', 'Aguilera', '36479', '+343663636881', 'F', '9702 Christiansen Cape Suite 288 - Florence, NY / 18096', 'NA');
INSERT INTO perfil VALUES ('13', 'Brahim', 'Sierra', 'Viñas', '83628', '+6520569594932', 'M', '12097 Jayden Views Apt. 270 - Waterloo, MO / 71902', 'NA');
INSERT INTO perfil VALUES ('14', 'Pelayo', 'Carbonell', 'Cabanillas', '40038', '+559596222580', 'M', '92316 Cruz Crescent Apt. 831 - Draper, UT / 75703', 'NA');
INSERT INTO perfil VALUES ('15', 'Delfina', 'Portela', 'Trujillo', '96366', '+9598264860719', 'F', '38752 Kilback Mission Suite 444 - Concord, DE / 92747', 'NA');
INSERT INTO perfil VALUES ('16', 'Adelaida', 'Sainz', 'Valle', '46941', '+429865727952', 'F', '718 Luther Avenue Suite 758 - Chelsea, IA / 39564', 'NA');
INSERT INTO perfil VALUES ('17', 'Mohamed', 'Miralles', 'Palomino', '30632', '+66824081578559', 'M', '4660 Thad Groves Apt. 331 - Burlington, ND / 08563', 'NA');
INSERT INTO perfil VALUES ('18', 'Anas', 'Herrero', 'Alvarado', '19190', '+6372598315268', 'F', '9843 Violette Walk Apt. 564 - Salina, CT / 58574', 'NA');
INSERT INTO perfil VALUES ('19', 'Norma', 'Aliaga', 'Redondo', '54036', '+244945860546', 'F', '30599 Jacobson Greens Apt. 480 - Cheyenne, CT / 85348', 'NA');
INSERT INTO perfil VALUES ('20', 'Alexandru', 'Guevara', 'García', '20841', '+316999487703', 'M', '72330 Towne Roads Apt. 585 - Jupiter, ND / 71023', 'NA');
INSERT INTO perfil VALUES ('21', 'Xavi', 'Paez', 'Mendoza', '74944', '+002268806287', 'M', '614 Triston Summit Apt. 331 - Kenosha, GA / 82566', 'NA');
INSERT INTO perfil VALUES ('22', 'Javi', 'Rios', 'Palazon', '81897', '+83585220740582', 'M', '07832 Witting Mission Suite 224 - Kent, WA / 04727', 'NA');
INSERT INTO perfil VALUES ('23', 'Khalid', 'Hidalgo', 'Escribano', '47440', '+120557347965', 'F', '0908 Torey Terrace Suite 873 - Charleston, PA / 96921', 'NA');
INSERT INTO perfil VALUES ('24', 'Sabela', 'Manrique', 'Domenech', '90573', '+63020742817875', 'F', '097 Pedro Lodge Suite 546 - Huntington, CO / 12357', 'NA');
INSERT INTO perfil VALUES ('25', 'Minerva', 'Maroto', 'Padron', '87931', '+973888522219', 'F', '3701 Augustus Mountains Apt. 236 - Parker, HI / 03984', 'NA');
INSERT INTO perfil VALUES ('26', 'Soledad', 'De la Fuente', 'Romero', '79485', '+85193957238916', 'F', '0183 Percy Dale Apt. 276 - Maricopa, AK / 37785', 'NA');
INSERT INTO perfil VALUES ('27', 'Jose', 'Ferrero', 'Ripoll', '72264', '+3538157680999', 'M', '7769 Bosco Crest Apt. 322 - Pittsburgh, CT / 41080', 'NA');
INSERT INTO perfil VALUES ('28', 'Rut', 'Romman', 'Castello', '32344', '+85881899038954', 'F', '90311 O\'Conner Locks Apt. 225 - Bowling Green, MO / 39880', 'NA');
INSERT INTO perfil VALUES ('29', 'Mari', 'Estevez', 'Gonzalo', '73964', '+8089916696596', 'F', '72833 Kelli Drive Suite 851 - Fargo, LA / 76175', 'NA');
INSERT INTO perfil VALUES ('30', 'Aaron', 'Velasco', 'Torres', '63003', '+826634625914', 'M', '25500 Terry Mews Suite 924 - Rock Island, CT / 70268', 'NA');
INSERT INTO perfil VALUES ('31', 'Alvaro', 'del Moral', 'Jaime', '91647', '+99056198571544', 'M', '881 Bradtke Lake Suite 039 - Dover, ID / 57317', 'NA');
INSERT INTO perfil VALUES ('32', 'Ana Belen', 'Rey', 'Marti', '20537', '+333107195207', 'F', '25792 Beier Expressway Apt. 136 - Spartanburg, NE / 32297', 'NA');
INSERT INTO perfil VALUES ('33', 'Ayman', 'San Jose', 'Dieguez', '13083', '+979285484955', 'F', '2588 Luettgen Station Suite 267 - Anchorage, NE / 42272', 'NA');
INSERT INTO perfil VALUES ('34', 'Orlando', 'Cardona', 'Cuadrado', '82175', '+0983274255208', 'M', '18220 Jones Islands Suite 022 - Missoula, VA / 77846', 'NA');
INSERT INTO perfil VALUES ('35', 'Humberto', 'Zheng', 'Carrion', '54252', '+816319164003', 'M', '077 Lambert Ville Apt. 389 - Bellevue, MA / 49156', 'NA');
INSERT INTO perfil VALUES ('36', 'Jacinto', 'Palau', 'Alavares', '93737', '+6867099842304', 'M', '82121 King Stream Apt. 895 - Grand Forks, CT / 55256', 'NA');
INSERT INTO perfil VALUES ('37', 'Candida', 'Real', 'Rubio', '90428', '+8738030956357', 'F', '0909 Greenfelder Square Apt. 901 - Burlington, IN / 55592', 'NA');
INSERT INTO perfil VALUES ('38', 'Melanie', 'Ariza', 'Maldonado', '47222', '+14673792534939', 'F', '126 Gleason Villages Apt. 998 - Hoover, WY / 85825', 'NA');
INSERT INTO perfil VALUES ('39', 'Antia', 'Ribas', 'Heredia', '74937', '+2665675622089', 'F', '621 Zelma Courts Apt. 099 - Provo, TN / 93270', 'NA');
INSERT INTO perfil VALUES ('40', 'Gerard', 'Montes', 'Calero', '52420', '+04376549174013', 'M', '146 Luna Cape Suite 493 - Portage, OR / 19345', 'NA');
INSERT INTO perfil VALUES ('41', 'Chupapi', 'Muñaño', 'Marcos', '35080', '+7174129473743', 'M', '983 Beier Hill Suite 726 - Kearny, WV / 04772', 'NA');
INSERT INTO perfil VALUES ('42', 'Jesus Steven', 'Pulido', 'Romero', '80609', '+4885004647706', 'M', '790 Shanahan Stream Apt. 384 - Grand Junction, GA / 35598', 'NA');
INSERT INTO perfil VALUES ('43', 'Josefina', 'Pulido', 'Sanatanez', '72445', '+744586770418', 'F', '396 Rolfson Brooks Suite 921 - Pocatello, WA / 12579', 'NA');
INSERT INTO perfil VALUES ('44', 'Michael', 'Paranco', 'Alavares', '94380', '+42335926480151', 'M', '98215 Schaden Meadows Suite 835 - Lancaster, AL / 34239', 'NA');
INSERT INTO perfil VALUES ('45', 'Josita', 'Real', 'Palacias', '33618', '+88328096801980', 'F', '2582 Kris Light Suite 571 - Elkhart, GA / 65223', 'NA');

SELECT * FROM hotel_palace.perfil;

-- Datos de tabla receptor

INSERT INTO receptor VALUES ('26589', 'Naia', 'Camara', 'Marques', '(55)104-97-39001', 'Matutino', 'NA');
INSERT INTO receptor VALUES ('63666', 'Arantxa', 'Bustamante', 'Yañez', '(55)104-20-86459', 'Vespertino', 'NA');
INSERT INTO receptor VALUES ('90903', 'Mamadou', 'Mamadou', 'Mena', '(55)349-23-73505', 'Matutino', 'NA');
INSERT INTO receptor VALUES ('86367', 'Iban', 'Nicolas', 'Gonzales', '(55)553-94-49621', 'Matutino', 'NA');
INSERT INTO receptor VALUES ('26990', 'Melania', 'Amat', 'Mota', '(55)647-40-10913', 'Vespertino', 'NA');
INSERT INTO receptor VALUES ('35693', 'Jesús', 'Palomares', 'Prats', '(55)056-89-29584', 'Vespertino', 'NA');
INSERT INTO receptor VALUES ('95153', 'Marcelino', 'Madrid', 'Aznar', '(55)235-63-18575', 'Matutino', 'NA');
INSERT INTO receptor VALUES ('54580', 'Gustavo', 'Redondo', 'Carmona', '(55)599-70-88329', 'Vespertino', 'NA');
INSERT INTO receptor VALUES ('40284', 'Abril', 'Aguilera', 'Lorente', '(55)889-07-49151', 'Vespertino', 'NA');
INSERT INTO receptor VALUES ('66543', 'Alfonsa', 'Martos', 'Rodenas', '(55)079-26-40135', 'Matutino', 'NA');

SELECT * FROM hotel_palace.receptor;

-- datos de la tabla de paquetes

INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('1', 'Paquete Estandar', '2000', 'desayuno,comida y cena con solo 4 acesos 1 por dia + acceso a picina', '3 estrellas', '4');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('2', 'Paquete Economico', '1600', '1 habitacion y solo un acceso para un dia con las 3 comidas.', '4 estrellas', '2');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('3', 'Paquete semanal', '3300', '7 deayunos,7 comidas ,7 cenas + 1 accesoa piscina.', '5 estrellas', '7');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('4', 'Paquete dia festivo', '1200', 'acceso a spa+ 1 comida media tarde y 1 cena.', '5 estrellas', '1');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('5', 'Paquete diurno', '1800', 'Durante la instancia podran tener desayunos .', '2 estrellas', '3');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('6', 'Paquete nocturno', '1800', 'Durante la instancia podran tener cenas .', '2 estrellas', '3');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('7', 'Paquete completo', '3600', 'Comidas del dia gratis+ acceso a spa+ piscina+ viaje al mirador.', '5 estrellas', '7');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('8', 'Paquete expedicion', '2500', '1 desayuno,comida y cena+ viaje al mirador gratis.', '5 estrellas', '2');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('9', 'Paquete de visita', '1200', '1 comida y 1 cena.', '5 estrellas', '1');
INSERT INTO `hotel_palace`.`paquetes` (`id_paquete`, `nombre`, `costo_paquete`, `descripcion`, `Valoracion`, `num_noches`) VALUES ('10', 'Paquete flexible', '3100', '4 dias con acceso a desayunos y cenas+ acceso a piscina.', '5 estrellas', '7');

SELECT * FROM hotel_palace.paquetes;