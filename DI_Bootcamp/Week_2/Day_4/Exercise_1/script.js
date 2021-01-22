// Exercise_1

function checkDriverAge (age) {
    if (age < 18) {
        alert(`Sorry, with ${age} you're too young to drive this car. Powering off`);
        return;
    } else if (age == 18) {
        alert(`Congratulations on your first year of driving. Enjoy the ride!`);
        return;
    } else {
        alert(`You are old enough to drive, Powering On. Enjoy the ride!`);
        return;
    }
}

checkDriverAge(prompt(`What is your age?`));

// Exercise_2

function changeEnough (moneyString, money) {
    let change = [0.25, 0.10, 0.05, 0.01];
    let result = 0;
    for (let i = 0; i < change.length; i++) {
        result += change[i]*moneyString[i];
    }
    if (result > money) {
        return true;
    } else {
        return false;
    }
}

console.log(changeEnough([0, 0, 20, 5], 0.75));

// Exercise_3

function multiples () {
    const max_value = 500;  // Maximum value
    let max_lenght = max_value/23; // calculate the steps
    let elements = 0;
    let sum = 0;
    for (let i = 0; i < max_lenght-1; i++) {        //-1 because we start at 0 and not at 1
        elements += 23;
        console.log(`Element ${i+1} is: ${elements}`);
        sum += elements;
    }
    console.log(`My sum is: ${sum}`);
}

multiples();

// Exercise_4

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
};

function checkBasket () {
    let item = prompt(`Which Item do you want?`);
    if(item in amazonBasket) {
        alert(`You got it`);
    } else {
        alert(`Not there`);
    }
}

checkBasket();

// Exercise_5

let shoppingnewList = [];

shoppingnewList.push("banana", "orange", "apple");

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}; 

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
};

function myBill () {
    let priceFinal = 0;
    for(let i = 0; i < shoppingnewList[i]; i++) {
        if(shoppingnewList[i] in prices) {
            priceFinal += prices;
        }
    }
    console.log(priceFinal);
    return priceFinal;
}

myBill();

// Exercise_6

function tipCalculator() {
    let list = [];
    let listInt = [];
    for (let i = 0; i < 3; i++) {
        list.push(prompt(`Put your ${i+1}. bill`));  //Takes in the 3 Bills, but still need to convert to int array
        listInt[i] = parseInt(list[i]);
    }
    console.log(listInt);
    return listInt;
}

function tips() {
    let newList = tipCalculator();
    let tipList = [];
    for (let i = 0; i < newList.length; i++) {
        if (newList[i] < 50) {
            tipList.push(newList[i]*0.2);
            newList[i] += tipList[i];
        } else if (newList[i] >= 50 && newList[i] <= 200) {
            tipList.push(newList[i]*0.15);
            newList[i] += tipList[i];
        } else {
            tipList.push(newList[i]*0.1);
            newList[i] += tipList[i];
        }
    }
    return newList;
}

console.log(tips());

// Exercise_7

function hotel_cost() {
    let nightsHotel = prompt(`How many nights do you want to stay?`);

    while(isNaN(nightsHotel) == true) {
        nightsHotel = prompt(`How many nights do you want to stay?`);
    }

    let nightsHotelInt = parseInt(nightsHotel);
    nightsHotelInt *= 140;

    return nightsHotelInt;
}

// console.log(hotel_cost());

function plane_ride_costs() {
    let place = prompt(`Where do you want to go?`);

    while(isNaN(place) == false) {
        place = prompt(`Where do you want to go?`);
    }

    let costsPlane = 0;
    if (place == "London") {
        costsPlane = 183;
    } else if (place == "Paris") {
        costsPlane = 220;
    } else if (typeof(place) == "string") {
        costsPlane = 300;
    } else {
        place = prompt(`Where do you want to go?`);

        while(isNaN(place) == false) {
            place = prompt(`Where do you want to go?`);
        }
    }

    return costsPlane;
}

// console.log(plane_ride_costs());

function rental_car_costs() {
    let carDays = prompt(`How many days you want the car?`);

    while(isNaN(carDays) == true) {
        carDays = prompt(`How many days you want the car?`);
    }

    let carDaysInt = parseInt(carDays);
    let dailyCost = carDaysInt*40;
    if(carDaysInt > 10) {
        dailyCost *=0.95;
    }

    return dailyCost;
}

// console.log(rental_car_costs());

function total_vacation_cost () {
    let hotel_cost_final = hotel_cost();
    let plane_cost_final = plane_ride_costs();
    let rental_cost_final = rental_car_costs();
    let sum_costs = hotel_cost_final + plane_cost_final + rental_cost_final;

    let finalCosts = console.log(`The car cost: ${rental_cost_final}, the hotel cost: ${hotel_cost_final}, the plane tickets cost: ${plane_cost_final}.\nYou're total costs are: ${sum_costs}`);
    

    return finalCosts;
}

total_vacation_cost();