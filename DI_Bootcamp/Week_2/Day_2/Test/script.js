// let colors = ['red', 'blue', 'yellow'];

// let user = {
//     username : "John",
//     password : 1234,
//     email : "jondoe@gmail.com",
//     LogIn : true,
//     countries : ["Israel", "America"],
//     friends : {
//         name : ["David", "Sarah"]
//     }
// };

let users = [
    {
        username : "John",
        password : 1234
    },
    {
        username : "Lea",
        password : 2222
    },
    {
        username : "David",
        password : 6767
    }
];

for (const n in users) {
    console.log(users[n]);
}

for (const n in users) {
    console.log(users[n].password);
}

// Conditionals

// let bankAmount = 500;
// let acccountNumber = 1234;

// if (bankAmount >= 500 && acccountNumber == 1234) {
//     console.log('I can buy a computer');
// } else {
//     console.log("I can`t buy a computer");
// }

// let age = prompt("what is your age?");

// if (age < 18) {
//     alert("Sorry, you are too young to drive this car. Powering off");
// } else if (age == 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// } else {
//     alert("Powering On. Enjoy the ride!");
// }

// // Ex_2

// let a = 2 + 2;  //a equals 4

// switch (a) {
//   case 3:       // checked and false, skipped to the next one
//     alert( 'Too small' );
//     break;
//    case 4:      // checked and true
//     alert( 'Exactly!' );    //Exactly! will be printed out
//     break;  //We are leaving the switch case
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }

// // Ex_3

// let b = 2 + 2;      // b equals 4

// switch (b) {
//   case 4:           // Statement is true
//     alert('Right!');    //Right! will be printed
//     break;          // Leaveing the switch statement

//   case 3: // (*) grouped two cases (Doesn't mater for us)
//   case 5:
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     break;

//   default:
//     alert('The result is strange. Really.');
// }