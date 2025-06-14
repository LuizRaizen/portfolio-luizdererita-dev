import os
import json

CAMINHO_ARQUIVO = "data/visualizacoes.json"

def _carregar_dados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
        with open(CAMINHO_ARQUIVO, "w") as f:
            json.dump({}, f)
    with open(CAMINHO_ARQUIVO, "r") as f:
        return json.load(f)

def _salvar_dados(dados):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(dados, f, indent=2)

def registrar_visualizacao(projeto, nome_post):
    chave = f"{projeto}/{nome_post}"
    dados = _carregar_dados()
    dados[chave] = dados.get(chave, 0) + 1
    _salvar_dados(dados)

def obter_visualizacoes(projeto, nome_post):
    chave = f"{projeto}/{nome_post}"
    dados = _carregar_dados()
    return dados.get(chave, 0)
