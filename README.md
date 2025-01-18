# TECH CHALLENGE - FASE 1 - GRUPO 37

Este é um projeto de API rest desenvolvido com Flask utilizando linguagem Python, que inclui web scraping utilizando beautifulsoup e autenticação JWT para consulta de dados na pagina Web site Embrapa.

[![N|Solid](https://seeklogo.com/images/E/Embrapa-logo-3C71B11BFE-seeklogo.com.png)](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06)

## 🚀 Funcionalidades

- **Autenticação:** As rotas da API são protegidas por autenticação JWT (JSON Web Token), garantindo maior segurança e controle de acesso. Esse método utiliza tokens para validar a identidade do usuário antes de permitir o acesso às rotas protegidas
- **Web Scraping:** Extração eficiente de informações de páginas web (títulos, cabeçalhos e parágrafos) usando BeautifulSoup.
- **Cache:** Otimização de desempenho com cache implementado para evitar consultas repetitivas e melhorar a velocidade.
- **Documentação:** Documentação automática com Swagger

## 📁 Estrutura do Projeto

```bash
TechChallenge_Fase1_Grupo37/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── scrape_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── scraping_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   └── config.py
├── requirements.txt
├── README.md
└── run.py
```

- **`app/`**: Diretório principal do aplicativo.
  - **`routes/`**: Contém as rotas organizadas por funcionalidades.
  - **`services/`**: Serviços para lógica de negócios, como scraping.
  - **`utils/`**: Utilitários, como autenticação.
  - **`config.py`**: Configurações da aplicação Flask.
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Documentação do projeto.
---

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/biancagobe/TechChallenge_Fase1_Grupo37.git
cd TechChallenge_Fase1_Grupo37
```

### 2. Crie um Ambiente Virtualpython

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

O aplicativo estará disponível em `http://localhost:5000`.

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`. A rota raiz (`http://localhost:5000/`) também direciona automaticamente para a documentação.

## 🤝 Contribuindo

1. Fork este repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.