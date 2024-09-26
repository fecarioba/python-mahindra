import random
import time
import pandas as pd

dados_pilotos = {
    'nome': ['Sergio Camara', 'Lucas di Grassi', 'Norman Nato', 'Sébastien Buemi', 'Sam Bird', 'Stoffel Vandoorne'],
    'idade': [26, 39, 32, 35, 37, 32],
    'equipe': ['ERT', 'Venturi', 'NIO', 'Nissan', 'Jaguar', 'Mercedes'],
    'historico': [0, 0, 0, 0, 0, 0]
}

pilotos_df = pd.DataFrame(dados_pilotos)

def checarNumero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def definir_posicoes_de_largada(pilotos_df):
    posicoes_largada = pilotos_df.sample(frac=1).reset_index(drop=True)
    return posicoes_largada

def simular_corrida(pilotos_df, voltas=10):
    posicoes = pilotos_df.copy()
    for volta in range(1, voltas + 1):
        print(f"\nVolta {volta}")
        for i in range(len(posicoes)):
            if i > 0 and random.random() < 0.3:
                posicoes.iloc[i], posicoes.iloc[i - 1] = posicoes.iloc[i - 1], posicoes.iloc[i]
        print("Posições:", posicoes['nome'].tolist())
        time.sleep(1)
    return posicoes

def calcular_ganho(posicao_largada, aposta, total_pilotos):
    return int(aposta * (total_pilotos / (posicao_largada + 1)))

def corrida_formula_e():
    creditos = 100

    while True:
        print("Início da corrida de Fórmula E")

        posicoes_largada = definir_posicoes_de_largada(pilotos_df)
        print("\nPosições de Largada:")
        for i, piloto in enumerate(posicoes_largada['nome']):
            equipe = posicoes_largada.iloc[i]['equipe']
            print(f"{i + 1}. {piloto} - Equipe: {equipe}")

        escolha = checarNumero("Escolha um piloto para torcer (número): ")
        while not (1 <= escolha <= len(pilotos_df)):
            print('Digite um número válido do piloto')
            escolha = checarNumero("Escolha um piloto para torcer (número): ")

        escolha -= 1
        piloto_escolhido = posicoes_largada.iloc[escolha]['nome']
        print(f"Você escolheu: {piloto_escolhido}")

        print(f"Você tem {creditos} créditos disponíveis.")
        aposta = 0
        if creditos > 0:
            aposta_opcional = input("Você quer apostar? (s/n): ").lower()

            while aposta_opcional not in ['s', 'n']:
                print('Por favor digite "s" ou "n"')
                aposta_opcional = input("Você quer apostar? (s/n): ").lower()

            if aposta_opcional == 's':
                aposta = checarNumero("Digite o valor da aposta: ")

                while aposta <= 0 or aposta > creditos:
                    if aposta <= 0:
                        print('Digite um valor de aposta válido')
                    else:
                        print(f'Você não pode apostar mais do que seus créditos disponíveis ({creditos}).')
                    aposta = checarNumero("Digite o valor da aposta: ")

                print(f"Você apostou {aposta} no {piloto_escolhido}")
        else:
            print("Você não tem créditos suficientes para apostar. A corrida será simulada sem apostas.")

        posicoes_finais = simular_corrida(posicoes_largada)
        print("\nPosições Finais:", posicoes_finais['nome'].tolist())

        vencedor = posicoes_finais.iloc[0]['nome']
        print(f"\nO vencedor da corrida é: {vencedor}")

        if vencedor == piloto_escolhido:
            if aposta > 0:
                ganho = calcular_ganho(escolha, aposta, len(pilotos_df))
                creditos += ganho
                print(f"Parabéns! O piloto que você escolheu ganhou a corrida! Você ganhou {ganho} créditos!")
            else:
                creditos += 50
                print("Parabéns! O piloto que você escolheu ganhou a corrida!")
        else:
            if aposta > 0:
                creditos -= aposta
                print("Que pena! O piloto que você escolheu não ganhou a corrida. Você perdeu sua aposta.")
            else:
                print("Que pena! O piloto que você escolheu não ganhou a corrida.")

        print(f"Você agora tem {creditos} créditos.")

        jogar_novamente = input("Você gostaria de simular a corrida novamente? (sim/nao): ").strip().lower()
        while jogar_novamente not in ['sim', 'nao']:
            jogar_novamente = input('Digite um valor válido (sim ou nao): ')
        if jogar_novamente != 'sim':
            break

corrida_formula_e()
