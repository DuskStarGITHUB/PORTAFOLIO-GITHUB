// Instrucciones if else y else if
let edad: number = 18;

if (edad < 18) {
  console.log("Eres menor de edad.");
} else if (edad === 18) {
  console.log("Tienes 18 años.");
} else {
  console.log("Eres mayor de edad.");
}

// BUCLE WHILE
let contador: number = 0;

while (contador < 5) {
  console.log(contador);
  contador++;
}

console.log(" ");

// BUCLE DO WHILE
let contador2: number = 0;

do {
  console.log(contador2);
  contador2++;
} while (contador2 < 5);

console.log(" ");

// Bucle For
for (let i = 0; i < 5; i++) {
  console.log(i);
}

console.log(" ");