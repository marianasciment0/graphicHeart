from turtle import *

# Define a cor de preenchimento como azul
color("blue")

# Inicia o preenchimento da figura
begin_fill()

# Define a largura da caneta como 3
pensize(3)

# Desenha um triângulo
for _ in range(3):
    forward(100)
    left(120)

# Completa o preenchimento da figura
end_fill()

# Mantém a janela aberta até que seja fechada pelo usuário
done()
