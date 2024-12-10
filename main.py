import flet as ft

class tarefa(ft.Row):
    def __init__(self, nome_tarefa, deletar_tarefa):
        super().__init__()
        self.nome_tarefa = nome_tarefa
        self.deletar_tarefa = deletar_tarefa
        self.editar_nome = ft.TextField(expand= 1)
        self.tarefa_display = ft.Checkbox(value= False, label= self.nome_tarefa)
        
        self.ver_display = ft.Row(
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            controls= [
                self.tarefa_display,
                ft.Row(
                    spacing= 0,
                    controls= [
                        ft.ElevatedButton('Editar', on_click= self.clique_editar),
                    ]
                )
            ]
        )

def principal(page: ft.Page):
    page.title = 'Lista de Tarefas'
    page.window_width = 400
    page.window_height = 600
    page.horizontal_alignment = 'center'

    def cria_tarefa(e):
        return  page.add(
                    ft.Row([
                        ft.Checkbox(label= caixa_texto.value),
                        ft.ElevatedButton('Editar'),
                        ft.ElevatedButton('Excluir',)
                    ])
                )
           
    def deletar_tarefa(e):
        return

    def editar_tarefa(e):
        return

    def adiciona_tarefa(e):
        if caixa_texto.value == '':
            page.open(
                ft.AlertDialog(
                    title= ft.Text('Por favor digite uma tarefa!')
                ) 
            )
        else:
            cria_tarefa(e)
            caixa_texto.value = ''
            caixa_texto.focus()
            caixa_texto.update()

    caixa_texto = ft.TextField(label= 'O que vamos fazer hoje?')
    botao_cria_tarefa = ft.ElevatedButton('Criar tarefa', on_click= cria_tarefa)
    botao_add = ft.ElevatedButton('Adicionar Tarefa', on_click= adiciona_tarefa, )
    ft.SafeArea(
        page.add(
            ft.AppBar(
                title= ft.Text('Lista de Tarefas', text_align= ft.alignment.center),
                bgcolor= ft.colors.RED
            ),
        caixa_texto,
        botao_add,
    ))

ft.app(principal)