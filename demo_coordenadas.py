from canvas import Canvas

W, H = 40, 30
c = Canvas(W, H, "Etapa 2 - coordenadas (zoom 16x)", zoom=16)

for i in range(1, 8):
    c.pixel(i, 0, 0, 255, 0)
    c.pixel(0, i, 0, 120, 255)
c.pixel(0, 0, 255, 0, 0)


def parabola(x):
    return 0.06 * (x - 20) ** 2


for x in range(W):
    y = parabola(x)
    c.ponto(x, y, 255, 255, 255)
    c.ponto(x, (H - 1) - y, 255, 220, 0)

while c.rodando():
    c.present()
c.fechar()
