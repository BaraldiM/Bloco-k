import os
import re
import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    # Exibir caixa de diálogo para selecionar o arquivo
    caminho_arquivo = filedialog.askopenfilename()
    print(caminho_arquivo)
    entrada_caminho.delete(0, tk.END)
    entrada_caminho.insert(tk.END, caminho_arquivo)

def substituir_data():
    # Obter os valores inseridos nos campos de entrada
    data_antiga = entrada_data_antiga.get()
    data_nova = entrada_data_nova.get()
    caminho_arquivo = entrada_caminho.get()

    # Abra o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as arquivo:
        # Leia o conteúdo do arquivo
        conteudo = arquivo.read()

    # Substitua a data antiga pela nova usando expressões regulares,
    # apenas para linhas que começam com "|K200|"
    conteudo_modificado = ""
    for linha in conteudo.split('\n'):
        if linha.startswith("|K200|"):
            linha_modificada = re.sub(data_antiga, data_nova, linha)
            conteudo_modificado += linha_modificada + '\n'
        else:
            conteudo_modificado += linha + '\n'

    # Abra o arquivo em modo de escrita
    with open(caminho_arquivo, 'w') as arquivo:
        # Escreva o conteúdo modificado de volta no arquivo
        arquivo.write(conteudo_modificado)

    print('A substituição da data foi realizada com sucesso!')

# Cria uma janela
janela = tk.Tk()
janela.title("Trocar datas bloco K")
janela.geometry("400x200")

entrada_caminho = tk.Entry(janela, state="normal")
entrada_caminho.pack()
button_selecionar_arquivo = tk.Button(janela, text="Selecionar arquivo", command=selecionar_arquivo)
button_selecionar_arquivo.pack()

label_data_antiga = tk.Label(janela, text="Data antiga:")
label_data_antiga.pack()
entrada_data_antiga = tk.Entry(janela)
entrada_data_antiga.pack()

label_data_nova = tk.Label(janela, text="Data nova:")
label_data_nova.pack()
entrada_data_nova = tk.Entry(janela)
entrada_data_nova.pack()

# Cria um botão para substituir a data
botao_substituir = tk.Button(janela, text="Substituir", command=substituir_data)
botao_substituir.pack()

# Executa o loop principal da aplicação
janela.mainloop()
