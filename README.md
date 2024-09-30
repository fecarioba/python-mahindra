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

Este projeto consiste em um simulador de corridas da fórmula E. 
Ele simula um grid de largada com os pilotos disponíveis, possibilita torcida e apostas, simula ultrapassagens e quando a simulação se encerra, o programa verifica se o piloto vencedor é o mesmo escolhido pelo usuário, e se o mesmo fez alguma aposta para calcular seu retorno ou prejuízo.
Após todo este processo o programa pergunta se o usuário deseja simular a corrida novamente e participar de toda essa nova aventura denovo.

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
import pandas
```

### 📝 Dicionário para armazenar os dados dos pilotos
``` python
dados_pilotos = {
    'nome': ['Sergio Camara', 'Lucas di Grassi', 'Norman Nato', 'Sébastien Buemi', 'Sam Bird', 'Stoffel Vandoorne'],
    'equipe': ['ERT', 'Venturi', 'NIO', 'Nissan', 'Jaguar', 'Mercedes'],
}
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
def definir_posicoes_de_largada(pilotos_df):
    posicoes_largada = pilotos_df.sample(frac=1).reset_index(drop=True)
    return posicoes_largada
```

### 💻 Função para simular a corrida com base nas posições de largada e um número de voltas
``` python
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
```

### 💻 Função para calcular os ganhos com base na posição de largada e na aposta
``` python
def calcular_ganho(posicao_largada, aposta, total_pilotos):
    return int(aposta * (total_pilotos / (posicao_largada + 1)))
```

### 🏎️ Função para executar o código
``` python
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
```

### 🏎️ Chamada da função que executa o código
``` python
corrida_formula_e()
```
