<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="idex.css">
    <title>Sistema de Pousada</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <article>
        <div class="fotos">
        <h1>Frase motivacional</h1>
        </div>
        <div class="formulario">
            <form method="POST" action="processa.php">
                <h2>Veja datas disponveis</h2>
                <div class="dados">
                <input name="nome" class="coletor" type="text" placeholder="Nome completo">
                <input name="cpf" class="coletor" type="text" placeholder="CPF ou CNPJ">
                <input name="tel" class="coletor" type="text" placeholder="Telefone">
                <input name="email" class="coletor" type="text" placeholder="Email">
                </div>
                <h3>Endereço</h3>
                <div class="endereço">
                    <input name="log" class="coletor" type="text" placeholder="Logradoro">
                    <input name="num" class="coletor" type="text" placeholder="Número">
                    <input name="cep" class="coletor" type="text" placeholder="CEP">
                    <input name="cidade" class="coletor" type="text" placeholder="Cidade">
                    <input name="bairro" class="coletor" type="text" placeholder="Bairro">
                    <input name="ref" class="coletor" type="text" placeholder="Ponto de referência">
                </div>
                <h3>Datas</h3>
                <div class="date">
                    <label>Data de Entrada:</label>
                    <input name="dataent" class="data" type="date">
                    <label>Data de Saída:</label>
                    <input name="datasai" class="data" type="date">
                </div>
                <input type="submit" value="Enviar">
            </form>
        </div>

    </article>
</body>
</html>