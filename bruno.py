import tkinter as tk
from tkinter import messagebox, PhotoImage
import random as rnd

# Listas de palavras por categoria
frutas = ['banana', 'limão', 'melancia']
animais = ['anta', 'javali', 'escorpião']
objetos = ['xícara', 'caderno', 'panela', 'bruno', 'polônio', 'miguel']

# Função para iniciar o jogo
def iniciar_jogo():
    global palavra, categoria, tentativas_restantes, letras_tentadas, exibicao_palavra
    tentativas_restantes = 10
    letras_tentadas = []
    exibicao_palavra = []

    # Escolhe uma palavra aleatória de uma categoria aleatória
    indice_palavra = rnd.randint(0, len(frutas) - 1)
    indice_categoria = rnd.randint(0, 2)
    
    if indice_categoria == 0:
        palavra = frutas[indice_palavra]
        categoria = "FRUTAS"
    elif indice_categoria == 1:
        palavra = animais[indice_palavra]
        categoria = "ANIMAIS"
    else:
        palavra = objetos[indice_palavra]
        categoria = "OBJETOS"

    # Inicializa a exibição da palavra com underscores
    for letra in palavra:
        exibicao_palavra.append("_")

    atualizar_display()


# Função para lidar com o palpite do jogador
def processar_palpite():
    global tentativas_restantes, letras_tentadas, exibicao_palavra
    palpite = entrada_palpite.get().lower()
    entrada_palpite.delete(0, tk.END)  # Limpa o campo de entrada

    # Verifica se o palpite é válido (uma única letra)
    if len(palpite) != 1 or not palpite.isalpha():
        messagebox.showwarning("Entrada inválida", "Por favor, entre com uma letra válida!")
        return

    # Verifica se a letra já foi tentada
    if palpite in letras_tentadas:
        messagebox.showinfo("Entrada inválida", "Esta letra já foi tentada!")
        return

    letras_tentadas.append(palpite)

    # Verifica se o palpite está na palavra
    if palpite in palavra:
        for i in range(len(palavra)):
            if palavra[i] == palpite:
                exibicao_palavra[i] = palpite
        atualizar_display()
        if "".join(exibicao_palavra) == palavra:
            messagebox.showinfo("Você acertou!", f"Parabéns, a palavra era {palavra.upper()}!")
            resetar_jogo()
    else:
        tentativas_restantes -= 1
        img["file"] = f"erro={10 - tentativas_restantes}.png"
        atualizar_display()
        if tentativas_restantes == 0:
            messagebox.showinfo("Você não acertou", f"Suas tentativas acabaram. A palavra era {palavra.upper()}.")
            resetar_jogo()


# Função para atualizar os elementos visuais na tela
def atualizar_display():
    label_palavra.config(text=" ".join(exibicao_palavra))
    label_categoria.config(text=f"Categoria: {categoria}")
    label_tentativas.config(text=f"Tentativas Restantes: {tentativas_restantes}")
    label_tentadas.config(text=f"Letras Tentadas: {' '.join(letras_tentadas)}")


# Função para resetar o jogo
def resetar_jogo():
    global tentativas_restantes, letras_tentadas, exibicao_palavra
    tentativas_restantes = 10
    letras_tentadas = []
    exibicao_palavra = []
    iniciar_jogo()


# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Jogo da Forca")

label_categoria = tk.Label(janela, text="Categoria: ", font=("Arial", 14))
label_categoria.grid(row=0, column=0, pady=10)

label_palavra = tk.Label(janela, text=" ", font=("Arial", 24))
label_palavra.grid(row=1, column=0, pady=10)

label_tentativas = tk.Label(janela, text="Tentativas Restantes: ", font=("Arial", 14))
label_tentativas.grid(row=2, column=0, pady=5)

label_tentadas = tk.Label(janela, text="Letras Tentadas: ", font=("Arial", 14))
label_tentadas.grid(row=3, column=0, pady=5)

entrada_palpite = tk.Entry(janela, font=("Arial", 14), width=2)
entrada_palpite.grid(row=4, column=0, pady=10)

botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 14), command=processar_palpite)
botao_enviar.grid(row=5, column=0)

img = PhotoImage(file="erro=0.png")
label_img = tk.Label(janela, image=img)
label_img.grid(column=0, row=6, pady=10)

# Inicia o jogo pela primeira vez
iniciar_jogo()

janela.mainloop()
