from datetime import datetime
semana = 0

print('SISTEMA DE POUSADA')
while True:
    preco = 0
    r = int(input("Escolha a opção desejada \n[1] Alugar Quarto \n[0] Sair \nR: "))
    print()
    if r == 0:
        break 
    elif r == 1:
        r = int(input("Selecione o tipo de quarto desejado \n[1] Individual \n[2] Duplo \n[0] Voltar \nR: "))
        print()
        if r == 1:
            p1 = 1400
            p2 = 2380
            ent = input("Selecione a data de entrada (dia/mes/ano): ")
            data_entrada = datetime.strptime(ent, "%d/%m/%Y").date()
            sai = input("Selecione a data de saída (dia/mês/ano): ")
            data_saida = datetime.strptime(sai, "%d/%m/%Y").date()
            dif = int((data_saida - data_entrada).days)

            if dif >= 7:
                while dif >= 7:
                    dif -= 7
                    semana += 1
            print(f'\nEstadia de {semana} semana(s) e {dif} dia(s)')

            print(f"""
            Os planos disponíveis para quarto individual (R$ 200,00 - diária) são:
                - 1º Pacote - Uma semana - R$ 1.400,00
                - 2º Pacote - Duas semanas - R$ 2.380,00 - 15% de desconto
                - 3º Pacote - Um mês - R$ 4.500,00 - 25% de desconto
            """)

            pac = 'O melhor plano de pagamento com base no seu tempo de estadia é de '

            if(semana == 1 and dif < 5):
                preco = p1 + (200 * dif)
                pac += f"1 pacote de 1 semana + pagamento de diárias individuais. Custando R$ {preco},00"
            elif(semana == 1):
                preco = p2
                pac += f'1 pacote de 2 semanas. Custando R$ 2380,00, tendo 15% de desconto.'
            elif(semana == 2 and dif < 7):
                preco = p2 + (200 * dif)
                pac += f"1 pacote de 2 semanas + pagamento de diárias individuais. Custando R$ {preco},00"
            elif semana == 3 and dif == 0:
                preco = p1 + p2
                pac += f"1 pacote de 2 semanas + 1 pacote de 1 semana. Custando R$ {p2 + p1},00"
            elif semana == 3 and dif <= 3:
                pac += f"1 pacote de 2 semanas + 1 pacote de 1 semana + diárias. Custando R$ {p2 + p1 + (200 * dif)},00"
            elif semana == 3 and dif > 3:
                pac += f"1 pacote de 1 mês. Custando R$ 4500,00"
            elif semana >= 4:
                mes = 0
                preco = 0
                while semana >= 4:
                    semana -= 4
                    mes += 1
                    preco += 4500
                pac += f" {mes} pacote(s) de 1 mês "
                if(semana == 1 and 0 < dif < 5):
                    preco += (200 * dif)
                    pac += f"e 1 pacote de 1 semana + pagamento de diárias individuais. Custando R$ {preco},00"
            print(pac,end="\n")
            r = int(input("Deseja contratar esse pacote? \n[1] Sim \n[2] Ver outras opções \nR: "))
            print()
            if r == 1:
                print(f'Pacote de quarto individual contratado! \nData de entrada: {data_entrada} \nData de saída: {data_saida} \nValor a pagar: R$ {preco},00\n')
            elif r == 2:
                preco = 0
                while True:
                    print('Selecione os pacotes que deseja adicionar')
                    r = int(input('[1] Diária (R$ 200,00) \n[2] 1 Semana (R$ 1400,00) \n[3] 2 Semanas (R$ 2380,00) \n[4] 1 Mês (R$ 4500,00) \n[0] Finalizar \nR: '))
                    print()
                    if r == 1:
                        preco += 200
                    elif r == 2:
                        preco += 1400
                    elif r == 3:
                        preco += 2380
                    elif r == 4:
                        preco += 4500
                    elif r == 0 and preco == 0:
                        print('\nNenhum pacote contratado!\n')
                        break
                    elif r == 0:
                        print(f'\nPacote de quarto individual contratado! \nData de entrada: {data_entrada} \nData de saída: {data_saida} \nValor a pagar: R$ {preco},00\n')
                        break
