from sqlite3 import IntegrityError
from flask import Flask
from sqlalchemy.orm import joinedload
from model import Session
from logger import logger
from model.abrigo import Abrigo
from model.abrigo_suprimento import AbrigoSuprimento
from model.suprimento import Suprimento
from schemas.abrigo_suprimento import lista_abrigo_suprimentos

def get_abrigo_suprimentos(query):
    
    id_abrigo = query.fk_abrigo
    logger.debug(f"Coletando suprimentos ")
    # cria conexão com a base e lista todos os suprimentos por abrigo
    session = Session()
    abrigo_suprimentos =  (session.query(Suprimento)
        .join(AbrigoSuprimento, AbrigoSuprimento.fk_suprimento == Suprimento.id_suprimento)
        .filter(AbrigoSuprimento.fk_abrigo == id_abrigo)
        .options(joinedload(AbrigoSuprimento.abrigo))
        .all()
    )
    
    if not abrigo_suprimentos:
        # se não há suprimentos cadastrados no abrigo
        return {"abrigo_suprimentos": []}, 200
    else:
        logger.debug(f"%d suprimentos encontrados no abrigo" % len(abrigo_suprimentos))
        # retorna a representação do abrigo
        return lista_abrigo_suprimentos(abrigo_suprimentos), 200