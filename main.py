from funcs import *
# estou importando o módulo tkinter e o apelidando como "tk" para melhor conveniência
import tkinter as tk


# cria a janela de interface ao instanciar a classe "Tk" do módulo "tk"
janela = tk.Tk()


# define o título da aplicação como "calculadora de IMC"
janela.title("calculadora de IMC")


# cria uma label que aparecerá na nossa aplicação com o texto "Calculadora de IMC"
label = tk.Label(janela, text="<<< Calculadora de IMC >>>")

# empacota a label na aplicação
label.pack()


cria_e_define_menus_e_submenus(janela)


# cria uma label2 com o texto "informe o seu nome"
label2 = tk.Label(janela, text="informe o seu nome: ")

# empacota a label2 na aplicação
label2.pack()

# cria uma entrada de dados que aparecerá na nossa janela para o usuário informar o nome
entrada_para_nome = tk.Entry(janela)

# empacota a entrada de dados para nome na aplicação
entrada_para_nome.pack()

# cria uma label para peso
label3 = tk.Label(janela, text="informe o seu peso: Kg")

# empacota a label 3 na aplicação
label3.pack()

# cria uma entrada de dados para peso
entrada_para_peso = tk.Entry(janela)


# empacota a entrada de dados para peso na aplicação
entrada_para_peso.pack()

# cri uma label que diz "informe a sua altura: "
label4 = tk.Label(janela, text="informe a sua altura: [M]")

# empacota a label4 na aplicação
label4.pack()

# cria entrada de dados para altura
entrada_para_altura = tk.Entry(janela)

# empacota a entrada de dados de altura na aplicação
entrada_para_altura.pack()


# cria uma área de texto onde será exibida a mensagem ao usuário sobre o seu IMC
area_de_texto = tk.Text(janela, height=5, width=30, state=tk.DISABLED)

# empacota a área de texto na aplicação
area_de_texto.pack()


# cria um botão de calcular imc e o associa a janela
botao_calcular_imc = tk.Button(janela, text="calcular", command=lambda: calcular_imc(entrada_para_nome, entrada_para_peso, entrada_para_altura, area_de_texto))

# empacota esse botão a aplicação
botao_calcular_imc.pack()

botao_imc = tk.Button(janela, text="o que é IMC?", command=mostrar_descricao_imc)

botao_imc.pack(pady=10)

# executa a aplicação
janela.mainloop()