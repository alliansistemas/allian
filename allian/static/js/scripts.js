// Função para obter a data atual no formato YYYY-MM-DD
function obterDataAtual() {
    const dataAtual = new Date();
    const ano = dataAtual.getFullYear();
    let mes = (dataAtual.getMonth() + 1).toString().padStart(2, '0'); // Adiciona zero à esquerda, se necessário
    let dia = dataAtual.getDate().toString().padStart(2, '0'); // Adiciona zero à esquerda, se necessário

    return `${ano}-${mes}-${dia}`;
}

// Define a data atual no campo de entrada de data
document.getElementById('id_aniversario').value = obterDataAtual();
document.getElementById('data_pesquisa').value = obterDataAtual();

const dataPesquisaInput = document.getElementById("data_pesquisa");

// Obtenha a data atual no formato correto para o campo de entrada de data
const today = new Date().toISOString().slice(0, 10);

// Defina o valor do campo de entrada para a data atual
dataPesquisaInput.value = today;