// TEMPERATURE CONVERTER APP

// when the submit button is clicked

// take the input in the temperature input 

// if the radio option checked is celsius

// do a calculation that converts the input from fahrenheit to celsius

// if the radio option checked is fahrenheit

// do a calculation that converts the input from celsius to fahrenheit 

document.getElementById("submit_button").onclick = function(){

  let temperature;

  if (document.getElementById("celsius_radio").checked == true){
    // a number will be entered so get the value
    temperature = document.getElementById("temperature_input").value;
    // the number will be a string so convert it to a number 
    temperature = Number(temperature);
    temperature = toCelsius(temperature);
    document.getElementById("temperature").textContent = temperature + "°C"
  }
  else if (document.getElementById("fahrenheit_radio").checked == true){
    temperature = document.getElementById("temperature_input").value;
    // the number will be a string so convert it to a number 
    temperature = Number(temperature);
    temperature = toFahrenheit(temperature);
    document.getElementById("temperature").textContent = temperature + "°F"
  }
  else {
    document.getElementById("temperature").textContent = "Select a unit"
  }

}

function toCelsius(temperature){
  return (temperature - 32) * (5/9);
}

function toFahrenheit(temperature){
  return (temperature * (9 /5)) + 32;
}

// declare and assign variable temperature

// at the end of the startProgram, declare 2 functions. toCelsuis and toFahrenheit. 


// ------------------------------------------------------------------------------------------

// NUMBER GUESSING GAME 

// // let x = Math.floor(Math.random() * 10 + 1);
const answer = Math.floor(Math.random() * 10 + 1)
// answer will be a random number between 1 and 10.

// keep track of our guesses 
let guesses = 0

// when we click on the button we would like to run a function that iterates the guesses
document.getElementById("submitButton").onclick = function (){
  let guess = document.getElementById("guessField").value;
  guesses += 1;


  if(guess == answer){
    alert(`${answer} is the number. It took you ${guesses} guesses`);
  }
  else if (guess < answer){
    alert("Too small!");
  }
  else{
      alert("Too large!");
  }

}

