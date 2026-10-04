def linha_ingenua(c, x0, y0, x1, y1, r, g, b):
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0
    m = (y1 - y0) / (x1 - x0)
    for x in range(x0, x1 + 1):
        c.ponto(x, y0 + m * (x - x0), r, g, b)


def linha_dda(c, x0, y0, x1, y1, r, g, b):
    dx, dy = x1 - x0, y1 - y0
    passos = max(abs(dx), abs(dy))
    if passos == 0:
        c.ponto(x0, y0, r, g, b)
        return
    sx, sy = dx / passos, dy / passos
    x, y = x0, y0
    for _ in range(passos + 1):
        c.ponto(x, y, r, g, b)
        x += sx
        y += sy


def linha_bresenham(c, x0, y0, x1, y1, r, g, b):
    ingreme = abs(y1 - y0) > abs(x1 - x0)
    if ingreme:
        x0, y0, x1, y1 = y0, x0, y1, x1
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x1 >= x0 else -1
    sy = 1 if y1 >= y0 else -1
    d = 2 * dy - dx
    y = y0
    for x in range(x0, x1 + sx, sx):
        if ingreme:
            c.pixel(y, x, r, g, b)
        else:
            c.pixel(x, y, r, g, b)
        if d > 0 or (d == 0 and sy > 0):
            y += sy
            d -= 2 * dx
        d += 2 * dy


def poligono(c, pontos, r, g, b):
    for (x0, y0), (x1, y1) in zip(pontos, pontos[1:] + pontos[:1]):
        linha_bresenham(c, x0, y0, x1, y1, r, g, b)


def triangulo(c, p0, p1, p2, r, g, b):
    poligono(c, [p0, p1, p2], r, g, b)


def retangulo(c, x0, y0, x1, y1, r, g, b):
    poligono(c, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)], r, g, b)


def preencher_poligono(c, pontos, r, g, b):
    arestas = list(zip(pontos, pontos[1:] + pontos[:1]))
    ys = [y for _, y in pontos]
    for y in range(min(ys), max(ys)):
        xs = []
        for (x0, y0), (x1, y1) in arestas:
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0
            if y0 <= y < y1:
                num = x0 * (y1 - y0) + (y - y0) * (x1 - x0)
                xs.append(-(-num // (y1 - y0)))
        xs.sort()
        for xa, xb in zip(xs[::2], xs[1::2]):
            for x in range(xa, xb):
                c.pixel(x, y, r, g, b)
