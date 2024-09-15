import random
import time

# Dados dos pilotos
pilotos = [
    {'nome': 'Sergio Camara', 'idade': 26, 'equipe': 'ERT', 'historico': 0},
    {'nome': 'Lucas di Grassi', 'idade': 39, 'equipe': 'Venturi', 'historico': 0},
    {'nome': 'Norman Nato', 'idade': 32, 'equipe': 'NIO', 'historico': 0},
    {'nome': 'Sébastien Buemi', 'idade': 35, 'equipe': 'Nissan', 'historico': 0},
    {'nome': 'Sam Bird', 'idade': 37, 'equipe': 'Jaguar', 'historico': 0},
    {'nome': 'Stoffel Vandoorne', 'idade': 32, 'equipe': 'Mercedes', 'historico': 0}
]

creditos = 100  # Créditos iniciais

def checarNumero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def definir_posicoes_de_largada(pilotos):
    posicoes_largada = pilotos[:]
    random.shuffle(posicoes_largada)
    return posicoes_largada

def simular_corrida(pilotos, voltas=10):
    posicoes = pilotos[:]
    for volta in range(1, voltas + 1):
        print(f"\nVolta {volta}")
        for i in range(len(posicoes)):
            if i > 0 and random.random() < 0.3:
                posicoes[i], posicoes[i - 1] = posicoes[i - 1], posicoes[i]
        print("Posições:", [p['nome'] for p in posicoes])
        time.sleep(1)
    return posicoes

def calcular_ganho(posicao_largada, aposta):
    return int(aposta * (len(pilotos) / (posicao_largada + 1)))

def corrida_formula_e():
    global creditos

    while True:
        print("Início da corrida de Fórmula E")

        posicoes_largada = definir_posicoes_de_largada(pilotos)
        print("\nPosições de Largada:")
        for i, piloto in enumerate(posicoes_largada):
            print(f"{i + 1}. {piloto['nome']}")

        escolha = checarNumero("Escolha um piloto para torcer (número): ")
        while not (1 <= escolha <= len(pilotos)):
            print('Digite um número válido do piloto')
            escolha = checarNumero("Escolha um piloto para torcer (número): ")

        escolha -= 1
        piloto_escolhido = posicoes_largada[escolha]['nome']
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
        print("\nPosições Finais:", [p['nome'] for p in posicoes_finais])

        vencedor = posicoes_finais[0]['nome']
        print(f"\nO vencedor da corrida é: {vencedor}")

        if vencedor == piloto_escolhido:
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

        jogar_novamente = input("Você gostaria de simular a corrida novamente? (sim/nao): ").strip().lower()
        while jogar_novamente not in ['sim', 'nao']:
            jogar_novamente = input('Digite um valor válido (sim ou nao)')
        if jogar_novamente != 'sim':
            break

corrida_formula_e()
