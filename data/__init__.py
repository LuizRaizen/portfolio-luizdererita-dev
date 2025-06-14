import importlib
import os
from flask import current_app

import importlib
import os

def carregar_projeto(nome):
    """Importa dinamicamente o módulo do projeto pelo nome."""
    try:
        nome_modulo = nome.replace('-', '_')  # converte para nome de módulo válido
        modulo = importlib.import_module(f"data.{nome_modulo}")

        caminho_logo = os.path.join("static", "img", nome, "logo.png")
        tem_logo = os.path.exists(caminho_logo)

        return {
            "projeto": getattr(modulo, "projeto"),
            "ficha_tecnica": getattr(modulo, "ficha_tecnica", {}),
            "posts": sorted(getattr(modulo, "posts", []), key=lambda post: post["data"], reverse=True),
            "roadmap": getattr(modulo, "roadmap", []),
            "imagens": getattr(modulo, "imagens", []),
            "videos": getattr(modulo, "videos", []),
            "downloads": getattr(modulo, "downloads", []),
            "tem_logo": tem_logo
        }

    except ModuleNotFoundError:
        return None
