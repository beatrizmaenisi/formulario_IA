// Função para limpar os campos do formulário
function limparFormulario() {
    document.getElementById("clienteForm").reset();
    document.getElementById("resultado").innerText = "";
}

//Enviar dados para gerar a classificação
document.getElementById("clienteForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o recarregamento da página
    const form = document.getElementById("clienteForm");
    form.submit(); // Envia manualmente o formulário ao Flask

    let formData = newFormData(this);
    fetch("/prever",{
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(html => {
        document.open();
        document.write(html);
        document.close();
    })
    .catch(error => console.error("Erro:",error))
});
