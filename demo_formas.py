from canvas import Canvas
from primitivas import poligono, retangulo, triangulo

c = Canvas(80, 50, "Etapa 5 - triangulo, retangulo, poligono", zoom=10)
triangulo(c, (3, 3), (30, 8), (10, 40), 255, 120, 0)
retangulo(c, 36, 4, 56, 20, 0, 220, 255)
poligono(c, [(45, 28), (70, 26), (76, 40), (60, 47), (40, 42)], 120, 255, 80)

while c.rodando():
    c.present()
c.fechar()
