import time

from canvas import Canvas
from primitivas import poligono, preencher_poligono
from transformacoes import escalar, para_pixels, rotacionar, transladar

c = Canvas(120, 70, "Etapa 7 - transformacoes", zoom=8)
tri = [(-10, -8), (12, -2), (-4, 10)]
t0 = time.perf_counter()

while c.rodando():
    t = time.perf_counter() - t0
    c.limpar(15, 15, 30)

    em_volta_da_origem = rotacionar(transladar(tri, 30, 35), t)
    poligono(c, para_pixels(em_volta_da_origem), 255, 120, 0)

    s = 1 + 0.4 * abs(t % 2 - 1)
    em_volta_do_centro = transladar(rotacionar(escalar(tri, s, s), t), 90, 35)
    pix = para_pixels(em_volta_do_centro)
    preencher_poligono(c, pix, 0, 220, 255)
    poligono(c, pix, 255, 255, 255)

    c.present()
c.fechar()
