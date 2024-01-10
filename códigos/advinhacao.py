import random
from tkinter import *

def jogo_adivinhacao():

    jogador = Entrada.get()
    jogador = int(jogador)

    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    aleatorio = random.randint(0, len(lista) - 1)

    if jogador == aleatorio:
        resultado = f"Você acertou! {jogador} é igual a {aleatorio}"
    else:
        resultado = f"Continue tentando, {jogador} é diferente de {aleatorio}"

    texto_iniciar["text"] = resultado




janela = Tk()
janela.title("Acerte o número")

texto_de_orientacao = Label(janela, text="Tente acertar o número aleatório que está entre 10 e 0: ")
texto_de_orientacao.grid(column = 0, row = 0, padx = 2, pady= 2)

Entrada = Entry(janela)
Entrada.grid(column = 0, row = 1, padx = 10, pady = 10)

botao = Button(janela, text="Iniciar", command=jogo_adivinhacao)
botao.grid(column = 0, row = 2, padx = 10, pady = 10)

texto_iniciar = Label(janela, text="")
texto_iniciar.grid(column = 0, row = 3, padx = 10, pady = 10)

janela.mainloop()



