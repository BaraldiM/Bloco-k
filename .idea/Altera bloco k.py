import PySimpleGUI as sg
import re

def selecionar_arquivo():
    # Exibir caixa de diálogo para selecionar o arquivo
    caminho_arquivo = sg.popup_get_file("Selecione um arquivo")
    print(caminho_arquivo)
    janela['entrada_caminho'].update(caminho_arquivo)

def substituir_data():
    # Obter os valores inseridos nos campos de entrada
    data_nova = janela['entrada_data_nova'].get()
    caminho_arquivo = janela['entrada_caminho'].get()

    # Abra o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as arquivo:
        # Leia o conteúdo do arquivo
        conteudo = arquivo.read()

    # Substitua a data antiga pela nova usando expressões regulares,
    # apenas para linhas que começam com "|K200|"
    conteudo_modificado = ""

    for linha in conteudo.split('\n'):
        if linha.startswith("|K200|"):
            linha_modificada = re.sub(r'\d{8}', data_nova, linha)
            conteudo_modificado += linha_modificada + '\n'
        else:
            conteudo_modificado += linha + '\n'

    # Abra o arquivo em modo de escrita
    with open(caminho_arquivo, 'w') as arquivo:
        # Escreva o conteúdo modificado de volta no arquivo
        arquivo.write(conteudo_modificado)

    print('A substituição da data foi realizada com sucesso!')

# Definir o layout da janela
layout = [
    [sg.Text("Caminho do arquivo: "), sg.Input(key='entrada_caminho'), sg.FileBrowse(button_text='Selecionar arquivo', key='botao_selecionar_arquivo')],
    #[sg.Text("Data antiga: "), sg.Input(key='entrada_data_antiga')],
    [sg.Text("Data nova: "), sg.Input(key='entrada_data_nova')],
    [sg.Button("Substituir", key='botao_substituir')]
]

# Criar a janela
janela = sg.Window("Trocar datas bloco K", layout)

# Loop principal da janela
while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'botao_selecionar_arquivo':
        selecionar_arquivo()
    elif event == 'botao_substituir':
        substituir_data()

janela.close()
