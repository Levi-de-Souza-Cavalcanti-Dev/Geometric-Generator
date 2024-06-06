import tkinter as tk
from tkinter import Canvas
import turtle

class DesenhoFormas:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Desenhar Formas")

        # Criação do canvas para desenho
        self.canvas = Canvas(self.janela, width=400, height=400, bg="white")
        self.canvas.pack()

        # Criação dos botões
        self.botao_quadrado = tk.Button(self.janela, text="Quadrado", command=self.desenhar_quadrado)
        self.botao_quadrado.pack(side=tk.LEFT, padx=10)

        self.botao_triangulo = tk.Button(self.janela, text="Triângulo", command=self.desenhar_triangulo)
        self.botao_triangulo.pack(side=tk.LEFT, padx=10)

        self.botao_circulo = tk.Button(self.janela, text="Círculo", command=self.desenhar_circulo)
        self.botao_circulo.pack(side=tk.LEFT, padx=10)

        self.botao_pentagono = tk.Button(self.janela, text="Pentágono", command=self.desenhar_pentagono)
        self.botao_pentagono.pack(side=tk.LEFT, padx=10)

        self.botao_hexagono = tk.Button(self.janela, text="Hexágono", command=self.desenhar_hexagono)
        self.botao_hexagono.pack(side=tk.LEFT, padx=10)

    def desenhar_quadrado(self):
        self.canvas.delete("all")
        turtle.TurtleScreen._root = self.canvas
        t = turtle.RawTurtle(self.canvas)
        t.shape("turtle")
        for _ in range(4):
            t.forward(100)
            t.right(90)

    def desenhar_triangulo(self):
        self.canvas.delete("all")
        turtle.TurtleScreen._root = self.canvas
        t = turtle.RawTurtle(self.canvas)
        t.shape("turtle")
        for _ in range(3):
            t.forward(100)
            t.left(120)

    def desenhar_circulo(self):
        self.canvas.delete("all")
        turtle.TurtleScreen._root = self.canvas
        t = turtle.RawTurtle(self.canvas)
        t.shape("turtle")
        t.circle(50)

    def desenhar_pentagono(self):
        self.canvas.delete("all")
        turtle.TurtleScreen._root = self.canvas
        t = turtle.RawTurtle(self.canvas)
        t.shape("turtle")
        for _ in range(5):
            t.forward(100)
            t.right(72)

    def desenhar_hexagono(self):
        self.canvas.delete("all")
        turtle.TurtleScreen._root = self.canvas
        t = turtle.RawTurtle(self.canvas)
        t.shape("turtle")
        for _ in range(6):
            t.forward(100)
            t.right(60)

# Criação da janela principal
janela_principal = tk.Tk()
app = DesenhoFormas(janela_principal)
janela_principal.mainloop()
