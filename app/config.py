class Config:
    SECRET_KEY = 'your_secret_key'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Tech Challenge Fase 1 Grupo 37',
        'uiversion': 3,
        'securityDefinitions': {
            'BearerAuth': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"'
            }
        }
    }
