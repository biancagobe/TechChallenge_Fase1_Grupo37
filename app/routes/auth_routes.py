from flask import jsonify, request
from app import app, auth
from app.services.scraping_service import producao, processamento, comercializacao, importacao, exportacao

@app.route('/producao', methods=['GET'])
@auth.login_required
def auth_producao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return producao(url,headers=headers)

@app.route('/processamento', methods=['GET'])
@auth.login_required
def auth_processamento():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return processamento(url,headers=headers)

@app.route('/comercializacao', methods=['GET'])
@auth.login_required
def auth_comercializacao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return comercializacao(url,headers=headers)

@app.route('/importacao', methods=['GET'])
@auth.login_required
def auth_importacao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return importacao(url,headers=headers)

@app.route('/exportacao', methods=['GET'])
@auth.login_required
def auth_exportacao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return exportacao(url,headers=headers)