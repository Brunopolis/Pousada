<?php

$servidor = "localhost";
$usuario = "root";
$senha = "";
$dbname = "pousada";

$mysqli = new mysqli($servidor, $usuario, $senha, $dbname);

if($mysqli->connect_errno){
    echo "Falha ao conectar: (". $mysqli->connect_errno .") ".$mysqli->connect_error;
} else{
    echo "Conectado";
} 