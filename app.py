from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from routes.abrigo import add_abrigo, get_abrigo, get_abrigos, update_abrigo
from routes.abrigo_suprimento import get_abrigo_suprimentos
from routes.campanha import add_campanha, get_campanhas, del_campanha, tem_abrigos
from routes.suprimento import add_suprimento, del_suprimento, get_suprimento, get_suprimentos, update_suprimento
from schemas import *
from flask_cors import CORS

info = Info(title="Ajuda Mais", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc.")
campanha_tag = Tag(name="Campanha", description="Inclusão, visualização e remoção de campanhas.")
abrigo_tag = Tag(name="Abrigo", description="Inclusão, visualização, atualização e remoção de abrigos.")
suprimento_tag = Tag(name="Suprimento", description="Inclusão, visualização, atualização e remoção de suprimentos.")
abrigo_suprimento_tag = Tag(name="Abrigo Suprimento", description="Administração dos suprimentos nos abrigos.")

@app.get('/', tags=[home_tag])
def home():    
    
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rotas com funções definidas em routes/campanha.py

@app.get('/campanhas', tags=[campanha_tag],
         responses={"200": ListagemCampanhasSchema, "404": ErrorSchema})
def listar_campanhas():
    
    """Lista todas as campanhas cadastradas.

    Retorna uma representação da listagem de campanhas.
    """
    return get_campanhas()


@app.post('/campanha/', tags=[campanha_tag],
          responses={"200": CampanhaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def incluir_campanha(form: CampanhaSchema):

    """Adiciona uma nova campanha. 
    """
    return add_campanha(form)
    
    
@app.delete('/campanha', tags=[campanha_tag],
            responses={"200": CampanhaDelSchema, "404": ErrorSchema})
def excluir_campanha(query: CampanhaBuscaSchema):
    
    """Deleta uma campanha definitivamente.

    Retorna uma mensagem de confirmação da remoção.
    """
    return del_campanha(query)


@app.get('/campanha/tem_abrigos', tags=[campanha_tag],
        responses={"200": TemAbrigosSchema, "404": ErrorSchema})
def verificar_abrigos(query: CampanhaBuscaSchema):
    
    """Verifica se uma campanha tem abrigos associados.
    
    Retorna um booleano indicando se a campanha tem abrigos associados.
    """    
    return tem_abrigos(query)


# Rotas com funções definidas em routes/abrigo.py

@app.get('/abrigos', tags=[abrigo_tag],
         responses={"200": ListagemAbrigosSchema, "404": ErrorSchema})
def listar_abrigos(query: CampanhaBuscaSchema):

    """Lista todos os abrigos cadastrados em uma campanha.

    Retorna uma representação da listagem de abrigos.
    """
    return get_abrigos(query)


@app.get('/abrigo', tags=[abrigo_tag],
         responses={"200": AbrigoViewSchema, "404": ErrorSchema})
def busca_abrigo(query: AbrigoBuscaSchema):

    """Busca um abrigo pelo ID do abrigo.
    
       Retorna uma representação do abrigo.
    """    
    return get_abrigo(query)


@app.post('/abrigo/', tags=[abrigo_tag],
          responses={"200": AbrigoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def incluir_abrigo(form: AbrigoSchema):

    """Adiciona um novo abrigo.
    """    
    return add_abrigo(form)


@app.put('/abrigo', tags=[abrigo_tag],
         responses={"200": AbrigoViewSchema, "404": ErrorSchema})
def atualizar_abrigo(form: AbrigoViewSchema):
    
    """Atualiza um abrigo.

       Retorna uma mensagem de confirmação da atualização.
    """    
    return update_abrigo(form)


# Rotas com funções definidas em routes/suprimento.py

@app.get('/suprimentos', tags=[suprimento_tag],
         responses={"200": ListagemSuprimentosSchema, "404": ErrorSchema})
def listar_suprimentos():
    
    """Lista todos os suprimentos cadastrados.

    Retorna uma representação da listagem de suprimentos.
    """
    return get_suprimentos()


@app.get('/suprimento', tags=[suprimento_tag],
         responses={"200": SuprimentoViewSchema, "404": ErrorSchema})
def busca_suprimento(query: SuprimentoBuscaSchema):

    """Busca um suprimento pelo ID do suprimento.
    
       Retorna uma representação do suprimento.
    """    
    return get_suprimento(query)


@app.post('/suprimento/', tags=[suprimento_tag],
          responses={"200": SuprimentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def incluir_suprimento(form: SuprimentoSchema):

    """Adiciona um novo suprimento. 
    """
    return add_suprimento(form)
    
    
@app.delete('/suprimento', tags=[suprimento_tag],
            responses={"200": SuprimentoDelUpdateSchema, "404": ErrorSchema})
def excluir_suprimento(query: SuprimentoBuscaSchema):
    
    """Deleta um suprimento definitivamente.

    Retorna uma mensagem de confirmação da remoção.
    """
    return del_suprimento(query)


@app.put('/suprimento', tags=[suprimento_tag],
         responses={"200": SuprimentoDelUpdateSchema, "404": ErrorSchema})
def atualizar_suprimento(form: SuprimentoViewSchema):
    
    """Atualiza um suprimento.

       Retorna uma mensagem de confirmação da atualização.
    """    
    return update_suprimento(form)


# Rotas com funções definidas em routes/abrigo_suprimento.py

@app.get('/abrigo_suprimentos', tags=[abrigo_suprimento_tag],
         responses={"200": ListagemAbrigoSuprimentosSchema, "404": ErrorSchema})
def lista_abrigo_suprimentos(query: AbrigoSuprimentoBuscaSchema):

    """Lista todos os suprimentos associados a um abrigo.

    Retorna uma representação da listagem de suprimentos por abrigo.
    """
    return get_abrigo_suprimentos(query)