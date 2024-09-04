/*
Scripts em JavaScript para registrar meu nível de aprendizado em um só arquivo.
*/


//> Nível Básico
function FirstCodeJS() {
  console.log("Hello World!");
}

function Piramide() {
  console.log("    a\n   b c\n  d e f\n g h i j\n    k ");
}

function Iniciais() {
  console.log(
    "FFFFFF     EEEEEE\nF          E\nFFFF       EEEEE\nF          E\nF          EEEEEE"
  );
}

function Recibo() {
  console.log("================================");
  console.log("        McDONALD's RECEIPT      ");
  console.log("--------------------------------");
  console.log("Item        Quantity      Price ");
  console.log("🍔 Burger      1          $2.99 ");
  console.log("🍟 Fries       1          $2.49 ");
  console.log("🥤 Soda        1          $1.99 ");
  console.log("________________________________");
  console.log("Total                     $7.47");
  console.log("================================");
}

function Variaveis() {
  /* Tipos de váriáveis e suas aplicações
  const userId = 1618033988;
  let userName = "Leeroy Jenkins";
  let progress = 0.75;
  let xp = 60;
  let verified = true;
  */
 const userID = '11111111111';
 const userCPF = '111.111.111.11'
 let userMAIL = 'example@mail.com';
 userBio = 'Hey, its me!'
 userMAIL = 'teste@mail.com'
 userBio = 'hey. i update it!'
 console.log(userBio)
 console.log(userCPF)
}

function StrIntBool(){
  let year = 2024
  let mail = "Example@example.com"
  let hungry = true
  console.log(year)
  console.log(mail)
  console.log(hungry)
}

function FahrenheitCelsius(){
  let fah = 98 //Mude o grau aqui.
  let c = (fah - 32)/1.8
  console.log("está fazendo", c,"graus celsius.")
}

function IMC(){
  let massa = 98.0 //Mude a massa aqui.
  let altura = 1.69 //Mude a altura aqui em cm.
  const imc = massa/(altura**2)
  console.log('seu imc é:', imc)
}

function Currency(){
  //Yuan Chines
  let yuan = 560  // Altere o valor aqui.
  //Iene Japones
  let yen = 2455  // Altere o valor aqui.
  //Won Sul-Coreano
  let won = 3280  // Altere o valor aqui.
  //total
  let totalusd = yuan*0.14 + yen*0.0069 + won*0.00075
  console.log('Você possui:', totalusd, 'em dolar')
}



// Run
Currency();
