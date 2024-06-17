import random
import time
#Bibliotecas utilizadas para fazer o sorteio das posições iniciais, chances de ultrapassagem
#E para ter um peaqueno delay entre as voltas

pilotos = ["Piloto A", "Piloto B", "Piloto C", "Piloto D", 'Piloto E', 'Piloto F']
creditos = 100  # Créditos iniciais


def checarNumero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num) 
    return num

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
        print("Posições:", posicoes)
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
            print(f"{i + 1}. {piloto}")
        
        escolha = input("Escolha um piloto para torcer (número): ")
        while not escolha.isnumeric() or not (1 <= int(escolha) <= len(pilotos)):
            print('Digite um número válido do piloto')
            escolha = input("Escolha um piloto para torcer (número): ")
        
        escolha = int(escolha) - 1
        piloto_escolhido = posicoes_largada[escolha]
        print(f"Você escolheu: {piloto_escolhido}")

        print(f"Você tem {creditos} créditos disponíveis.")  # Mostra ao usuário quantos créditos ele tem disponíveis
        aposta = 0
        if creditos > 0:
            aposta_opcional = input("Você quer apostar? (s/n): ").lower()
            while aposta_opcional != 's' and aposta_opcional != 'n':
                print('Por favor digite "s" ou "n"')
                aposta_opcional = input("Você quer apostar? (s/n): ").lower()
            if aposta_opcional == 's':
                aposta = input("Digite o valor da aposta: ")
                while not aposta.isnumeric() or int(aposta) <= 0 or int(aposta) > creditos:
                    if not aposta.isnumeric() or int(aposta) <= 0:
                        print('Digite um valor de aposta válido')
                    else:
                        print(f'Você não pode apostar mais do que seus créditos disponíveis ({creditos}).')
                    aposta = input("Digite o valor da aposta: ")
                aposta = int(aposta)
                print(f"Você apostou {aposta} no {piloto_escolhido}")
        else:
            print("Você não tem créditos suficientes para apostar. A corrida será simulada sem apostas.")

        posicoes_finais = simular_corrida(posicoes_largada)
        print("\nPosições Finais:", posicoes_finais)

        vencedor = posicoes_finais[0]
        print(f"\nO vencedor da corrida é: {vencedor}")
        
        if vencedor == piloto_escolhido: 
            if aposta > 0:
                ganho = calcular_ganho(escolha, aposta)
                creditos += ganho  # Adiciona o ganho aos créditos do usuário
                print(f"Parabéns! O piloto que você escolheu ganhou a corrida! Você ganhou {ganho} créditos!")
            else:
                creditos += 50  # Adiciona 50 créditos se o piloto escolhido vencer sem aposta
                print("Parabéns! O piloto que você escolheu ganhou a corrida!")
        else:
            if aposta > 0:
                creditos -= aposta  # Subtrai o valor da aposta dos créditos do usuário se ele perder
                print("Que pena! O piloto que você escolheu não ganhou a corrida. Você perdeu sua aposta.")
            else:
                print("Que pena! O piloto que você escolheu não ganhou a corrida.")
        
        print(f"Você agora tem {creditos} créditos.")  # Mostra ao usuário a quantidade de créditos restantes

        jogar_novamente = input("Você gostaria de simular a corrida novamente? (sim/não): ").strip().lower()
        if jogar_novamente != 'sim':
            break
    
corrida_formula_e()
