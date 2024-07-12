from sqlite3 import IntegrityError
from urllib.parse import unquote
from sqlalchemy import func
from model import Campanha, Session
from logger import logger
from model.abrigo import Abrigo
from schemas.campanha import exibe_campanha, lista_campanhas

def get_campanhas():

    logger.debug(f"Coletando campanhas ")
    # cria conexão com a base e lista todas as campanhas
    session = Session()
    campanhas = session.query(Campanha).all()
    
    if not campanhas:
        # se não há campanhas cadastradas
        return {"campanhas": []}, 200
    else:
        logger.debug(f"%d campanhas encontradas" % len(campanhas))
        # retorna a representação da lista de campanhas
        print(campanhas)
        return lista_campanhas(campanhas), 200


def add_campanha(form):

    campanha = Campanha(descricao_campanha=form.descricao_campanha)
    logger.debug(f"Adicionando campanha: '{campanha.descricao_campanha}'")
    
    try:
        # cria conexão com a base e adiciona a campanha
        session = Session()
        session.add(campanha)
        session.commit()
        
        logger.debug(f"Adicionado campanha '{campanha.descricao_campanha}'")
        
        return exibe_campanha(campanha), 200

    except IntegrityError as e:
        # erro de integridade do IntegrityError
        error_msg = "Erro de integridade:/"
        logger.warning(f"Erro ao adicionar abrigo '{campanha.descricao_campanha}', {error_msg}")
        
        return {"mensagem": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova campanha:/"
        logger.warning(f"Erro ao adicionar abrigo '{campanha.descricao_campanha}', {error_msg}")
        
        return {"mensagem": error_msg}, 400


def del_campanha(query):

    campanha_id = unquote(unquote(query.id_campanha))
    logger.debug(f"Deletando dados da campanha #{campanha_id}")
    
    # cria conexão com a base e remove a campanha
    session = Session()
    count = session.query(Campanha).filter(Campanha.id_campanha == campanha_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletada a campanha #{campanha_id}")
        return {"mensagem": "Campanha removida", "id_campanha": campanha_id}
    else:
        error_msg = "Campanha não encontrada:/"
        logger.warning(f"Erro ao deletar campanha #'{campanha_id}', {error_msg}")
        return {"mensagem": error_msg}, 404


def tem_abrigos(query): 
    
    id_campanha = query.id_campanha
    logger.debug(f"Verificando se a campanha #{id_campanha} tem abrigos associados")
    
    # cria conexão com a base e faz a busca por fk_campanha em Abrigo
    session = Session()
    count = session.query(func.count(Abrigo.id_abrigo)).filter(Abrigo.fk_campanha == id_campanha).scalar()

    if count > 0:
        logger.debug(f"Campanha #{id_campanha} tem abrigos associadas")  
        return {"tem_abrigos": {"tem_abrigos": True}}, 200
    else:
        logger.debug(f"Campanha #{id_campanha} não tem abrigos associadas")
        return {"tem_abrigos": {"tem_abrigos": False}}, 200
