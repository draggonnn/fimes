document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault();
    alert('Obrigado pelo seu contato! Em breve retornaremos.');
    this.reset(); // Limpa o formulário após o envio
});
