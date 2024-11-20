document.getElementById('imc-form').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
  
    if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {
      alert("Por favor, insira valores válidos.");
      return;
    }
  
    const imc = weight / (height * height);
    let message = '';
  
    if (imc < 18.5) {
      message = `Seu IMC é ${imc.toFixed(2)}. Você está abaixo do peso.`;
      document.getElementById('result').style.color = 'blue';
    } else if (imc >= 18.5 && imc <= 24.9) {
      message = `Seu IMC é ${imc.toFixed(2)}. Você está com peso normal.`;
      document.getElementById('result').style.color = 'green';
    } else {
      message = `Seu IMC é ${imc.toFixed(2)}. Você está acima do peso.`;
      document.getElementById('result').style.color = 'red';
    }
  
    document.getElementById('result').textContent = message;
  });
  