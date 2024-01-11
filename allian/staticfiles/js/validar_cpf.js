var alertaCPFExibido = false;

function validarCPF() {
  var cpf = document.getElementById('cpf').value;
  cpf = cpf.replace(/\D/g, ''); // Remove caracteres não numéricos

  if (cpf.length === 0) {
    alertaCPFExibido = true;
    alert('Insira o CPF!');
    setTimeout(function() {
      document.getElementById('cpf').focus();
    }, 0);
  } else if (cpf.length < 11) {
    alertaCPFExibido = true;
    alert('CPF inválido!');
    setTimeout(function() {
      document.getElementById('cpf').focus();
    }, 0);
  } else if (cpf.length === 11) {
    if (verificaSomaCPF(cpf)) {
      alertaCPFExibido = false;
      // Desbloqueia os outros campos do formulário
      for (var i = 0; i < document.querySelectorAll('input').length; i++) {
        document.querySelectorAll('input')[i].disabled = false;
      }
    } else {
      alertaCPFExibido = true;
      alert('CPF inválido!');
      setTimeout(function() {
        document.getElementById('cpf').focus();
      }, 0);
    }
  }

  // Desabilita o botão de cadastrar se o CPF for inválido
  document.getElementById('cadastrar').disabled = alertaCPFExibido;
}

document.getElementById('cpf').addEventListener('keyup', validarCPF);

function verificaSomaCPF(cpf) {
  cpf = cpf.replace(/\D/g, ''); // Remova caracteres não numéricos novamente

  var soma = 0;
  for (var i = 0; i < 9; i++) {
    soma += parseInt(cpf.charAt(i)) * (10 - i);
  }
  var digitoVerificador1 = soma % 11 < 2 ? 0 : 11 - (soma % 11);

  soma = 0;
  for (var i = 0; i < 10; i++) {
    soma += parseInt(cpf.charAt(i)) * (11 - i);
  }
  var digitoVerificador2 = soma % 11 < 2 ? 0 : 11 - (soma % 11);

  return digitoVerificador1 === parseInt(cpf.charAt(9)) &&
         digitoVerificador2 === parseInt(cpf.charAt(10));
}
