const nome = document.querySelector('#nome');
const cpf = document.querySelector('#cpf');
const telefone = document.querySelector('#telefone');
const email = document.querySelector('#email');
const logradouro = document.querySelector('#logradouro');
const numero = document.querySelector('#numero');
const cep = document.querySelector('#cep');
const cidade = document.querySelector('#cidade');
const bairro = document.querySelector('#bairro');
const referencia = document.querySelector('#referencia');
const dataentrada = document.querySelector('#dataentrada');
const datasaida = document.querySelector('#datasaida');
const individuais = document.querySelector('#individuais');
const duplos = document.querySelector('#duplos');

const confirmacao = document.querySelector('.confirmaçao')

const bntEnvia = document.querySelector('#btnenviar');

bntEnvia.addEventListener('click', function(e){
    const p = document.createElement('p');
    p.innerText = dataentrada.value;
    confirmacao.appendChild(p);
    p.classList.add('confirmação');
});

