from utils.db import db

class Visualizacao(db.Model):
    __tablename__ = 'visualizacoes'

    id = db.Column(db.Integer, primary_key=True)
    projeto = db.Column(db.String, nullable=False)
    pagina = db.Column(db.String, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)

    __table_args__ = (db.UniqueConstraint('projeto', 'pagina', name='uix_projeto_pagina'),)
