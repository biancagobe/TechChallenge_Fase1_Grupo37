from flask import jsonify, request
from app import app, auth
from app.services.scraping_service import producao, processamento, comercializacao, importacao, exportacao

@app.route('/producao/<int:id>', methods=['GET'])
@auth.login_required
def auth_producao(id):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return producao(id,headers=headers)

@app.route('/processamento/<int:id>', methods=['GET'])
@auth.login_required
def auth_processamento(id):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return processamento(id,headers=headers)

@app.route('/comercializacao/<int:id>', methods=['GET'])
@auth.login_required
def auth_comercializacao(id):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return comercializacao(id,headers=headers)

@app.route('/importacao/<int:id>', methods=['GET'])
@auth.login_required
def auth_importacao(id):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return importacao(id,headers=headers)

@app.route('/exportacao/<int:id>', methods=['GET'])
@auth.login_required
def auth_exportacao(id):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return exportacao(id,headers=headers)