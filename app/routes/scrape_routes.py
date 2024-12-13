from flask import request, jsonify
from app import app, auth
from app.services.scraping_service import producao, processamento, comercializacao, importacao, exportacao

@app.route('/scrape/producao', methods=['GET'])
@auth.login_required
def scrape_producao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return producao(url,headers=headers)

@app.route('/scrape/processamento', methods=['GET'])
@auth.login_required
def scrape_processamento():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return processamento(url,headers=headers)

@app.route('/scrape/comercializacao', methods=['GET'])
@auth.login_required
def scrape_comercializacao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return comercializacao(url,headers=headers)

@app.route('/scrape/importacao', methods=['GET'])
@auth.login_required
def scrape_importacao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return importacao(url,headers=headers)

@app.route('/scrape/exportacao', methods=['GET'])
@auth.login_required
def scrape_exportacao():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    return exportacao(url,headers=headers)