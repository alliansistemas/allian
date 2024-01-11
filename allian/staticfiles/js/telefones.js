var alertaTelefoneExibido = false;

function validarTelefone() {
  var telefone = document.getElementById('telefone').value;
  telefone = telefone.replace(/\D/g, ''); // Remove caracteres não numéricos

  if (telefone.length === 0 && !alertaTelefoneExibido) {
    alert('Insira o Telefone!');
    alertaTelefoneExibido = true;
    setTimeout(function() {
      document.getElementById('telefone').focus();
    }, 0);
  } else if (telefone.length < 10) {
    alertaTelefoneExibido = true;
    alert('Telefone inválido!');
    setTimeout(function() {
      document.getElementById('telefone').focus();
    }, 0);
  } else if (telefone.length > 11) {
    alertaTelefoneExibido = true;
    alert('Telefone inválido!');
    setTimeout(function() {
      document.getElementById('telefone').focus();
    }, 0);
  } else if ((telefone.length === 11 || telefone.length === 10) && !alertaTelefoneExibido) {
    alertaTelefoneExibido = false;
  } else if (telefone.length >= 1 && telefone.length <= 9) {
    alert('Telefone inválido!');
    alertaTelefoneExibido = true;
  }
}
