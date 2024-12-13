import requests
from bs4 import BeautifulSoup
from flask import jsonify, request

def scrape_data(url,headers=None):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.select('.tb_dados')
    return [item.text for item in data]

def producao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    data = scrape_data(url, headers=headers)
    return jsonify(data)

def processamento(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'
    data = scrape_data(url, headers=headers)
    return jsonify(data)

def comercializacao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
    data = scrape_data(url, headers=headers)
    return jsonify(data)

def importacao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'
    data = scrape_data(url,headers=headers)
    return jsonify(data)

def exportacao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06'
    data = scrape_data(url,headers=headers)
    return jsonify(data)
