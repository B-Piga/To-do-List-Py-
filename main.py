import PySimpleGUI as Sg

def criarTarefa():
    Sg.theme('DarkBlue4')
    linha = [
        [Sg.Checkbox(''), Sg.Input('')]
        ]
    layout = [
        [Sg.Frame('To-Do', layout=linha, key='container')],
        [Sg.Button('Nova Tarefa'),Sg.Button('Resetar')]
    ]

    return Sg.Window('To-Do-List', layout=layout, finalize=True)

janela = criarTarefa()

while True:
    event, values = janela.read()
    if event == Sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[Sg.Checkbox(''),Sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criarTarefa()