import time

from canvas import Canvas

W, H = 800, 600
c = Canvas(W, H, "Etapa 1 - pixel")

t0 = time.perf_counter()
for y in range(H):
    for x in range(W):
        c.pixel(x, y, 20, 20, 40)
print(f"preencher {W}x{H} = {W * H} chamadas: {time.perf_counter() - t0:.3f}s")

for dx in range(10):
    for dy in range(10):
        c.pixel(dx, dy, 255, 0, 0)
        c.pixel(W - 1 - dx, dy, 0, 255, 0)
        c.pixel(dx, H - 1 - dy, 0, 0, 255)
        c.pixel(W - 1 - dx, H - 1 - dy, 255, 255, 255)

for x in range(W):
    c.pixel(x, 10, 255, 255, 0)
for y in range(H):
    c.pixel(10, y, 0, 255, 255)

while c.rodando():
    c.present()
c.fechar()
