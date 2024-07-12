from typing import List
from pydantic import BaseModel
from model.suprimento import Suprimento

class SuprimentoSchema(BaseModel):
    
    """ Define como uma nova suprimento deve ser inserida
    """
    descricao_suprimento: str = "Água 1,5 litros"
    qtd_para_pessoa_semana: int
   

class SuprimentoViewSchema(BaseModel):
    
    """ Define como um suprimento será retornado
    """
    id_suprimento: int
    descricao_suprimento: str = "Água 1,5 litros"
    qtd_para_pessoa_semana: int


class ListagemSuprimentosSchema(BaseModel):
    
    """ Define como uma listagem de suprimentos será retornada.
    """
    suprimentos:List[SuprimentoSchema]
    
    
class SuprimentoBuscaSchema(BaseModel):
    
    """ Define como deve ser a estrutura que representa a busca. 
        Busca pelo ID do suprimento.
    """
    id_suprimento: str


class SuprimentoDelUpdateSchema(BaseModel):
    
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    nome: str
    

class TemAbrigosSchema(BaseModel):
    """ Define como deve ser a estrutura que representa se uma suprimento tem abrigos associados. """

    tem_abrigos: bool


def exibe_suprimento(suprimento: Suprimento):
    
    """ Retorna uma representação de suprimento seguindo o schema definido em
        SuprimentoViewSchema.
    """
    return {
        "id_suprimento": suprimento.id_suprimento,
        "descricao_suprimento": suprimento.descricao_suprimento,
        "qtd_para_pessoa_semana": suprimento.qtd_para_pessoa_semana
    }
    
    
def lista_suprimentos(suprimentos: List[Suprimento]):
    
    """ Retorna uma representação da suprimento seguindo o schema definido em
        SuprimentoViewSchema.
    """
    result = []
    
    for suprimento in suprimentos:
        result.append({
            "id_suprimento": suprimento.id_suprimento,
            "descricao_suprimento": suprimento.descricao_suprimento,
            "qtd_para_pessoa_semana": suprimento.qtd_para_pessoa_semana
        })   
    return {"suprimentos": result}