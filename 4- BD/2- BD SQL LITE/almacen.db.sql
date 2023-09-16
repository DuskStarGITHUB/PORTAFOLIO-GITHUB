BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "registro" (
	"id"	INTEGER NOT NULL UNIQUE,
	"modelo"	TEXT NOT NULL,
	"matricula"	TEXT NOT NULL,
	"fecha_entrada"	TEXT NOT NULL,
	"fecha_salida"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "personas" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"apellido_paterno"	TEXT NOT NULL,
	"apellido_materno"	TEXT NOT NULL,
	"vehiculo"	INTEGER UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("vehiculo") REFERENCES "registro"("id")
);
CREATE TABLE IF NOT EXISTS "cobros" (
	"id"	INTEGER NOT NULL UNIQUE,
	"persona"	INTEGER NOT NULL UNIQUE,
	"vehiculo"	INTEGER NOT NULL UNIQUE,
	"deudo"	NUMERIC NOT NULL,
	"estado"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("persona") REFERENCES "personas"("id"),
	FOREIGN KEY("vehiculo") REFERENCES "registro"("id")
);
COMMIT;
