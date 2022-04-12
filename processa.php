<?php
include("conexao.php");

$nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_STRING);
$cpf = filter_input(INPUT_POST, 'cpf', FILTER_SANITIZE_STRING);
$tel = filter_input(INPUT_POST, 'tel', FILTER_SANITIZE_STRING);
$email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
$log = filter_input(INPUT_POST, 'log', FILTER_SANITIZE_STRING);
$num = filter_input(INPUT_POST, 'num', FILTER_SANITIZE_STRING);
$cep = filter_input(INPUT_POST, 'cep', FILTER_SANITIZE_STRING);
$cidade = filter_input(INPUT_POST, 'cidade', FILTER_SANITIZE_STRING);
$bairro = filter_input(INPUT_POST, 'bairro', FILTER_SANITIZE_STRING);
$ref = filter_input(INPUT_POST, 'ref', FILTER_SANITIZE_STRING);

$dataent = filter_input(INPUT_POST, 'dataent');
$datasai = filter_input(INPUT_POST, 'datasai');

echo "Data de entrada: $dataent <br>";
echo "Data de saida: $datasai <br>";

$result_cliente = "INSERT INTO cliente (nome, cpf, telefone, email, logradouro, numero, cep, cidade, bairro, referencia) VALUES ('$nome', '$cpf', '$tel', '$email', '$log', '$num', '$cep', '$cidade', '$bairro', '$ref')";
$resultado_cliente = mysqli_query($mysqli, $result_cliente);