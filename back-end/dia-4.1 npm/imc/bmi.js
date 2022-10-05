const readline = require('readline-sync');

const IMC = (altura, peso) => {
  const BMI = peso / altura ** 2;

  return BMI;
};

const main = async () => {
  const altura = readline.questionFloat('Qual a sua altura: ');
  const peso = readline.questionFloat('Qual o seu peso: ');
  const bmi = IMC(altura, peso);

  console.log(`
    Sua altura é de ${altura}, 
    Seu peso é de ${peso}, 
    BMI: ${bmi.toFixed(2)}
  `);

  if (bmi < 18.5) {
    console.log('Abaixo de 18,5	Abaixo do peso (magreza)');
  } else if (bmi <= 24.9) {
    console.log('Peso normal');
  } else if (bmi <= 29.9) {
    console.log('Acima do peso (sobrepeso)');
  } else if (bmi <= 34.9) {
    console.log('Obesidade grau I');
  } else if (bmi < 40) {
    console.log('Obesidade grau II');
  } else {
    console.log('Obesidade graus III e IV');
  }
}

main();
