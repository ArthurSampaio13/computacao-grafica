# computacao-grafica

Biblioteca de computação gráfica 2D em Python. A SDL2 só abre a janela e mostra o framebuffer; todo o resto é desenhado a partir de `canvas.pixel(x, y, r, g, b)`.

## Como rodar

Precisa do [uv](https://docs.astral.sh/uv/).

```
uv run main.py          # menu com as demos
uv run main.py linha    # roda uma demo direto
```

## O que tem

- `canvas.py`: janela, framebuffer, `pixel`, `ponto`, `limpar` e zoom
- `primitivas.py`: linha (ingênua, DDA, Bresenham), triângulo, retângulo, polígono e preenchimento por scanline
- `transformacoes.py`: translação, escala e rotação
- `demo_*.py`: uma demo por etapa

## O que falta

- Matrizes e composição de transformações
- Coordenadas de mundo para tela
- Clipping
- Antialiasing
