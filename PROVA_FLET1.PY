# [PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.


import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"

    # Lista para mostrar as tarefas na coluna
    tarefas = ft.Column()

    # Campo de entrada de texto
    entrada_tarefa = ft.TextField(label="Digite o nome da tarefa", width=400, color="green")

    # Função para adicionar tarefa
    def adicionar_tarefa(e):
        tarefa = entrada_tarefa.value.strip()
        if tarefa:
            # Cria um texto para a tarefa e adiciona na lista
            tarefas.controls.append(ft.Text(tarefa))
            entrada_tarefa.value = ""  # limpa o campo
            page.update()

    # Botão para adicionar a tarefa
    botao_adicionar = ft.ElevatedButton(text="Adicionar tarefa á lista", color="green", on_click=adicionar_tarefa)

    # Layout da página
    page.add(
        entrada_tarefa,
        botao_adicionar,
        ft.Text("Tarefas:", weight=ft.FontWeight.BOLD, size=30, color="green"),
        tarefas
    )

ft.app(target=main)
