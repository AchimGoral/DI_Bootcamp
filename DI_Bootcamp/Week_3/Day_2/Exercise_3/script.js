let buttonSubmit = document.getElementById("submit");

buttonSubmit.addEventListener("click", calc);

function calc(event) {
    document.getElementById("radius").style.border = "";
    event.preventDefault();
    let radiusInput = document.getElementById("radius").value;
    if(isNaN(radiusInput)) {
        radiusInput = "";
        document.getElementById("radius").style.border = "2px solid red";
        alert("Only numbers are alowed");
    }
    let volumeCalc = (4/3) * Math.PI * Math.pow(radiusInput, 3);
    let volumeOutput = document.getElementById("volume");
    volumeOutput.value = volumeCalc;
}