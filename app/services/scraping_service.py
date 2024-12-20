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

def producao(id,headers=None):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={id}&opcao=opt_02'
    data = scrape_data(url, headers=headers) 
    return jsonify(data.to_dict(orient='records'))

def processamento(id,headers=None):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={id}&opcao=opt_03'
    data = scrape_data(url, headers=headers)
    return jsonify(data.to_dict(orient='records'))

def comercializacao(id,headers=None):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={id}&opcao=opt_04'
    data = scrape_data(url, headers=headers)
    return jsonify(data.to_dict(orient='records'))

def importacao(id,headers=None):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={id}&opcao=opt_05'
    data = scrape_data(url,headers=headers)
    return jsonify(data.to_dict(orient='records'))

def exportacao(id,headers=None):
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={id}&opcao=opt_06'
    data = scrape_data(url,headers=headers)
    return jsonify(data.to_dict(orient='records'))
