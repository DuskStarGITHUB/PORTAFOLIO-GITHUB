// TPOS DE DATOS Y VARIABLES

// NUMBER (NUMERICO)
let unNumero: number = 5;
console.log(unNumero);
// STRING (TEXTO)
let nombre: string = "DuskStar";
console.log(nombre);
// BOOLEAN (BOOLEANO)
let existe: boolean = true;
let existe2: boolean = false;
console.log(existe + " " + existe2);
// ARRAY (ARREGLO)
let numeros: number[] = [1, 2, 3, 4, 5];
console.log(numeros);
// TUPLE (TUPLA)
let coordenas: [number, number] = [10, 20];
console.log(coordenas);
// ENUM (SET)
enum DiaSemana {
  Lunes,
  Martes,
  Miercoles,
  Jueves,
  Viernes,
  Sabado,
  Domingo,
}

let dia: DiaSemana = DiaSemana.Domingo;
console.log(dia);

// ANY (CUALQUIER TIPO DE DATO)
let variableCualquiera: any = "Esto podria ser cualquier cosa";
console.log(variableCualquiera);

// VOID (FUNCION QUE NO RETORNA NINGUN VALOR)
function imprimirMensaje(): void {
  console.log("Hola, NYASU!!!");
}
imprimirMensaje();

// NULL Y UNDEFINED (NULO Y SIN DEFINICION)
let valorNulo: null = null;
let valorIndefinido: undefined = undefined;
console.log(valorNulo)
console.log(valorIndefinido)

// //NEVER (REPRESENTA VALOR CUNAOD HAY UNA EXEPCION O BUCLE INFINITO)
// function lanzaError(mensaje: string): never {
//   throw new Error(mensaje);
// }
// lanzaError("Hola");

// OBJECT (REPRESENTA UN VALOR PRIMITIVO)
let persona: object = { nombre: "Asuna", edad: 30 };
console.log(persona);

// UNION (MULTIPLES TIPOS DE VARIABLES)
let union: number | string = 10;
union = "ACHU";
console.log(union);

// INTERSECTION (VARUOS TIPOS EN UNO SOLO)
type A = { a: number };
type B = { b: string };
let ab: A & B = { a: 5, b: "HOLA" };
console.log(ab);

// LITERAL TYPE (ESPECIFICAR VALORES LITERABLES COMO TIPOS)
let estado: "activo" | "inactivo";
estado = "activo";
console.log(estado)

