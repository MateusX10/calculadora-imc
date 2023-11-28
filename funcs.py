import tkinter as tk
from tkinter import messagebox



def mostra_mensagem_sobre():

    

    messagebox.showinfo("Sobre", "Calculadora de IMC\n Versão 1.0 \nAutor: Mateus Henrique de Souza Medeiros")


def mostrar_autor():

    messagebox.showinfo("Autor", "Esta aplicação foi desenvolvida por Mateus Henrique de Souza Medeiros")


def abrir_github():

    import webbrowser


    url_my_github_profile = "https://github.com/MateusX10"

    webbrowser.open_new(url_my_github_profile)


def mostrar_descricao_imc():
    # Descrição sobre o IMC
    descricao_imc = ('''O Índice de Massa Corporal (IMC) é uma medida que te permite determinar se você está com o peso ideal ou não.\nAbaixo, você pode conferir a classificação do IMC:

- IMC abaixo de 18,5: Abaixo do peso\n
- IMC entre 18,5 e 24,9: Peso saudável\n
- IMC entre 25 e 29,9: Sobrepeso\n
- IMC 30 ou superior: Obesidade\n\n\n


* Se quiser saber mais sobre o IMC, você pode conferir o nosso Guia do IMC em: ajuda -> Guia do IMC.
    ''')
    messagebox.showinfo("O que é IMC?", descricao_imc)



def abrir_guia_do_imc():

    import webbrowser
    import os



    caminho_do_arquivo_html = os.path.join(os.path.dirname(__file__), 'guia_imc.html')

    caminho_do_arquivo_css = os.path.join(os.path.dirname(__file__), 'style.css')

    webbrowser.open_new(caminho_do_arquivo_html)



def cria_e_define_menus_e_submenus(janela):
    import webbrowser


    # cria uma barra de menu e a associa a janela da aplicação
    barra_menu = tk.Menu(janela)

    # configura a barra da nossa janela como sendo a barra de menu criada acima
    janela.config(menu=barra_menu)

    menu_arquivo = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

    menu_arquivo.add_command(label="Sair", command=janela.quit)

    menu_ajuda = tk.Menu(barra_menu, tearoff=0)

    barra_menu.add_cascade(label="ajuda", menu=menu_ajuda)

    menu_ajuda.add_command(label="Sobre", command=mostra_mensagem_sobre)

    menu_ajuda.add_command(label="Autor", command=mostrar_autor)


    menu_ajuda.add_command(label="Visitar github do autor", command=abrir_github)

    menu_ajuda.add_command(label="Guia do IMC", command=abrir_guia_do_imc)



def calcular_imc(nome, peso, altura, area_de_texto):
    '''
    '''

    

    # obtém o nome do usuário
    nome_usuario = nome.get()

    # obtém o peso do usuário
    peso_usuario = peso.get()

    peso_usuario = float(peso_usuario)

    # obtém a altura do usuário
    altura_usuario = altura.get()

    altura_usuario = float(altura_usuario)


    # calcula o imc
    imc = peso_usuario / (altura_usuario ** 2)

    mensagem_situacao_de_saude = define_a_situacao_de_saude_do_usuario(imc)

    # define a mensagem a ser exibida ao usuário
    mensagem_ao_usuario = f"{nome_usuario}, seu IMC é de {imc:.1f} \nVocê está com {mensagem_situacao_de_saude}."

    # define a área de texto para a possibilidade de gravar dados nela
    area_de_texto.config(state=tk.NORMAL)

    # limpa a área de texto
    area_de_texto.delete("1.0", tk.END)

    # insere a mensagem na área de texto para que possa ser exibida ao usuário
    area_de_texto.insert(tk.END, mensagem_ao_usuario)

    # define a área de texto como de somente leitura
    area_de_texto.config(state=tk.DISABLED)



def define_a_situacao_de_saude_do_usuario(imc):
    '''-> Define a situação de saúde do usuário de acordo com o valor do seu IMC    
        
        Parâmetros:

            imc(float): o valor do imc do usuário
            return: retorna uma mensagem informando a situação de saúde do usuário
    '''

    # usuário está abaixo do peso
    if imc < 18.5:

        mensagem = "abaixo do peso"

    # usuário está com peso normal
    elif imc <= 24.9:
        mensagem = "peso normal"

    # usuário está com sobrepeso
    elif imc <= 29.9:
        mensagem = "sobrepeso"

    # usuário está com obesidade grau I
    elif imc <= 34.9:

        mensagem = "obesidade grau I"


    # usuário está com obesidade grau II
    elif imc <= 39.9:

        mensagem = "obesidade grau II"


    # usuário está com obesidade grau III
    elif imc >= 40:

        mensagem = "obesidad grau III"


    return mensagem



 