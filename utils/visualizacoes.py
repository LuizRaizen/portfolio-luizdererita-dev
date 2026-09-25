from utils.models import Visualizacao
from utils.db import db

def registrar_visualizacao(projeto, pagina):
    registro = Visualizacao.query.filter_by(projeto=projeto, pagina=pagina).first()
    if registro:
        registro.quantidade += 1
    else:
        registro = Visualizacao(projeto=projeto, pagina=pagina, quantidade=1)
        db.session.add(registro)
    db.session.commit()

def obter_visualizacoes(projeto, pagina):
    registro = Visualizacao.query.filter_by(projeto=projeto, pagina=pagina).first()
    return registro.quantidade if registro else 0
