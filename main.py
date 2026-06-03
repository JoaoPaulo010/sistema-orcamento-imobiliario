import csv

print(f"""
Bem-vindo(a) a R.M. Imovéis
trabalhamos com 3 tipos de locação e valores padrões:
1) Apartamentos: \033[32mR$ 700,00 / 1 Quarto\033[0m
2) Casas: \033[32mR$ 900,00 / 1 Quarto\033[0m
3) Estudio: \033[32mR$ 1200,00\033[0m
 
obs: O valor do contrato imobiliário é de \033[32mR$ 2.000,00\033[0m divididos em até 5 vezes
""")

valor_total = 0
valor_apartamento = 700
valor_casa = 900
valor_estudio = 1200
contrato_imob = 2000

def estacionamento(valor_total):
    print("Para incluir a vaga de garagem deve-se pagar R$ 300,00")
    vaga_estacionamento = validar_opc_alf('Deseja incluir vaga de estacionamento? (S) / (N) > ', ("S", "N"))

    if vaga_estacionamento == "S":
        return valor_total + 300
    
    return valor_total

def validar_opc_num(mensagem, opc_validas):
    while True:
        try:
            valor = int(input(mensagem))

            if valor in opc_validas:
                return valor

            print('\033[31mERRO!\033[0m')

        except ValueError:
            print('\033[31mDigite apenas números!\033[0m')

def validar_opc_alf (mensagem, opc_validas):
    valor = input(mensagem).upper()

    while valor not in opc_validas:
        print('\033[31mERRO!\033[0m')
        valor = input(mensagem).upper()
    return valor

tipo_aluguel = validar_opc_num('''
Qual tipo de aluguel deseja? 
(1) Apartamentos 
(2) Casas
(3) Estudio
                         
> ''',(1, 2, 3))

if tipo_aluguel == 1:
    print('Temos opções de 1 e 2 quartos')
    quant_quarto = validar_opc_num('Quantos quartos deseja? ',(1, 2))

    if quant_quarto == 1:
        valor_total = valor_apartamento

    else:
        valor_total = valor_apartamento + 200
    
    valor_total = estacionamento(valor_total)

    desconto = validar_opc_alf('Tem filhos? (S) / (N) > ', ("S", "N"))
    if desconto == "N":
        valor_total *= 0.95

elif tipo_aluguel == 2:
    print('Temos opções de 1 e 2 quartos')
    quant_quarto = validar_opc_num('Quantos quartos deseja? ',(1, 2))
    
    if quant_quarto == 1:
        valor_total = valor_casa

    else:
        valor_total = valor_casa + 250
    
    valor_total = estacionamento(valor_total)

else:
    valor_total = valor_estudio
    print('No caso do Estudio pode ser adicionado vagas de estacionamento a partir de R$ 250,00 com 2 (duas) vagas, podendo acrescentar mais vagas no valor de R$ 60,00 cada')
    vaga_estacionamento = validar_opc_alf('Deseja incluir vaga de estacionamento? (S) / (N) > ' , ("S", "N"))

    if vaga_estacionamento == "S":
        quant_vagas = int(input('Deseja adicionar quantas vagas? '))

        if quant_vagas == 1 or quant_vagas == 2:
            valor_total += 250

        elif quant_vagas > 2:
            valor_total += 250 + (60 * (quant_vagas - 2))

valor_total += contrato_imob

print(f'Valor a ser pago será de: R$ {valor_total:.2f}')

opc_parcelar = validar_opc_alf('Deseja parcelar? (S) / (N) > ', ("S", "N"))

if opc_parcelar == "S":
    quant_parcelas = validar_opc_num('Podemos parcelar em até 5 vezes. Deseja parcelar em 2, 3, 4 ou 5 vezes? ',(2, 3, 4, 5))
    valor_parcelado = valor_total / quant_parcelas

    with open("orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Parcelas:"])

        for i in range(1, quant_parcelas + 1):
            escritor.writerow([f"Parcela {i}: R$ {valor_parcelado:.2f}"])
