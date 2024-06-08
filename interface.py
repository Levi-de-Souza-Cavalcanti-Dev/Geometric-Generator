import tkinter as tk
from tkinter import Canvas, messagebox
import turtle
from PIL import ImageGrab

class DesenhoPlantaCasa:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Desenhar Planta de Casa")

        # Obter as dimensões da tela
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()

        # Criação do botão
        self.botao_desenhar = tk.Button(self.janela, text="Desenhar Planta de Casa", command=self.desenhar_planta_casa)
        self.botao_desenhar.pack(side=tk.TOP, pady=10)

        # Criação do canvas para desenho
        self.canvas = Canvas(self.janela, width=largura_tela, height=altura_tela, bg="white")
        self.canvas.pack()

    def desenhar_planta_casa(self):
        self.canvas.delete("all")
        turtle.TurtleScreen._root = self.canvas
        t = turtle.RawTurtle(self.canvas)
        t.shape("turtle")
        t.speed(20000000000)

        # Calcula as coordenadas para centralizar o desenho
        x_centro = self.canvas.winfo_reqwidth() // 5
        y_centro = self.canvas.winfo_reqheight() // 5

        # Desenhar a planta da casa
        self.desenhar_sala(t, x_centro, y_centro)
        self.desenhar_quarto(t, x_centro + 100, y_centro + 150)
        self.desenhar_quarto(t, x_centro - 300, y_centro + 150)
        self.desenhar_cozinha(t, x_centro - 100, y_centro + 50)
        self.desenhar_banheiro(t, x_centro, y_centro - 0)
        self.desenhar_garagem(t, x_centro, y_centro - 300)

        # Adicionar textos aos comodos
        self.canvas.create_text(x_centro, y_centro + 200, text="Sala", font=("Arial", 12, "bold"))
        self.canvas.create_text(x_centro - 200, y_centro + 200, text="Quarto", font=("Arial", 12, "bold"))
        self.canvas.create_text(x_centro + 200, y_centro + 200, text="Quarto", font=("Arial", 12, "bold"))
        self.canvas.create_text(x_centro, y_centro - 50, text="Cozinha", font=("Arial", 12, "bold"))
        self.canvas.create_text(x_centro, y_centro - 200, text="Banheiro", font=("Arial", 12, "bold"))
        self.canvas.create_text(x_centro, y_centro - 450, text="Garagem", font=("Arial", 12, "bold"))

        # Salvar imagem
        self.salvar_imagem()

    def desenhar_sala(self, turtle_obj, x, y):
        turtle_obj.penup()
        turtle_obj.goto(x - 100, y + 150)
        turtle_obj.pendown()

        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(300)
        turtle_obj.right(90)
        turtle_obj.forward(400)
        turtle_obj.right(90)
        turtle_obj.forward(300)
        turtle_obj.right(90)
        turtle_obj.forward(200)

    def desenhar_quarto(self, turtle_obj, x, y):
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()

        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(300)
        turtle_obj.right(90)
        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(300)
        turtle_obj.right(90)

    def desenhar_cozinha(self, turtle_obj, x, y):
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()

        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(200)
        turtle_obj.right(90)

    def desenhar_banheiro(self, turtle_obj, x, y):
        turtle_obj.penup()
        turtle_obj.goto(x - 100, y - 150)
        turtle_obj.pendown()

        turtle_obj.forward(300)
        turtle_obj.right(90)
        turtle_obj.forward(300)
        turtle_obj.right(90)
        turtle_obj.forward(300)
        turtle_obj.right(90)
        turtle_obj.forward(300)
        turtle_obj.right(90)

    def desenhar_garagem(self, turtle_obj, x, y):
        turtle_obj.penup()
        turtle_obj.goto(x - 100, y - 350)
        turtle_obj.pendown()

        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(100)
        turtle_obj.right(90)
        turtle_obj.forward(200)
        turtle_obj.right(90)
        turtle_obj.forward(100)
        turtle_obj.right(90)

    def salvar_imagem(self):
        # Capturar a área do canvas
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        # Capturar a imagem e salvar em um arquivo
        imagem = ImageGrab.grab(bbox=(x, y, x + w, y + h))
        imagem.save("planta_casa.png")
        messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")

# Criação da janela principal
janela_principal = tk.Tk()
app = DesenhoPlantaCasa(janela_principal)
janela_principal.geometry(f"{janela_principal.winfo_screenwidth()}x{janela_principal.winfo_screenheight()}")
janela_principal.mainloop()