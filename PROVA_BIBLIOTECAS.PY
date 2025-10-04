import random

print("ATIVIDADE: Simulador de lançamento de dados utilizando o módulo random e mostrando o resultado da soma dos valores obtidos")
print("Valores dos dados obtidos nesta rodada:")

def lancar_dados():
    dado1 = random.randint (1, 6)
    dado2 = random.randint (1, 6)
    soma = dado1 + dado2
    print(f'Dado 01: {dado1}, Dado 02: {dado2}')
    return soma

resultado = lancar_dados()
print(f'O resultado final da soma do lançamentos dos dados desta rodada foi: {resultado}.')
