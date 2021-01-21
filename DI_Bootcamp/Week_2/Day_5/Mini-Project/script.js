function my_f(argument) // get the value of the clicked button and store it 
{ 
    document.getElementById("result").value += argument; 
} 

function solver() // function call when solver is clicked
{ 
    let newValue = document.getElementById("result").value;

    let nextValue = eval(newValue); // calculating the value

    document.getElementById("result").value = nextValue;  // displaying the result
}

function reset()
{ 
    document.getElementById("result").value = ""; // Resets the value in the display to 0
}