import random
import time
import pandas as pd

dados_pilotos = {
    'nome': ['Sergio Camara', 'Lucas di Grassi', 'Norman Nato', 'Sébastien Buemi', 'Sam Bird', 'Stoffel Vandoorne'],
    'equipe': ['ERT', 'Venturi', 'NIO', 'Nissan', 'Jaguar', 'Mercedes'],
    'idade': [26, 37, 30, 35, 36, 31],
    'historico': [0, 2, 1, 3, 4, 1] 
}


df_pilotos = pd.DataFrame(dados_pilotos)

creditos = 100

def checarNumero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def definir_posicoes_de_largada(df):
    posicoes_largada = df.sample(frac=1).reset_index(drop=True)
    return posicoes_largada

def simular_corrida(df, voltas=10):
    posicoes = df.copy()
    for volta in range(1, voltas + 1):
        print(f"\nVolta {volta}")
        for i in range(len(posicoes)):
            if i > 0 and random.random() < 0.3:
                posicoes.iloc[i], posicoes.iloc[i - 1] = posicoes.iloc[i - 1], posicoes.iloc[i]
        print("Posições:", posicoes['nome'].tolist())
        time.sleep(1)
    return posicoes

def calcular_ganho(posicao_largada, aposta):
    return int(aposta * (len(df_pilotos) / (posicao_largada + 1)))

def corrida_formula_e(creditos): 
    while True:
        print("Início da corrida de Fórmula E")

        posicoes_largada = definir_posicoes_de_largada(df_pilotos)
        print("\nPosições de Largada:")
        for i, piloto in enumerate(posicoes_largada.itertuples(index=False)):
            print(f"{i + 1}. {piloto.nome} - Equipe: {piloto.equipe}")

        escolha = checarNumero("Escolha um piloto para torcer (número): ")
        while not (1 <= escolha <= len(posicoes_largada)):
            print('Digite um número válido do piloto')
            escolha = checarNumero("Escolha um piloto para torcer (número): ")

        escolha -= 1
        piloto_escolhido = posicoes_largada.iloc[escolha]
        print(f"Você escolheu: {piloto_escolhido.nome}")

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

                print(f"Você apostou {aposta} no {piloto_escolhido.nome}")
        else:
            print("Você não tem créditos suficientes para apostar. A corrida será simulada sem apostas.")

        posicoes_finais = simular_corrida(posicoes_largada)
        print("\nPosições Finais:", posicoes_finais['nome'].tolist())

        vencedor = posicoes_finais.iloc[0]
        print(f"\nO vencedor da corrida é: {vencedor.nome}")

        # Comparar diretamente as informações do piloto
        if vencedor.nome:
            if aposta > 0:
                ganho = calcular_ganho(escolha, aposta)
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

        print(f"\nDados do vencedor:")
        for key, value in vencedor.items():
            print(f"{key.capitalize()}: {value}")

        jogar_novamente = input("Você gostaria de simular a corrida novamente? (sim/nao): ").strip().lower()
        while jogar_novamente not in ['sim', 'nao']:
            jogar_novamente = input('Digite um valor válido (sim ou nao): ')
        if jogar_novamente != 'sim':
            break

# Iniciar a corrida com os créditos iniciais
corrida_formula_e(creditos)
