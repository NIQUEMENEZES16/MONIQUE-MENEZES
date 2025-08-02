# [LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.

num_alunos = int(input("Digite o número de alunos: "))
soma_medias = 0

for i in range(num_alunos):
    print(f"\nAluno {i+1}")
    nome = input("Nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    soma_medias += media

    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"\nNome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

media_geral = soma_medias / num_alunos
print(f"\nMédia geral da turma é: {media_geral:.2f}")
