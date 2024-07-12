import datetime as dt
from sqlite3 import IntegrityError
from urllib.parse import unquote
from flask import Flask
from sqlalchemy.orm import joinedload
from model import Session
from logger import logger
from model.abrigo import Abrigo
from schemas.abrigo import AbrigoBuscaSchema, exibe_abrigo, lista_abrigos

def get_abrigos(query):
    
    id_campanha = query.id_campanha
    logger.debug(f"Coletando abrigos ")
    # cria conexão com a base e lista todos os abrigos por campanha
    session = Session()
    abrigos = session.query(Abrigo).filter_by(fk_campanha=id_campanha).options(joinedload(Abrigo.campanha)).all()
     
    if not abrigos:
        # se não há abrigos cadastradas
        return {"abrigos": []}, 200
    else:
        logger.debug(f"%d abrigos encontradas" % len(abrigos))
        # retorna a representação do abrigo
        return lista_abrigos(abrigos), 200
    
    
def get_abrigo(query):   

    abrigo_id = query.id_abrigo
    logger.debug(f"Coletando dados sobre o abrigo ID #{abrigo_id}")
    
    # cria conexão com a base e faz a busca pelo ID do abrigo
    session = Session()
    abrigo = session.query(Abrigo).filter(Abrigo.id_abrigo == abrigo_id).first()

    if abrigo:
        logger.debug(f"Abrigo econtrado: '{abrigo.descricao_abrigo}'")  
        return exibe_abrigo(abrigo), 200
    else:
        error_msg = "Abrigo não encontrado:/"
        logger.warning(f"Erro ao buscar abrigo '{abrigo_id}', {error_msg}")
        return {"mensagem": error_msg}, 404


def add_abrigo(form):
          
    abrigo = Abrigo(
        fk_campanha = form.fk_campanha,
        descricao_abrigo = str(form.descricao_abrigo),
        capacidade_maxima = form.capacidade_maxima,
        lotacao_atual = form.lotacao_atual,
        logradouro = str(form.logradouro),
        numero = form.numero,
        complemento = str(form.complemento),
        bairro = str(form.bairro),
        cidade = str(form.cidade),
        estado = str(form.estado),
        cep = str(form.cep),       
        ativo = form.ativo,
        data_inclusao = dt.datetime.now(),
        data_atualizacao = dt.datetime.now()
        )
    
    logger.debug(f"Adicionando abrigo: '{abrigo.descricao_abrigo}'")
    
    try:
        # cria conexão com a base e adiciona o abrigo
        session = Session()
        session.add(abrigo)
        session.commit()
        
        logger.debug(f"Adicionado abrigo: '{abrigo.descricao_abrigo}'")
        
        return exibe_abrigo(abrigo), 200

    except IntegrityError as e:
        # erro de integridade do IntegrityError
        error_msg = "Erro de integridade:/"
        logger.warning(f"Erro ao adicionar abrigo '{abrigo.descricao_abrigo}', {error_msg}")
        
        return {"mensagem": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova abrigo:/"
        logger.warning(f"Erro ao adicionar abrigo '{abrigo.descricao_abrigo}', {error_msg}")
        
        return {"mensagem": error_msg}, 400
    

def update_abrigo(form):
    
    logger.debug(f"Atualizando o abrigo #{form.id_abrigo}")
    
    try:
        # cria conexão com a base e atualiza o abrigo
        session = Session()
        abrigo_atual = session.query(Abrigo).filter(Abrigo.id_abrigo == form.id_abrigo).first()

        # Atualiza os campos do abrigo existente com os novos valores
        abrigo_atual.id_abrigo = form.id_abrigo  
        abrigo_atual.descricao_abrigo = str(form.descricao_abrigo)
        abrigo_atual.capacidade_maxima = form.capacidade_maxima
        abrigo_atual.lotacao_atual = form.lotacao_atual
        abrigo_atual.logradouro = str(form.logradouro)
        abrigo_atual.numero = form.numero
        abrigo_atual.complemento = str(form.complemento)
        abrigo_atual.bairro = str(form.bairro)
        abrigo_atual.cidade = str(form.cidade)
        abrigo_atual.estado = str(form.estado)
        abrigo_atual.cep = str(form.cep)  
        abrigo_atual.ativo = form.ativo
        abrigo_atual.data_atualizacao = dt.datetime.now()
        
        session.commit()
        
        logger.debug(f"Atualizando abrigo '{form.id_abrigo}'")
        
        return exibe_abrigo(abrigo_atual), 200

    except IntegrityError as e:
        # erro de integridade do IntegrityError
        error_msg = "Erro de integridade:/"
        logger.warning(f"Erro ao alterar abrigo '{form.id_abrigo}', {error_msg}")
        
        return {"mensagem": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar abrigo:/"
        logger.warning(f"Erro ao alterar abrigo '{form.id_abrigo}', {error_msg}")
        
        return {"mensagem": error_msg}, 400
