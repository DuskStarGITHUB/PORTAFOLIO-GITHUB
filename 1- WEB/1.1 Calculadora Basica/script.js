// Obtener referencia al campo de entrada y al elemento de salida
const inputField = document.getElementById("inputField");
const outputElement = document.getElementById("output");

// Agregar un listener al campo de entrada para capturar eventos de entrada
inputField.addEventListener("input", () => {
  // Obtener el valor actual del campo de entrada
  const inputValue = inputField.value;

  // Llamar a la función calculate con el valor de entrada
  calculate(inputValue);
});

// Función para calcular y mostrar el resultado de una operación
function calculate(inputValue) {
  try {
    // Evaluar la expresión ingresada en el campo de entrada
    const result = eval(inputValue);

    // Mostrar el resultado en el elemento de salida
    outputElement.textContent = result;
  } catch (error) {
    // En caso de error, mostrar "Error" en el elemento de salida
    outputElement.textContent = "Error";
  }
}
