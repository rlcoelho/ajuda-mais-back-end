from typing import List
from pydantic import BaseModel
from model.abrigo_suprimento import AbrigoSuprimento

class AbrigoSuprimentoSchema(BaseModel):
    
    """ Define como deve ser inserido o suprimento de um abrigo
    """
    fk_abrigo: int
    fk_suprimento: int
    qtd_atual: int


class AbrigoSuprimentoViewSchema(BaseModel):
    
    """ Define como será retornado o suprimento de um abrigo
    """
    fk_abrigo: int
    fk_suprimento: int
    qtd_atual: int   
    descricao_abrigo: str
    capacidade_maxima: int
    lotacao_atual: int
    descricao_suprimento: str
    qtd_para_pessoa_semana: int


class ListagemAbrigoSuprimentosSchema(BaseModel):
    
    """ Define como uma listagem de abrigo_suprimentos será retornada.
    """
    abrigo_suprimentos:List[AbrigoSuprimentoViewSchema]
    
    
class AbrigoSuprimentoBuscaSchema(BaseModel):
    
    """ Define como deve ser a estrutura que representa a busca. 
        Busca pelo ID do abrigo todos os suprimentos associados.
    """
    fk_abrigo: str


class AbrigoSuprimentoDelSchema(BaseModel):
    
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    nome: str
    

def exibe_abrigo_suprimento(abrigo_suprimento: AbrigoSuprimento):
    
    """ Retorna uma representação da abrigo_suprimento seguindo o schema definido em
        AbrigoSuprimentoViewSchema.
    """
    return {
        "id_abrigo_suprimento": abrigo_suprimento.id_abrigo_suprimento,
        "fk_abrigo": abrigo_suprimento.fk_abrigo,
        "fk_suprimento": abrigo_suprimento.fk_suprimento,
        "qtd_atual": abrigo_suprimento.qtd_atual
    }
    

def lista_abrigo_suprimentos(abrigo_suprimentos: List[AbrigoSuprimento]):
    
    """ Retorna uma representação de uma lista da abrigo_suprimento seguindo o schema definido em
        AbrigoSuprimentoViewSchema.
    """
    result = []
    
    for abrigo_suprimento in abrigo_suprimentos:
        result.append({
        "id_abrigo_suprimento": abrigo_suprimento.id_abrigo_suprimento,
        "fk_abrigo": abrigo_suprimento.fk_abrigo,
        "fk_suprimento": abrigo_suprimento.fk_suprimento,
        "qtd_atual": abrigo_suprimento.qtd_atual
        })   
    return {"abrigo_suprimentos": result}
