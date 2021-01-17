let num1 = prompt('Choose your first number');
let number1 = parseInt(num1);
let num2 = prompt('Choose your second number');
let number2 = parseInt(num2);
let variable = prompt('Choose your second operation: +, -, *, /');
let calc;

if (variable == '+') {
    calc = number1 + number2;
    alert(`Your result is: ${calc}`);
}

else if (variable == '-') {
    calc = number1 - number2;
    alert(`Your result is: ${calc}`);
}

else if (variable == '*') {
    calc = number1 * number2;
    alert(`Your result is: ${calc}`);
}

else if (variable == '/') {
    calc = number1 / number2;
    alert(`Your result is: ${calc}`);
}

else {
    alert(`This is not a valid calculation`);
}