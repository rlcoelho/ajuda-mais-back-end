from sqlite3 import IntegrityError
from urllib.parse import unquote
from model import Suprimento, Session
from logger import logger
from schemas.suprimento import exibe_suprimento, lista_suprimentos

def get_suprimentos():

    logger.debug(f"Coletando suprimentos ")
    # cria conexão com a base e lista todos os suprimentos
    session = Session()
    suprimentos = session.query(Suprimento).all()
    
    if not suprimentos:
        # se não há suprimentos cadastradas
        return {"suprimentos": []}, 200
    else:
        logger.debug(f"%d suprimentos encontradas" % len(suprimentos))
        # retorna a representação da lista de suprimentos
        print(suprimentos)
        return lista_suprimentos(suprimentos), 200
    

def get_suprimento(query):   

    suprimento_id = query.id_suprimento
    logger.debug(f"Coletando dados sobre o abrigo ID #{suprimento_id}")
    
    # cria conexão com a base e faz a busca pelo ID do suprimento
    session = Session()
    suprimento = session.query(Suprimento).filter(Suprimento.id_suprimento == suprimento_id).first()

    if suprimento:
        logger.debug(f"Suprimento econtrado: '{suprimento.descricao_suprimento}'")  
        return exibe_suprimento(suprimento), 200
    else:
        error_msg = "Suprimento não encontrado:/"
        logger.warning(f"Erro ao buscar suprimento '{suprimento_id}', {error_msg}")
        return {"mensagem": error_msg}, 404


def add_suprimento(form):

    suprimento = Suprimento(
        descricao_suprimento = form.descricao_suprimento,
        qtd_para_pessoa_semana = form.qtd_para_pessoa_semana
        )
    logger.debug(f"Adicionando suprimento: '{suprimento.descricao_suprimento}'")
    
    try:
        # cria conexão com a base e adiciona o suprimento
        session = Session()
        session.add(suprimento)
        session.commit()
        
        logger.debug(f"Adicionado suprimento '{suprimento.descricao_suprimento}'")
        
        return exibe_suprimento(suprimento), 200

    except IntegrityError as e:
        # erro de integridade do IntegrityError
        error_msg = "Erro de integridade:/"
        logger.warning(f"Erro ao adicionar abrigo '{suprimento.descricao_suprimento}', {error_msg}")
        
        return {"mensagem": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova suprimento:/"
        logger.warning(f"Erro ao adicionar abrigo '{suprimento.descricao_suprimento}', {error_msg}")
        
        return {"mensagem": error_msg}, 400


def del_suprimento(query):

    suprimento_id = unquote(unquote(query.id_suprimento))
    logger.debug(f"Deletando dados do suprimento #{suprimento_id}")
    
    # cria conexão com a base e remove o suprimento
    session = Session()
    count = session.query(Suprimento).filter(Suprimento.id_suprimento == suprimento_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado o suprimento #{suprimento_id}")
        return {"mensagem": "Suprimento removido", "id_suprimento": suprimento_id}
    else:
        error_msg = "Suprimento não encontrado:/"
        logger.warning(f"Erro ao deletar suprimento #'{suprimento_id}', {error_msg}")
        return {"mensagem": error_msg}, 404


def update_suprimento(form):
    
    logger.debug(f"Atualizando o suprimento #{form.id_suprimento}")
    
    try:
        # cria conexão com a base e atualiza o suprimento
        session = Session()
        suprimento_atual = session.query(Suprimento).filter(Suprimento.id_suprimento == form.id_suprimento).first()

        # Atualiza os campos do suprimento existente com os novos valores
        suprimento_atual.descricao_suprimento = form.descricao_suprimento
        suprimento_atual.qtd_para_pessoa_semana = form.qtd_para_pessoa_semana
        session.commit()
        
        logger.debug(f"Atualizando suprimento '{form.id_suprimento}'")
        
        return exibe_suprimento(suprimento_atual), 200

    except IntegrityError as e:
        # erro de integridade do IntegrityError
        error_msg = "Erro de integridade:/"
        logger.warning(f"Erro ao alterar suprimento '{form.id_suprimento}', {error_msg}")
        
        return {"mensagem": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar suprimento:/"
        logger.warning(f"Erro ao alterar suprimento '{form.id_suprimento}', {error_msg}")
        
        return {"mensagem": error_msg}, 400
