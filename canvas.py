import ctypes
import math

import sdl2

BPP = 3


class Canvas:
    def __init__(self, largura, altura, titulo="Canvas", janela=True, zoom=1):
        self.largura = largura
        self.altura = altura
        self.pitch = largura * BPP
        self.fb = bytearray(self.pitch * altura)
        self._sdl = False
        if janela:
            self._abrir_janela(titulo, zoom)

    def pixel(self, x, y, r, g, b):
        if not (0 <= x < self.largura and 0 <= y < self.altura):
            return
        i = (y * self.largura + x) * BPP
        self.fb[i] = r
        self.fb[i + 1] = g
        self.fb[i + 2] = b

    def limpar(self, r=0, g=0, b=0):
        self.fb[:] = bytes((r, g, b)) * (self.largura * self.altura)

    def ponto(self, x, y, r, g, b):
        self.pixel(math.floor(x + 0.5), math.floor(y + 0.5), r, g, b)

    def _abrir_janela(self, titulo, zoom):
        if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
            raise RuntimeError(sdl2.SDL_GetError().decode())
        self._sdl = True
        self._janela = sdl2.SDL_CreateWindow(
            titulo.encode(),
            sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
            self.largura * zoom, self.altura * zoom, sdl2.SDL_WINDOW_SHOWN,
        )
        sdl2.SDL_SetHint(sdl2.SDL_HINT_RENDER_SCALE_QUALITY, b"0")
        self._renderer = sdl2.SDL_CreateRenderer(self._janela, -1, sdl2.SDL_RENDERER_PRESENTVSYNC)
        self._textura = sdl2.SDL_CreateTexture(
            self._renderer, sdl2.SDL_PIXELFORMAT_RGB24,
            sdl2.SDL_TEXTUREACCESS_STREAMING, self.largura, self.altura,
        )
        if not (self._janela and self._renderer and self._textura):
            raise RuntimeError(sdl2.SDL_GetError().decode())
        self._ptr = (ctypes.c_char * len(self.fb)).from_buffer(self.fb)
        self._evento = sdl2.SDL_Event()

    def present(self):
        sdl2.SDL_UpdateTexture(self._textura, None, self._ptr, self.pitch)
        sdl2.SDL_RenderCopy(self._renderer, self._textura, None, None)
        sdl2.SDL_RenderPresent(self._renderer)

    def rodando(self):
        while sdl2.SDL_PollEvent(ctypes.byref(self._evento)):
            if self._evento.type == sdl2.SDL_QUIT:
                return False
        return True

    def fechar(self):
        if self._sdl:
            sdl2.SDL_DestroyTexture(self._textura)
            sdl2.SDL_DestroyRenderer(self._renderer)
            sdl2.SDL_DestroyWindow(self._janela)
            sdl2.SDL_Quit()
            self._sdl = False
