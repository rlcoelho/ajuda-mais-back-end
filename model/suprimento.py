from sqlalchemy import Column, String, Integer
from model import Base
from model.abrigo_suprimento import AbrigoSuprimento

class Suprimento(Base):
    __tablename__ = 'suprimento'

    id_suprimento = Column(Integer, primary_key=True)
    descricao_suprimento = Column(String(100))
    qtd_para_pessoa_semana = Column(Integer)
        
    def __init__(self, descricao_suprimento:str, qtd_para_pessoa_semana: int):
        """
        Cadastra um suprimento

        Arguments:
            descricao_suprimento: descreve o suprimento
            qtd_para_pessoa_semana: quantidade necessária deste suprimento para cada pessoa por semana
        """
        self.descricao_suprimento = descricao_suprimento
        self.qtd_para_pessoa_semana = qtd_para_pessoa_semana
