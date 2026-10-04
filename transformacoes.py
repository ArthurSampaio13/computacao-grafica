import math


def transladar(pontos, tx, ty):
    return [(x + tx, y + ty) for x, y in pontos]


def escalar(pontos, sx, sy):
    return [(x * sx, y * sy) for x, y in pontos]


def rotacionar(pontos, ang):
    c, s = math.cos(ang), math.sin(ang)
    return [(x * c - y * s, x * s + y * c) for x, y in pontos]


def para_pixels(pontos):
    return [(math.floor(x + 0.5), math.floor(y + 0.5)) for x, y in pontos]
