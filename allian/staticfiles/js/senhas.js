function validarSenhas() {
  var senha = document.getElementById('password').value;
  var confirmarSenha = document.getElementById('confirmar_senha').value;
  var mensagemConfirmarSenha = document.getElementById('mensagemConfirmarSenha');
  var cadastrarBtn = document.getElementById('cadastrarBtn');

  if (confirmarSenha.length > 0) {
    if (senha !== confirmarSenha) {
      mensagemConfirmarSenha.textContent = 'As senhas não coincidem!';
      cadastrarBtn.disabled = true;
    } else {
      mensagemConfirmarSenha.textContent = '';
      cadastrarBtn.disabled = false;
    }
  } else {
    mensagemConfirmarSenha.textContent = '';
    cadastrarBtn.disabled = true;
  }
}

function verificarConfirmarSenhaBlur() {
  var senha = document.getElementById('password').value;
  var confirmarSenha = document.getElementById('confirmar_senha').value;
  var mensagemConfirmarSenha = document.getElementById('mensagemConfirmarSenha');

  if (senha.length > 0 && senha !== confirmarSenha) {
    alert('As senhas não coincidem!');
    setTimeout(function() {
      document.getElementById('confirmar_senha').focus();
    }, 0);
  }
}
