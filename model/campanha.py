from sqlalchemy import Column, String, Integer

from model import Base


class Campanha(Base):
    __tablename__ = 'campanha'

    id_campanha = Column(Integer, primary_key=True)
    descricao_campanha = Column(String(50))
    
    def __init__(self, descricao_campanha:str):
        """
        Cria uma Campanha de Ajuda

        Arguments:
            descricao_campanha: descreve a campanha.
        """
        self.descricao_campanha = descricao_campanha

