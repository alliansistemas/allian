function listen() {
    const options = {
        method: "GET",
        mode: "cors",
        caches: "default"}
    const cep = document.getElementById("cep")
    cep.addEventListener("blur", (e) => {
        let Cep = document.getElementById("cep").value;
        console.log(Cep)
        let search = cep.value.replace("-", "")
        fetch(`https://viacep.com.br/ws/${search}/json/`, options).then((response) => {
            response.json().then(data => {
                console.log(data)
                document.getElementById("logradouro").value = data.logradouro;
                document.getElementById("bairro").value = data.bairro;
                document.getElementById("cidade").value = data.localidade;
                document.getElementById("estado").value = data.uf;})})})
    let logradouro = document.getElementById("logradouro").value;
    let bairro = document.getElementById("bairro").value;
    let localidade = document.getElementById("cidade").value;
    let uf = document.getElementById("estado").value;
    let json = {
        "logradouro": logradouro,
        "bairro": bairro,
        "cidade": localidade,
        "estado": uf,}
    console.log(json)}
function init() {listen();}
document.addEventListener("DOMContentLoaded", function() {listen();});