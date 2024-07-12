import datetime as dt
from pydantic import BaseModel
from typing import List, Optional
from model.abrigo import Abrigo

class AbrigoSchema(BaseModel):
    
    """ Define como um novo abrigo deve ser inserido
    """
    fk_campanha: int
    descricao_abrigo: str = "Escola Municipal Dona Ana"
    capacidade_maxima: int
    lotacao_atual: int
    logradouro: Optional[str] = None 
    numero: Optional[int] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None
    ativo: bool = True
    data_inclusao: dt.datetime = dt.datetime.now()
    data_atualizacao: dt.datetime = dt.datetime.now()
 

class AbrigoBuscaSchema(BaseModel):
    
    """ Define como deve ser a estrutura que representa a busca. 
        Busca pelo ID do abrigo.
    """
    id_abrigo: str
 

class ListagemAbrigosSchema(BaseModel):
    
    """ Define como uma listagem de abrigos será retornada.
    """
    abrigos:List[AbrigoSchema]


class AbrigoViewSchema(BaseModel):
    
    """ Define como uma abrigo será retornada.
    """
    id_abrigo: int
    fk_campanha: int
    descricao_abrigo: str = "Escola Municipal Dona Ana"
    capacidade_maxima: int
    lotacao_atual: int
    logradouro: Optional[str] = None 
    numero: Optional[int] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None
    ativo: bool = True
    data_inclusao: dt.datetime = dt.datetime.now()
    data_atualizacao: dt.datetime = dt.datetime.now()

 
class AbrigoDelUpdateSchema(BaseModel):
    
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de exclusão ou de atualização. 
    """
    mensagem: str
    nome: str


def exibe_abrigo(abrigo: Abrigo):
    
    """ Retorna uma representação da abrigo seguindo o schema definido em
        AbrigoViewSchema.
    """
    return {
        "id_abrigo": abrigo.id_abrigo,
        "fk_campanha": abrigo.fk_campanha,
        "descricao_abrigo": abrigo.descricao_abrigo,
        "capacidade_maxima": abrigo.capacidade_maxima,
        "lotacao_atual": abrigo.lotacao_atual,
        "logradouro": abrigo.logradouro,
        "numero": abrigo.numero,
        "complemento": abrigo.complemento,
        "bairro": abrigo.bairro,
        "cidade": abrigo.cidade,
        "estado": abrigo.estado,
        "cep": abrigo.cep,
        "ativo": abrigo.ativo,         
        "data_inclusao": abrigo.data_inclusao,
        "data_atualizacao": abrigo.data_atualizacao
    }


def lista_abrigos(abrigos: List[Abrigo]):
    
    """ Retorna uma representação de uma lista de abrigos seguindo o schema definido em
        AbrigoViewSchema.
    """
    result = []
    
    for abrigo in abrigos:
        result.append({
            "id_abrigo": abrigo.id_abrigo,
            "fk_campanha": abrigo.fk_campanha,
            "descricao_abrigo": abrigo.descricao_abrigo,
            "capacidade_maxima": abrigo.capacidade_maxima,
            "lotacao_atual": abrigo.lotacao_atual,
            "logradouro": abrigo.logradouro,
            "numero": abrigo.numero,
            "complemento": abrigo.complemento,
            "bairro": abrigo.bairro,
            "cidade": abrigo.cidade,
            "estado": abrigo.estado,
            "cep": abrigo.cep,            
            "ativo": abrigo.ativo,
            "data_inclusao": abrigo.data_inclusao,
            "data_atualizacao": abrigo.data_atualizacao
        })   
    return {"abrigos": result}
