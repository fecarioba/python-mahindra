# 🏎️ CHALLENGE Mahindra

## 🐍 Computational Thinking with Python

Entrega da matéria Computational Thinking with Python para a primeira Sprint da CHALLENGE.

## 👥 Integrantes

RM: 556785 // Carlos Eduardo dos Santos Ribeiro Filho <br>
RM: 555530 // Djalma Moreira de Andrade Filho <br>
RM: 558447 // Felipe Paes de Barros Muller Carioba <br>
RM: 556506 // Nicolas Caciolato Reis <br>
RM: 554736 // Rafael Federici de Oliveira <br>

## 📕 Sobre o Projeto

### ✨ Visão geral do projeto

Este projeto refere-se ao site desenvolvido com o objetivo de popularizar e mostrar, de melhor forma, o que é a Fórmula-E no Brasil.
A percepção de que a Fórmula-E é apenas uma divisão secundária da Fórmula 1 deve deixar de existir e, é com este pensamento, que desenvolvemos nosso site para uma percepção mais agradável do público em relação ao esporte de automobilismo elétrico fórmula.
Focamos em não desvincular totalmente a fórmula E dos veículos à combustão, mas sim, mostrar as semelhanças e comparações sutis entre ambos. (Inclusive, tal ato pode ser visto na propaganda do EP de Tokyo de 2024, que chamaram Sung Kang, ator do Han, de Velozes e Furiosos, para gravar um comercial com diversos veículos à combustão personalizados e customizados. Tal propaganda possuía o intuito de promover a Fórmula E com sua estética e vincular a Fórmula E com corridas de rua).
Utilizaremos de um site intuitivo, customizável e imersivo para um melhor agrado do usuário. Com isto, traremos comparações com a Fórmula 1 sobre estatísticas, tempo de volta, velocidade, entre outros.
Decidimos que, focar em estética, vínculo com corridas em cenários de rua, tecnologia e acessibilidade, seria o ideal para a popularização da Fórmula E no Brasil, visto que, o brasileiro se interessa por esses quatro pontos.

### 🐍 Visão geral em Computational Thinking with Python



## 🔨 Ferramentas

- [Visual Studio Code](https://code.visualstudio.com/docs)
- [Python](https://www.python.org/doc/)

## 🖥️ Requisitos e Componentes

### 🔧 Requisitos

- Instalar uma IDE ou Editor de Código ([PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/?section=windows) ou [Visual Studio Code](https://code.visualstudio.com/Download)) em seu computador.
- Instalar [Python](https://www.python.org/downloads/) em seu computador.
- Abrir estre projeto no aplicativo escolhido.

## 📒 Instruções de Uso

- Abrir este [projeto]() em uma IDE ou Editor de Código.
- Compilar e 'rodar' o código.
- Seguir as intruções qua aparecerão no console do programa.

## 🧠 Explicando o Código

### 📚 Importando bibliotecas
``` python
import random
import time
```

### 📝 Variaveis para pilotos e creditos
``` python
pilotos = ["Sergio Camara", "Lucas di Grassi", "Norman Nato", "Sébastien Buemi", 'Sam Bird', 'Stoffel Vandoorne']
creditos = 100
```

### 💻 Função para garantir que a entrada seja um número
``` python
def checarNumero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)
```

### 💻 Função para embaralhar as posições de largada dos pilotos
``` python
def definir_posicoes_de_largada(pilotos):
    posicoes_largada = pilotos[:]
    random.shuffle(posicoes_largada)
    return posicoes_largada
```

### 💻 Função para simular a corrida com base nas posições de largada e um número de voltas
``` python
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
```

### 💻 Função para calcular os ganhos com base na posição de largada e na aposta
``` python
def calcular_ganho(posicao_largada, aposta):
    return int(aposta * (len(pilotos) / (posicao_largada + 1)))
```

### 🏎️ Função para executar o código
``` python
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
```

### 🏎️ Chamada da função que executa o código
``` python
corrida_formula_e()
```