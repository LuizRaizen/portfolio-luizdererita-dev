"""
Gera as imagens dos certificados a partir dos PDFs em static/docs/certificados/.

Para cada PDF cria, em static/img/certificados/:
    <nome>.webp         prévia (960 px de largura) — usada nos cards em destaque
    <nome>-thumb.webp   miniatura (320 px)          — usada nas listas

Ferramenta de desenvolvimento (não é importada pelo app). Dependências:
    pip install pymupdf pillow
Uso (na raiz do projeto):
    python tools/extrair_certificados.py              # só o que ainda não existe
    python tools/extrair_certificados.py --refazer    # regera tudo
    python tools/extrair_certificados.py codigo1 codigo2   # só esses PDFs (sem .pdf)

Só a primeira página é usada (certificados de várias páginas trazem o verso/lista
de módulos nas seguintes).
"""

import argparse
import io
import sys
from pathlib import Path

import pymupdf
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
PDFS = RAIZ / "static" / "docs" / "certificados"
IMAGENS = RAIZ / "static" / "img" / "certificados"

LARGURAS = {"": (960, 78), "-thumb": (320, 72)}  # sufixo -> (largura, qualidade webp)


def renderizar(pdf: Path) -> Image.Image:
    pagina = pymupdf.open(pdf)[0]
    pix = pagina.get_pixmap(dpi=200)
    return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("nomes", nargs="*", help="nomes de PDF (sem extensão); vazio = todos")
    ap.add_argument("--refazer", action="store_true")
    args = ap.parse_args()

    IMAGENS.mkdir(parents=True, exist_ok=True)
    pdfs = [PDFS / f"{n}.pdf" for n in args.nomes] if args.nomes else sorted(PDFS.glob("*.pdf"))
    feitos = 0
    for pdf in pdfs:
        if not pdf.exists():
            print(f"não encontrado: {pdf.name}", file=sys.stderr)
            continue
        base = pdf.stem.lower()
        alvos = {suf: IMAGENS / f"{base}{suf}.webp" for suf in LARGURAS}
        if not args.refazer and all(a.exists() for a in alvos.values()):
            continue
        img = renderizar(pdf)
        for suf, (largura, qualidade) in LARGURAS.items():
            altura = round(img.height * largura / img.width)
            img.resize((largura, altura), Image.LANCZOS).save(alvos[suf], "WEBP", quality=qualidade, method=6)
        feitos += 1
        print(f"ok  {pdf.name}")
    print(f"{feitos} certificado(s) processado(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
