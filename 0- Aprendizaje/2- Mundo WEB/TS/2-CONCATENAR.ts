// OPERADOR +
let saludo: string = "HOLA ";
let nombre: string = "DuskStar" + "Dust ";
type edad = { a: number };
type texto = { b: string };
let miEdad: edad & texto = { a: 20, b: " años" };
const mensaje = saludo + nombre + miEdad.a + miEdad.b;
console.log(mensaje);

// METODO concat()
let parte1: string = "Hola, ";
let parte2: string = "Mundo";
let mensajillo: string = parte1.concat(parte2);
console.log(mensajillo);

// PLANTILLAS DE CADENA (usar comillas inveridas ´${}´
let iaNombre: string = "Asuna";
let iaEdad: number = 19;
let iaMensaje: string = `Hola, mi nombre es ${iaNombre} y tengo ${iaEdad} años.`;
console.log(iaMensaje);
