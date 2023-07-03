import os
import re
import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    # Exibir caixa de diálogo para selecionar o arquivo
    caminho_arquivo = filedialog.askopenfilename()

    # Verificar se o arquivo foi selecionado
    if caminho_arquivo:
        entry_caminho_arquivo.delete(0, tk.END)
        entry_caminho_arquivo.insert(tk.END, caminho_arquivo)
        entry_caminho_arquivo.config(state="readonly")

def substituir_data():
    # Obter os valores inseridos nos campos de entrada
    data_antiga = entry_data_antiga.get()
    data_nova = entry_data_nova.get()
    caminho_arquivo = entry_caminho_arquivo.get()

    # Abra o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as arquivo:
        # Leia o conteúdo do arquivo
        conteudo = arquivo.read()

    # Substitua a data antiga pela nova usando expressões regulares
    conteudo_modificado = re.sub(data_antiga, data_nova, conteudo)

    # Abra o arquivo em modo de escrita
    with open(caminho_arquivo, 'w') as arquivo:
        # Escreva o conteúdo modificado de volta no arquivo
        arquivo.write(conteudo_modificado)

    print('A substituição da data foi realizada com sucesso!')

# Cria uma janela
janela = tk.Tk()

# Cria os campos de entrada
label_caminho_arquivo = tk.Label(janela, text="Caminho do arquivo:")
label_caminho_arquivo.pack()
entry_caminho_arquivo = tk.Entry(janela, state="normal")
entry_caminho_arquivo.pack(side=tk.LEFT, expand=True, fill=tk.X)
button_selecionar_arquivo = tk.Button(janela, text="Selecionar arquivo", command=selecionar_arquivo)
button_selecionar_arquivo.pack(side=tk.LEFT)

label_data_antiga = tk.Label(janela, text="Data antiga:")
label_data_antiga.pack()
entry_data_antiga = tk.Entry(janela)
entry_data_antiga.pack()

label_data_nova = tk.Label(janela, text="Data nova:")
label_data_nova.pack()
entry_data_nova = tk.Entry(janela)
entry_data_nova.pack()

# Cria um botão para substituir a data
botao_substituir = tk.Button(janela, text="Substituir", command=substituir_data)
botao_substituir.pack()

# Executa o loop principal da aplicação
janela.mainloop()
