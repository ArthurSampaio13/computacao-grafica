import math

from canvas import Canvas
from primitivas import poligono, preencher_poligono

c = Canvas(90, 50, "Etapa 6 - preenchimento (scanline, par-impar)", zoom=10)

tri = [(3, 3), (30, 10), (10, 45)]
preencher_poligono(c, tri, 255, 120, 0)
poligono(c, tri, 255, 255, 255)

estrela = [(55 + round(20 * math.cos(math.pi / 2 + k * 4 * math.pi / 5)),
            25 - round(20 * math.sin(math.pi / 2 + k * 4 * math.pi / 5))) for k in range(5)]
preencher_poligono(c, estrela, 0, 220, 255)

quad = [(78, 5), (88, 5), (88, 45), (78, 45)]
preencher_poligono(c, quad[:3], 120, 255, 80)
preencher_poligono(c, [quad[0], quad[2], quad[3]], 255, 80, 200)

while c.rodando():
    c.present()
c.fechar()
