import turtle
import random

# Configuração da tela
window = turtle.Screen()
window.bgcolor("white")
window.setup(width=800, height=600)  # Configura o tamanho da janela

# Configuração da tartaruga
t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.speed(0)  # Aumenta a velocidade da tartaruga

# Função para desenhar um quadrado
def desenhar_quadrado(tartaruga, lado):
    for _ in range(4):
        tartaruga.forward(lado)
        tartaruga.right(90)

# Função para mover a tartaruga para uma posição aleatória
def mover_para_posicao_aleatoria(tartaruga, largura, altura):
    x = random.randint(-largura//2, largura//2)
    y = random.randint(-altura//2, altura//2)
    tartaruga.penup()
    tartaruga.goto(x, y)
    tartaruga.pendown()

# Desenha 10 quadrados em posições aleatórias
for _ in range(100):
    mover_para_posicao_aleatoria(t, 800, 600)
    desenhar_quadrado(t, 100)

# Esconde a tartaruga
t.hideturtle()

# Mantém a janela aberta
window.mainloop()
