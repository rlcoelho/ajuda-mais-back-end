from typing import List
from pydantic import BaseModel
from model.campanha import Campanha

class CampanhaSchema(BaseModel):
    
    """ Define como uma nova campanha deve ser inserida
    """
    descricao_campanha: str = "SOS Rio Grande do Sul"
    

class CampanhaViewSchema(BaseModel):
    
    """ Define como uma campanha será retornada
    """
    id_campanha: int
    descricao_campanha: str = "SOS Rio Grande do Sul"


class ListagemCampanhasSchema(BaseModel):
    
    """ Define como uma listagem de campanhas será retornada.
    """
    campanhas:List[CampanhaSchema]
    
    
class CampanhaBuscaSchema(BaseModel):
    
    """ Define como deve ser a estrutura que representa a busca. 
        Busca pelo ID da campanha.
    """
    id_campanha: str


class CampanhaDelSchema(BaseModel):
    
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    nome: str
    

class TemAbrigosSchema(BaseModel):
    """ Define como deve ser a estrutura que representa se uma campanha tem abrigos associados. """

    tem_abrigos: bool


def exibe_campanha(campanha: Campanha):
    
    """ Retorna uma representação da campanha seguindo o schema definido em
        CampanhaViewSchema.
    """
    return {
        "id_campanha": campanha.id_campanha,
        "descricao_campanha": campanha.descricao_campanha
    }
    
    
def lista_campanhas(campanhas: List[Campanha]):
    
    """ Retorna uma representação da campanha seguindo o schema definido em
        CampanhaViewSchema.
    """
    result = []
    
    for campanha in campanhas:
        result.append({
            "id_campanha": campanha.id_campanha,
            "descricao_campanha": campanha.descricao_campanha
        })   
    return {"campanhas": result}