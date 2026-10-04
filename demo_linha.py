import math

from canvas import Canvas
from primitivas import linha_bresenham, linha_dda, linha_ingenua

W, H = 121, 41
c = Canvas(W, H, "Etapa 3/4 - ingenua | DDA | Bresenham", zoom=10)

for k in range(16):
    a = k * math.pi / 8 + 0.1
    dx, dy = round(18 * math.cos(a)), round(18 * math.sin(a))
    linha_ingenua(c, 20, 20, 20 + dx, 20 + dy, 255, 120, 0)
    linha_dda(c, 60, 20, 60 + dx, 20 + dy, 0, 220, 255)
    linha_bresenham(c, 100, 20, 100 + dx, 20 + dy, 120, 255, 80)

while c.rodando():
    c.present()
c.fechar()
