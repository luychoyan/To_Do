import flet as ft


def principal(page: ft.Page):
    page.title = 'Lista de Tarefas' # titulo do app
    page.window.width = 500 # O app abre com essa largura
    page.window.min_width = 500 # Largura minima do app (nao diminui a largura mais do que esse valor)
    page.window.max_width = 700 # Largura maxima do app (nao aumenta a largura mais do que esse valor)
    
    page.window.height = 700 # Abre o app com essa altura
    page.window.max_height = 900  # Altura maxima do app (nao aumenta a altura mais do que esse valor)
    page.window.min_height = 700 # Altura minima do app (nao diminui a altura mais do que esse valor)
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

    botao_add = ft.ElevatedButton('Adicionar Tarefa', on_click= adiciona_tarefa, color= ft.Colors.CYAN, bgcolor= ft.Colors.WHITE,)
    caixa_texto = ft.TextField(label= 'O que vamos fazer hoje?')
    alerta_confirmar = ft.AlertDialog(
        modal= True,
        title= ft.Text('Quer mesmo deletar esta tarefa?'),
        actions= [
            ft.ElevatedButton('Confirmar', on_click= fechar_alerta),
            ft.ElevatedButton('Cancelar', on_click= fechar_alerta)
        ]
    )
    # renderiza na tela
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
                ]),
            ])
        )
    )

ft.app(principal)