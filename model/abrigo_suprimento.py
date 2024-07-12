from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from model import Base


class AbrigoSuprimento(Base):
    __tablename__ = 'abrigo_suprimento'
    
    id_abrigo_suprimento = Column(Integer, primary_key=True)
    fk_abrigo = Column(Integer, ForeignKey("abrigo.id_abrigo"), nullable=False)
    fk_suprimento = Column(Integer, ForeignKey("suprimento.id_suprimento"), nullable=False)
    qtd_atual = Column(Integer)
    
    abrigo = relationship("Abrigo")
    suprimento = relationship("Suprimento")
    
        
    def __init__(self, fk_abrigo: int, fk_suprimento: int, qtd_atual: int):
        """
        Cadastra os suprimentos por abrigo e atualiza a quantidade atual de suprimentos

        Arguments:
            fk_abrigo: foreignkey do abrigo
            fk_suprimento: foreignkey do suprimento
            qtd_atual: quantidade atual do suprimento no abrigo
        """
        self.fk_abrigo = fk_abrigo
        self.fk_suprimento = fk_suprimento
        self.qtd_atual = qtd_atual
