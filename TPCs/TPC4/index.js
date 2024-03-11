
const botao_exercicio = document.getElementById("exercicio");
const botao_desporto = document.getElementById("desporto");
const botao_aprender = document.getElementById("aprender");
const botao_artes = document.getElementById("artes");

const descricao_exercicio = document.getElementById("descricao_exercicio");
const descricao_desporto = document.getElementById("descricao_desporto");
const descricao_aprender = document.getElementById("descricao_aprender");
const descricao_artes = document.getElementById("descricao_artes");

botao_exercicio.addEventListener("click", event => {
    descricao_exercicio.style.display = "flex";
    descricao_desporto.style.display = "none";
    descricao_aprender.style.display = "none";
    descricao_artes.style.display = "none";
    window.scrollTo(0, 10000);
});

botao_desporto.addEventListener("click", event => {
    descricao_exercicio.style.display = "none";
    descricao_desporto.style.display = "flex";
    descricao_aprender.style.display = "none";
    descricao_artes.style.display = "none";
    window.scrollTo(0, 10000);
});

botao_aprender.addEventListener("click", event => {
    descricao_exercicio.style.display = "none";
    descricao_desporto.style.display = "none";
    descricao_aprender.style.display = "flex";
    descricao_artes.style.display = "none";
    window.scrollTo(0, 10000);
});

botao_artes.addEventListener("click", event => {
    descricao_exercicio.style.display = "none";
    descricao_desporto.style.display = "none";
    descricao_aprender.style.display = "none";
    descricao_artes.style.display = "flex";
    window.scrollTo(0, 10000);
});