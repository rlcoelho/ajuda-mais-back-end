from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from typing import Union

from model import Base

class Abrigo(Base):
    __tablename__ = 'abrigo'

    id_abrigo = Column(Integer, primary_key=True)
    fk_campanha = Column(Integer, ForeignKey("campanha.id_campanha"), nullable=False)
    descricao_abrigo = Column(String(100))
    capacidade_maxima = Column(Integer)
    lotacao_atual = Column(Integer)
    logradouro = Column(String(100), nullable=True)
    numero = Column(Integer, nullable=True)
    complemento = Column(String(20), nullable=True)
    bairro = Column(String(20), nullable=True)
    cidade = Column(String(20))
    estado = Column(String(2))
    cep = Column(String(9))
    ativo = Column(Boolean, default=True)
    data_inclusao = Column(DateTime, default=func.now())
    data_atualizacao = Column(DateTime, default=func.now())

    campanha = relationship("Campanha")

                
    def __init__(self, fk_campanha: int, descricao_abrigo:str, capacidade_maxima: int,
                 lotacao_atual: int, logradouro:str, numero: int,
                 complemento: str, bairro: str, cidade: str, estado: str, cep: str,
                 ativo:bool = True, 
                 data_inclusao:Union[DateTime, None] = None, 
                 data_atualizacao:Union[DateTime, None] = None):
        """
        Cria um abrigo vinculado a uma campanha existente

        Arguments:
            fk_campanha: vincula um abrigo a uma campanha
            descricao_abrigo: descreve o abrigo
            capacidade_maxima: capacidade máxima de pessoas atendidas
            lotacao_atual: total de atendidos na data de atualização
            logradouro: nome do logradouro
            numero: numero do logradouro
            complemento: complemento do endereço
            bairro: bairro do endereço
            cidade: cidade do endereço
            estado: UF do endereço
            cep: código CEP do endereço com 9 dígitos (00000-000)
            ativo: status do abrigo
            data_inclusao: data da criação do abrigo
            data_atualizacao: data da atualização da lotação atual
        """
        self.fk_campanha = fk_campanha
        self.descricao_abrigo = descricao_abrigo
        self.capacidade_maxima = capacidade_maxima
        self.lotacao_atual = lotacao_atual
        self.ativo = ativo
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep        
        self.data_inclusao = data_inclusao
        self.data_atualizacao = data_atualizacao

        if data_inclusao:
            self.data_inclusao = data_inclusao
        
        if data_atualizacao:
            self.data_atualizacao = data_atualizacao