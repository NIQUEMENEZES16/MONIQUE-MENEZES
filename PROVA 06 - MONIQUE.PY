# [LPIA-A06]  Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

usuario_correto = "admin"
senha_correta = "1234"

maximo_tentativas = 3

for tentativa in range(maximo_tentativas):

    usuario = input("\nDigite o nome de usuário: ")
    senha = input("Digite a senha correta: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo, acesso concedido!")
        break
    else:
        restante = maximo_tentativas - (tentativa + 1)
        if restante > 0:
            print(f"Credenciais incorretas. Você tem {restante} tentativa(s) restante(s).\n")
        else:
            print("\nTodas as tentativas foram usadas.")

else:
    for _ in range(3):
        print("Acesso bloqueado.")
