import requests
import pandas as pd
from bs4 import BeautifulSoup
from flask import jsonify, request

def scrape_data(url,headers=None):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table',{'class':'tb_base tb_dados'})
    rows = table.find_all('tr')
    data = []

    for row in rows:
        cells = row.find_all(['th','td'])
        cells_text = [cell.get_text(strip=True)for cell in cells]
        data.append(cells_text)
    df = pd.DataFrame(data)
    df = pd.DataFrame(data[1:],columns=data[0])
    return df

def producao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    data = scrape_data(url, headers=headers)
    return jsonify(data.to_dict(orient='records'))

def processamento(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'
    data = scrape_data(url, headers=headers)
    return jsonify(data.to_dict(orient='records'))

def comercializacao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
    data = scrape_data(url, headers=headers)
    return jsonify(data.to_dict(orient='records'))

def importacao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'
    data = scrape_data(url,headers=headers)
    return jsonify(data.to_dict(orient='records'))

def exportacao(url, headers=None):
    headers = {
        'Authorization': f'Bearer {request.headers.get("Authorization")}'
    }
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06'
    data = scrape_data(url,headers=headers)
    return jsonify(data.to_dict(orient='records'))
