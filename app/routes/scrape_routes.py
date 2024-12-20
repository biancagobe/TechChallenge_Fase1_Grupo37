from flask import request, jsonify
from app import app, auth
from app.services.scraping_service import producao, processamento, comercializacao, importacao, exportacao

@app.route('/producao/<int:id>', methods=['GET'])
@auth.login_required
def scrape_producao(id):
    """
    Extrai dados da página produção para um ID específico.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do recurso de produção.
    responses:
      200:
        description: Dados de produção.
        schema:
          type: array
          items:
            type: object
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return producao(id, headers=headers)

@app.route('/processamento/<int:id>', methods=['GET'])
@auth.login_required
def scrape_processamento(id):
    """
    Extrai dados da página processamento para um ID específico.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do recurso de processamento.
    responses:
      200:
        description: Dados de processamento.
        schema:
          type: array
          items:
            type: object
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return processamento(id, headers=headers)

@app.route('/comercializacao/<int:id>', methods=['GET'])
@auth.login_required
def scrape_comercializacao(id):
    """
    Extrai dados da página comercialização para um ID específico.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do recurso de comercialização.
    responses:
      200:
        description: Dados de comercialização.
        schema:
          type: array
          items:
            type: object
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return comercializacao(id, headers=headers)

@app.route('/importacao/<int:id>', methods=['GET'])
@auth.login_required
def scrape_importacao(id):
    """
    Extrai dados da página importação para um ID específico.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do recurso de importação.
    responses:
      200:
        description: Dados de importação.
        schema:
          type: array
          items:
            type: object
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return importacao(id, headers=headers)

@app.route('/exportacao/<int:id>', methods=['GET'])
@auth.login_required
def scrape_exportacao(id):
    """
    Extrai dados da página exportação para um ID específico.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do recurso de exportação.
    responses:
      200:
        description: Dados de exportação.
        schema:
          type: array
          items:
            type: object
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return exportacao(id, headers=headers)