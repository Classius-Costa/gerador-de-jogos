# Importa o módulo random para gerar números aleatórios
# random.sample() é usado para criar uma lista de valores únicos de um intervalo específico
import random

# Função para gerar números aleatórios
# Parâmetro 'dezenas': número de dezenas a serem sorteadas
# Retorna uma lista com 'dezenas' números únicos entre 1 e 60
def gerar_numeros_aleatorios(dezenas):
    return random.sample(range(1, 61), dezenas)

# Entrada do valor apostado pelo usuário
# Usa a função input() para receber o valor como string e converte para float
valor_apostado = float(input("Informe o valor apostado: R$ "))

# Entrada do valor do jogo (valor de um único cartão de apostas)
# Também utiliza input() seguido de conversão para float
valor_jogo = float(input("Informe o valor do jogo: R$ "))

# Cálculo do troco (diferença entre o valor apostado e o valor usado para os jogos)
troco = valor_apostado - valor_jogo

# Cálculo da quantidade de jogos possíveis com o valor apostado
# Divide o valor apostado pelo valor do jogo e converte o resultado para inteiro
quantidade_jogos = int(valor_apostado / valor_jogo)

# Entrada da quantidade de dezenas a serem escolhidas por cartão
# Converte o valor recebido pelo input() para inteiro
quantidade_dezenas = int(input("Informe a quantidade de dezenas por cartão: "))

# Geração de números aleatórios para cada jogo
# A lista 'numeros_aleatorios' armazena os resultados de cada jogo
numeros_aleatorios = []
for i in range(quantidade_jogos):
    # Chama a função gerar_numeros_aleatorios() para criar os números de cada jogo
    numeros_aleatorios.append(gerar_numeros_aleatorios(quantidade_dezenas))

# Exibe os resultados das entradas e cálculos ao usuário
print("Valor do jogo: R$ {:.2f}".format(valor_jogo))
print("Valor apostado: R$ {:.2f}".format(valor_apostado))
print("Troco: R$ {:.2f}".format(troco))
print("Quantidade de jogos: {}".format(quantidade_jogos))
print("Quantidade de dezenas por cartão: {}".format(quantidade_dezenas))

# Exibe todos os jogos gerados
# Itera sobre a lista 'numeros_aleatorios' para imprimir cada jogo
print("Jogos feitos: ")
for i in range(quantidade_jogos):
    print("Jogo {}: {}".format(i + 1, numeros_aleatorios[i]))
