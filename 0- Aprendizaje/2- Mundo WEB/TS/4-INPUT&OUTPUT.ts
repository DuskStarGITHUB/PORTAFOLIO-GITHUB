// ENTRADA DE DATOS
let nombre: string | null = prompt("Por favor, ingresa tu nombre:");

if (nombre !== null) {
    console.log(`Hola, ${nombre}!`);
} else {
    console.log("No ingresaste ningún nombre.");
}

// ----------------------------
let nombre2: string = "Juan";
console.log(`Hola, ${nombre2}!`);
