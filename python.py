import random
import time

pilotos = ["Piloto A", "Piloto B", "Piloto C", "Piloto D"]

def definir_posicoes_de_largada(pilotos):
    posicoes_largada = pilotos[:]
    random.shuffle(posicoes_largada)
    return posicoes_largada

# Função para simular a corrida
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

def corrida_formula_e():
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


    aposta_opcional = input("Você quer apostar? (sim/não): ").strip().lower()
    aposta = 0
    if aposta_opcional == 'sim':
        aposta = input("Digite o valor da aposta: ")
        while not aposta.isnumeric() or int(aposta) <= 0:
            print('Digite um valor de aposta válido')
            aposta = input("Digite o valor da aposta: ")
        aposta = int(aposta)
        print(f"Você apostou {aposta} no {piloto_escolhido}")

    posicoes_finais = simular_corrida(posicoes_largada)
    print("\nPosições Finais:", posicoes_finais)

    vencedor = posicoes_finais[0]
    print(f"\nO vencedor da corrida é: {vencedor}")
    
    if vencedor == piloto_escolhido:
        if aposta > 0:
            ganho = aposta * 2
            print(f"Parabéns! O piloto que você escolheu ganhou a corrida! Você ganhou {ganho}!")
        else:
            print("Parabéns! O piloto que você escolheu ganhou a corrida!")
    else:
        if aposta > 0:
            print("Que pena! O piloto que você escolheu não ganhou a corrida. Você perdeu sua aposta.")
        else:
            print("Que pena! O piloto que você escolheu não ganhou a corrida.")

corrida_formula_e()
