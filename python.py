# Bibliotecas utilizadas para o melhor funcionamento do código
import random
# Biblioteca utilizada para gerar os números aleátorios e  chances de ultrapassagem
import time
# Biblioteca que possibilita adicionar um pequeno delay entre as voltas da simulação


pilotos = ["Sergio Camara", "Lucas di Grassi", "Norman Nato", "Sébastien Buemi", 'Sam Bird', 'Stoffel Vandoorne']
# Pilotos atuais da fórmula E que podem ser escolhidos para realizar a simulação 
creditos = 100  # Créditos iniciais

def checarNumero(msg):
    # Função para garantir que a entrada seja um número
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def definir_posicoes_de_largada(pilotos):
    # Função para embaralhar as posições de largada dos pilotos
    posicoes_largada = pilotos[:]
    random.shuffle(posicoes_largada)
    return posicoes_largada

def simular_corrida(pilotos, voltas=10):
    # Função para simular a corrida com base nas posições de largada e um número de voltas
    posicoes = pilotos[:]
    for volta in range(1, voltas + 1):
        print(f"\nVolta {volta}")
        for i in range(len(posicoes)):
            if i > 0 and random.random() < 0.3:
                posicoes[i], posicoes[i - 1] = posicoes[i - 1], posicoes[i]
        print("Posições:", posicoes)
        time.sleep(1)
    return posicoes

def calcular_ganho(posicao_largada, aposta):
    # Função para calcular os ganhos com base na posição de largada e na aposta
    return int(aposta * (len(pilotos) / (posicao_largada + 1)))

def corrida_formula_e(): 
    # Função que inicia a simulação da corrida
    global creditos

    while True:
        # Este loop existe para que no final o usuário possa escolher simular de novo
        print("Início da corrida de Fórmula E")

        posicoes_largada = definir_posicoes_de_largada(pilotos)
        print("\nPosições de Largada:")
        for i, piloto in enumerate(posicoes_largada):
            # For que enumera as posições dos pilotos
            print(f"{i + 1}. {piloto}")

        escolha = checarNumero("Escolha um piloto para torcer (número): ")
        while not (1 <= escolha <= len(pilotos)):
            # While que garante que o usuário escolha um corredor válido
            print('Digite um número válido do piloto')
            escolha = checarNumero("Escolha um piloto para torcer (número): ")

        escolha -= 1
        piloto_escolhido = posicoes_largada[escolha]
        print(f"Você escolheu: {piloto_escolhido}")

        print(f"Você tem {creditos} créditos disponíveis.")
        aposta = 0
        if creditos > 0:
            # Verifica se o usuário possui créditos para poder apostar
            aposta_opcional = input("Você quer apostar? (s/n): ").lower()

            while aposta_opcional != 's' and aposta_opcional != 'n':
                # Verifica se o usuário da uma resposta de sim ou não válida
                print('Por favor digite "s" ou "n"')
                aposta_opcional = input("Você quer apostar? (s/n): ").lower()

            if aposta_opcional == 's':
                # Se a aposta for sim o programa pede o valor
                aposta = checarNumero("Digite o valor da aposta: ")

                while aposta <= 0 or aposta > creditos:
                    # Verifica se a aposta tem um valor válido
                    if aposta <= 0:
                        print('Digite um valor de aposta válido')
                    else:
                        print(f'Você não pode apostar mais do que seus créditos disponíveis ({creditos}).')
                    aposta = checarNumero("Digite o valor da aposta: ")

                print(f"Você apostou {aposta} no {piloto_escolhido}")
        else:
            print("Você não tem créditos suficientes para apostar. A corrida será simulada sem apostas.")

        posicoes_finais = simular_corrida(posicoes_largada)
        print("\nPosições Finais:", posicoes_finais)

        vencedor = posicoes_finais[0]
        print(f"\nO vencedor da corrida é: {vencedor}")

        if vencedor == piloto_escolhido:
            # Verifica se o piloto escolhido pelo usuário é o mesmo que ganhou a corrida
            if aposta > 0:
                # Se o usuário apostou e ganhou, o programa calcula o valor de retorno
                ganho = calcular_ganho(escolha, aposta)
                creditos += ganho
                print(f"Parabéns! O piloto que você escolheu ganhou a corrida! Você ganhou {ganho} créditos!")
            else:
                #Se ele não apostou, ele ganha 50 créditos para apostar futuramente
                creditos += 50
                print("Parabéns! O piloto que você escolheu ganhou a corrida!")
        else:
            if aposta > 0:
                # Se o usuário apostou e o corredor não ganhou, ele perde o valor de aposta
                creditos -= aposta
                print("Que pena! O piloto que você escolheu não ganhou a corrida. Você perdeu sua aposta.")
            else:
                print("Que pena! O piloto que você escolheu não ganhou a corrida.")

        print(f"Você agora tem {creditos} créditos.")

        jogar_novamente = input("Você gostaria de simular a corrida novamente? (sim/nao): ").strip().lower()
        while jogar_novamente != 'sim' and jogar_novamente != 'nao':
            jogar_novamente = input('Digite um valor válido (sim ou nao)')
        if jogar_novamente != 'sim':
            # Se o input de jogar novamente for diferente de sim, o loop da simulação quebra e é encerrado
            break

corrida_formula_e()
