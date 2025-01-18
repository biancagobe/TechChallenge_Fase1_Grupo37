from flask import jsonify
from flask import Flask, redirect
from app import app, auth
from app.services.scraping_service import producao, processamento, comercializacao, importacao, exportacao
from flasgger import swag_from

@app.route('/')
def home():
    return redirect('/apidocs')

@app.route('/producao/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Producao'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Dados de produção.',
            'schema': {
                'type': 'object'
            }
        },
        '401': {
            'description': 'Não autorizado.'
        }
    }
})
@auth.login_required
def auth_producao(id):
    return producao(id)

@app.route('/processamento/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Processamento'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Dados de processamento.',
            'schema': {
                'type': 'object'
            }
        },
        '401': {
            'description': 'Não autorizado.'
        }
    }
})
@auth.login_required
def auth_processamento(id):
    return processamento(id)

@app.route('/comercializacao/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Comercializacao'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Dados de comercialização.',
            'schema': {
                'type': 'object'
            }
        },
        '401': {
            'description': 'Não autorizado.'
        }
    }
})
@auth.login_required
def auth_comercializacao(id):
    return comercializacao(id)

@app.route('/importacao/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Importacao'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Dados de importação.',
            'schema': {
                'type': 'object'
            }
        },
        '401': {
            'description': 'Não autorizado.'
        }
    }
})
@auth.login_required
def auth_importacao(id):
    return importacao(id)

@app.route('/exportacao/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Exportacao'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Dados de exportação.',
            'schema': {
                'type': 'object'
            }
        },
        '401': {
            'description': 'Não autorizado.'
        }
    }
})
@auth.login_required
def auth_exportacao(id):
    return exportacao(id)