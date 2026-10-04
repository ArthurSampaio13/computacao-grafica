import runpy
import sys
from pathlib import Path

DEMOS = {p.stem.removeprefix("demo_"): p for p in sorted(Path(__file__).parent.glob("demo_*.py"))}


def rodar(nome):
    runpy.run_path(str(DEMOS[nome]), run_name="__main__")


def escolher(texto, nomes):
    if texto in DEMOS:
        return texto
    if texto.isdigit() and 1 <= int(texto) <= len(nomes):
        return nomes[int(texto) - 1]
    return None


nomes = list(DEMOS)

if len(sys.argv) > 1:
    nome = escolher(sys.argv[1], nomes)
    if nome is None:
        sys.exit(f"demo desconhecida: {sys.argv[1]} (opções: {', '.join(nomes)})")
    rodar(nome)
    sys.exit()

while True:
    print()
    for i, n in enumerate(nomes, 1):
        print(f"  {i}. {n}")
    try:
        texto = input("demo (enter para sair): ").strip()
    except EOFError:
        break
    if not texto:
        break
    nome = escolher(texto, nomes)
    if nome is None:
        print("opção inválida")
    else:
        rodar(nome)
