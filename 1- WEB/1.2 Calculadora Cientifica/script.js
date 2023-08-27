class CalculadoraBasica {
  constructor() {
    // Define una expresión regular para verificar operaciones básicas.
    this.basicOperationShape = new RegExp(
      "(([1-9][0-9]*|[0.])(.[0-9]*[1-9])?[-+*/])(([1-9][0-9]*|[0.])(.[0-9]*[1-9])?)"
    );
    // Inicializa el registro de memoria en 0.
    this.memoryRegister = 0;
  }

  // Imprime el contenido del registro de memoria en la pantalla.
  printMemoryContents() {
    this.clearDisplay();
    this.writeToDisplay(this.memoryRegister);
  }

  // Resta el resultado de la operación actual del registro de memoria.
  subtractFromMemory() {
    this.memoryRegister -= this.solveOperation();
  }

  // Suma el resultado de la operación actual al registro de memoria.
  addToMemory() {
    this.memoryRegister += this.solveOperation();
  }

  // Escribe el dato en la pantalla.
  writeToDisplay(data) {
    let legacy = document.getElementById("displayBox").value;
    if (data == ".") {
      legacy += data;
    } else {
      legacy = legacy == "0" ? data : (legacy += data);
    }
    document.getElementById("displayBox").value = legacy;
  }

  // Escribe el operador en la pantalla.
  writeOperatorToDisplay(operator) {
    let legacy = document.getElementById("displayBox").value;
    // Si ya hay una operación básica en pantalla, resuelve la operación.
    if (this.basicOperationShape.test(legacy)) {
      this.solveOperation();
    }
    this.writeToDisplay(operator);
  }

  // Limpia la pantalla.
  clearDisplay() {
    document.getElementById("displayBox").value = "0";
  }

  // Resuelve la operación actual y muestra el resultado en la pantalla.
  solveOperation() {
    let operation = document.getElementById("displayBox").value;
    let result = 0;
    try {
      result = eval(operation == "" ? 0 : operation);
    } catch (err) {
      alert("Error de sintaxis");
      this.clearDisplay();
    }
    document.getElementById("displayBox").value = result;
    return result;
  }
}

class CalculadoraCientifica extends CalculadoraBasica {
  constructor() {
    super();
    // Inicializa una lista de entradas y una cadena para la operación.
    this.inputList = new Array();
    this.operationString = "";
    this.justSolved = false;
    // Define un mapeo de funciones científicas.
    this.operationMap = {
      "sin(": "Math.sin(",
      "cos(": "Math.cos(",
      "tan(": "Math.tan(",
      "log(": "Math.log10(",
      "ln(": "Math.log(",
      "sqrt(": "Math.sqrt(",
      PI: "Math.PI",
      e: "Math.E",
    };
  }

  /**
   * Escribe la nueva entrada del usuario en la pantalla.
   *
   * @param {String} data Los datos para mostrar en la pantalla.
   * Provistos por un clic de botón del usuario.
   */
  writeToDisplay(data) {
    if (document.getElementById("displayBox").value == "Error de sintaxis") {
      super.clearDisplay();
    }
    super.writeToDisplay(data);
    this.operationString += data;
    this.inputList.push(data);
  }

  /**
   * Escribe el operador seleccionado por el usuario en la pantalla.
   *
   * @param {String} operator Una cadena que representa el operador
   * seleccionado por el usuario.
   */
  writeOperatorToDisplay(operator) {
    if (document.getElementById("displayBox").value == "Error de sintaxis") {
      super.clearDisplay();
    }
    this.operationString += operator;
    super.writeToDisplay(operator);
    this.inputList.push(operator);
  }

  /**
   * Resuelve la operación actualmente mostrada en la calculadora.
   * Si la sintaxis no es correcta para una expresión aritmética bien formada,
   * se mostrará un error y la pantalla mostrará 0.
   * Debido a la complejidad de la verificación de expresiones regulares,
   * esta tarea requeriría una gramática libre de contexto u otra técnica.
   *
   * ~Tomado de StackOverflow~
   * No se pueden encontrar paréntesis coincidentes con expresiones regulares.
   * Esto es una consecuencia del lema de bombeo para lenguajes regulares.
   * ~Tomado de StackOverflow~
   */
  solveOperation() {
    let result = 0;
    try {
      result = eval(
        this.operationString == "" || this.operationString == "Error de sintaxis"
          ? 0
          : this.operationString
      );
    } catch (err) {
      result = "Error de sintaxis";
    }
    document.getElementById("displayBox").value = result;
    this.operationString = "";
    this.operationString += result;
    this.justSolved = true;
    return result;
  }

  /**
   * Limpia la pantalla.
   */
  clearDisplay() {
    super.clearDisplay();
    this.operationString = "";
  }

  // Cambia el signo del número en pantalla.
  toggleSign() {
    var displayBox = document.getElementById("displayBox");
    var displayContents = displayBox.value;
    if (displayContents == "Error de sintaxis") {
      super.clearDisplay();
    }
    if (displayContents == "0") {
      displayBox.value = "-";
      this.operationString += "-";
    } else {
      displayBox.value = "-" + displayBox.value;
      this.operationString = "-" + this.operationString;
    }
  }

  // Limpia el registro de memoria.
  clearMemory() {
    super.subtractFromMemory(this.memoryRegister);
  }

  // Lee el contenido del registro de memoria y muestra en pantalla.
  readMemory() {
    this.clearDisplay();
    this.writeToDisplay(this.memoryRegister);
  }

  // Guarda el resultado de la operación actual en el registro de memoria.
  saveToMemory() {
    this.memoryRegister = this.solveOperation();
  }

  // Borra la última entrada.
  eraseLastInput() {
    this.inputList.pop();
    var recreatedOperation = "";
    for (var each in this.inputList) {
      recreatedOperation += this.inputList[each];
    }
    document.getElementById("displayBox").value = recreatedOperation;
    for (var each in this.operationMap) {
      recreatedOperation = recreatedOperation.replace(
        each,
        this.operationMap[each]
      );
    }
    this.operationString = recreatedOperation;
  }

  // Escribe una función matemática en pantalla.
  writeMathFunction(data) {
    if (document.getElementById("displayBox").value == "Error de sintaxis") {
      super.clearDisplay();
    }
    super.writeToDisplay(data);
    this.operationString += this.operationMap[data];
    this.inputList.push(data);
  }

  // Calcula el factorial de un número.
  calculateFactorial() {
    var number = parseInt(this.operationString.split(new RegExp("[^0-9]")));
    var result = 0;
    try {
      result = this.calculateRecursiveFactorial(number);
    } catch (err) {
      document.getElementById("displayBox").value = "Ese número es demasiado grande";
    }
    this.clearDisplay();
    document.getElementById("displayBox").value = result;
  }

  // Calcula el factorial de manera recursiva.
  calculateRecursiveFactorial(number) {
    if (number == 1 || number == 0) {
      return 1;
    }
    return number * this.calculateRecursiveFactorial(number - 1);
  }

  // Calcula la potencia de diez elevado a la enésima potencia.
  nthTenPower() {
    var number = parseInt(this.operationString.split(new RegExp("[^0-9]")));
    this.clearDisplay();
    document.getElementById("displayBox").value = Math.pow(
      10,
      parseInt(number)
    );
  }

  // Calcula el cuadrado de un número.
  square() {
    var number = parseInt(this.operationString.split(new RegExp("[^0-9]")));
    this.clearDisplay();
    document.getElementById("displayBox").value = Math.pow(parseInt(number), 2);
  }

  // Calcula el cubo de un número.
  cube() {
    var number = parseInt(this.operationString.split(new RegExp("[^0-9]")));
    this.clearDisplay();
    document.getElementById("displayBox").value = Math.pow(parseInt(number), 3);
  }

  // Calcula el inverso de un número.
  inverseNumber() {
    var number = parseInt(this.operationString.split(new RegExp("[^0-9]")));
    this.clearDisplay();
    document.getElementById("displayBox").value = Math.pow(
      parseInt(number),
      -1
    );
  }
}

// Crea una instancia de la CalculadoraCientifica al cargar la página.
const calculadora = new CalculadoraCientifica();
