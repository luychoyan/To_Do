import flet as ft


def principal(page: ft.Page):
    page.title = 'Lista de Tarefas'
    page.window.width = 500
    page.window.height = 700
    page.horizontal_alignment = 'center'

    # cria a tarefa
    def cria_tarefa(e):
        return page.add(
            ft.Row([
                ft.Checkbox(label= caixa_texto.value),
                ft.IconButton(icon= ft.Icons.EDIT_OUTLINED),
                ft.IconButton(icon= ft.Icons.DELETE, on_click= mostrar_alerta_confirmar)
            ])
        )
    # mostra o alerta na tela
    def mostrar_alerta_confirmar(e):
        page.open(
            alerta_confirmar
        )
    # fecha o alerta de confirmacao
    def fechar_alerta(e):
        page.close(
            alerta_confirmar
        )
    # se a caixa não estiver vazia, adiciona uma nova tarefa 
    def adiciona_tarefa(e):
        # se a caixa estiver vazia, mostra um alerta na tela
        if caixa_texto.value == '':
            page.open(
                ft.AlertDialog(
                    title= ft.Text('Por favor digite uma tarefa!')
                ) 
            )
        else:
            # Adiciona uma nova tarefa com o titulo digitado na caixa
            cria_tarefa(e)
            caixa_texto.value = '' # limpa a caixa de texto
            caixa_texto.focus() # caixa de texto com foco
            caixa_texto.update()

    caixa_texto = ft.TextField(label= 'O que vamos fazer hoje?')
    alerta_confirmar = ft.AlertDialog(
        modal= True,
        title= ft.Text('Quer mesmo deletar esta tarefa?'),
        actions= [
            ft.ElevatedButton('Confirmar', on_click= fechar_alerta),
            ft.ElevatedButton('Cancelar', on_click= fechar_alerta)
        ]
    )
    botao_add = ft.ElevatedButton('Adicionar Tarefa', on_click= adiciona_tarefa, )
    ft.SafeArea(
        page.add(
            ft.AppBar(
                title= ft.Text('Lista de Tarefas',),
                bgcolor= ft.Colors.CYAN,
                center_title= True # centraliza o titulo da AppBar
            ),
            ft.Column([
                ft.Row([
                    caixa_texto,
                    botao_add,
                ])
            ])
    ))

ft.app(principal)